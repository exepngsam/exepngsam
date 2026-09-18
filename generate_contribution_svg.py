"""
generate_contribution_svg.py
Generates a high-end, cyberpunk-themed animated GitHub contribution calendar SVG
using pure SMIL animations with diagonal "slant reveal" and specular flash glints.
Fetches live data from GitHub for @exepngsam with fallback snapshot.
"""

import os
import re
import math
import requests
from datetime import datetime, timedelta

USERNAME = "exepngsam"
OUTPUT_FILE = "github-contribution-animation.svg"

# Palette: Cyberpunk Dark Mode & Neon Accents
COLORS = {
    0: "#161b22",          # Inactive base
    1: "#0e4429",          # Level 1 - Subtle dark emerald
    2: "#006d32",          # Level 2 - Medium emerald
    3: "#26a641",          # Level 3 - Bright green (outer glow)
    4: "#39d353",          # Level 4 - Cyber neon green (peak glow)
    "purple": "#a855f7",   # Special peak / milestone accent
    "bg": "#0d1117",       # Card background
    "border": "#30363d",   # Card border
    "text_main": "#e6edf3",# Primary text
    "text_muted": "#7d8590",# Secondary text
    "cyan": "#00f0ff",     # Cyan accent
}

# Offline fallback snapshot extracted from live GitHub profile (109 contributions)
FALLBACK_ACTIVE_DAYS = {
    # (row, col): (level, count, date_str)
    (0, 48): (4, 13, "2026-08-16"),
    (1, 40): (1, 1,  "2026-06-22"),
    (1, 50): (1, 1,  "2026-08-31"),
    (1, 51): (1, 1,  "2026-09-07"),
    (2, 48): (1, 3,  "2026-08-18"),
    (2, 50): (2, 4,  "2026-09-01"),
    (2, 51): (2, 7,  "2026-09-08"),
    (2, 52): (1, 1,  "2026-09-15"),
    (3, 51): (3, 8,  "2026-09-09"),
    (3, 52): (4, 15, "2026-09-16"),
    (4, 52): (1, 1,  "2026-09-17"),
    (5, 48): (4, 25, "2026-08-21"),
    (5, 52): (4, 13, "2026-09-18"),
    (6, 47): (2, 7,  "2026-08-15"),
    (6, 48): (3, 9,  "2026-08-22"),
}
FALLBACK_TOTAL = 109


def fetch_contributions(username=USERNAME):
    """Fetches real contributions calendar for the user from GitHub."""
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    grid = {}
    total_count = FALLBACK_TOTAL
    months_data = []

    try:
        resp = requests.get(url, headers=headers, timeout=8)
        if resp.status_code == 200:
            html = resp.text
            # Extract total count
            m_total = re.search(r'([0-9,]+)\s+contributions\s+in the last year', html)
            if m_total:
                total_count = int(m_total.group(1).replace(",", ""))

            # Extract cells: id="contribution-day-component-{row}-{col}" data-date="..." data-level="..."
            cell_matches = re.finditer(r'<td\b([^>]*)>', html)
            for m in cell_matches:
                attrs = m.group(1)
                id_m = re.search(r'id="contribution-day-component-(\d+)-(\d+)"', attrs)
                level_m = re.search(r'data-level="(\d+)"', attrs)
                date_m = re.search(r'data-date="(\d{4}-\d{2}-\d{2})"', attrs)
                if id_m and level_m:
                    row = int(id_m.group(1))
                    col = int(id_m.group(2))
                    level = int(level_m.group(1))
                    date = date_m.group(1) if date_m else ""
                    grid[(row, col)] = {
                        "level": level,
                        "date": date,
                        "count": 0
                    }

            # Parse tooltips for exact count
            tooltips = dict(re.findall(r'for="([^"]+)"[^>]*>(.*?)</tool-tip>', html, re.DOTALL))
            for (row, col), data in grid.items():
                cid = f"contribution-day-component-{row}-{col}"
                if cid in tooltips:
                    tt = tooltips[cid]
                    count_m = re.search(r'(\d+)\s+contribution', tt)
                    if count_m:
                        data["count"] = int(count_m.group(1))

            # Extract month headers
            month_spans = re.findall(r'<td[^>]*class="ContributionCalendar-label"[^>]*colspan="(\d+)"[^>]*>.*?<span aria-hidden="true"[^>]*>([A-Za-z]+)</span>', html, re.DOTALL)
            cur_col = 0
            for colspan, mname in month_spans:
                months_data.append((cur_col, mname))
                cur_col += int(colspan)

            if len(grid) >= 300:
                print(f"[OK] Successfully fetched live GitHub contributions for {username}: {total_count} total contributions.")
                return grid, total_count, months_data
    except Exception as e:
        print(f"[WARN] Live fetch failed ({e}). Using robust fallback snapshot.")

    # Populate fallback grid (53 columns x 7 rows)
    grid = {}
    for r in range(7):
        for c in range(53):
            if (r, c) in FALLBACK_ACTIVE_DAYS:
                lvl, cnt, dt = FALLBACK_ACTIVE_DAYS[(r, c)]
                grid[(r, c)] = {"level": lvl, "count": cnt, "date": dt}
            else:
                grid[(r, c)] = {"level": 0, "count": 0, "date": ""}

    default_months = [
        (0, "Sep"), (4, "Oct"), (8, "Nov"), (13, "Dec"),
        (17, "Jan"), (21, "Feb"), (25, "Mar"), (30, "Apr"),
        (34, "May"), (39, "Jun"), (43, "Jul"), (47, "Aug"), (51, "Sep")
    ]
    return grid, FALLBACK_TOTAL, default_months


def generate_svg(grid, total_count, months_data, output_path=OUTPUT_FILE):
    """Generates the full SMIL-animated SVG."""
    cell_size = 11
    cell_gap = 4
    step = cell_size + cell_gap  # 15px

    left_margin = 48
    top_margin = 84
    cols_count = 53
    rows_count = 7

    grid_width = cols_count * step
    width = grid_width + left_margin + 36  # ~879px
    height = top_margin + rows_count * step + 56  # ~245px

    # Compute max diagonal for slant delay
    # Slant from bottom-left (col=0, row=6 -> d=0) to top-right (col=52, row=0 -> d=58)
    max_d = (cols_count - 1) + (rows_count - 1)  # 52 + 6 = 58
    delay_step = 0.024  # seconds per diagonal step (total reveal ~1.4s)

    svg_parts = []
    # Header & Styles
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="max-width: {width}px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="50%" stop-color="#0e131b" />
      <stop offset="100%" stop-color="#141a23" />
    </linearGradient>

    <!-- Glassmorphic Border Gradient -->
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.6" />
      <stop offset="35%" stop-color="#30363d" stop-opacity="0.8" />
      <stop offset="70%" stop-color="#39d353" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0.6" />
    </linearGradient>

    <!-- Neon Glow Filter for Level 3 & Level 4 squares -->
    <filter id="neon-glow-l3" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="neon-glow-l4" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3.2" result="blur1" />
      <feGaussianBlur in="SourceGraphic" stdDeviation="1.5" result="blur2" />
      <feMerge>
        <feMergeNode in="blur1" />
        <feMergeNode in="blur2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="specular-glint" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="1.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .terminal-btn {{ transition: transform 0.2s ease; }}
    .terminal-btn:hover {{ transform: scale(1.2); }}
    .month-label {{ font-size: 10px; fill: #7d8590; font-weight: 500; font-family: monospace; }}
    .day-label {{ font-size: 9px; fill: #7d8590; font-weight: 500; font-family: monospace; }}
    .title-text {{ font-size: 13px; font-weight: 700; fill: #e6edf3; letter-spacing: 0.5px; }}
    .badge-text {{ font-size: 11px; font-weight: 600; fill: #00f0ff; font-family: monospace; }}
    .legend-text {{ font-size: 10px; fill: #7d8590; font-family: monospace; }}
    .stat-number {{ font-size: 13px; font-weight: 800; fill: #39d353; font-family: monospace; }}
  </style>

  <!-- Base Card Frame with Glowing Border -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="14" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5" />

  <!-- Top Terminal Bar -->
  <g transform="translate(18, 16)">
    <!-- Window buttons -->
    <circle cx="0" cy="6" r="4.5" fill="#ff5f56" class="terminal-btn" />
    <circle cx="14" cy="6" r="4.5" fill="#ffbd2e" class="terminal-btn" />
    <circle cx="28" cy="6" r="4.5" fill="#27c93f" class="terminal-btn" />

    <!-- Terminal Window Title -->
    <text x="46" y="9" class="title-text">
      <tspan fill="#00f0ff">~/cyberdeck</tspan>
      <tspan fill="#7d8590"> / </tspan>
      <tspan fill="#e6edf3">github-contribution-graph</tspan>
      <tspan fill="#7d8590">.svg</tspan>
    </text>

    <!-- Pulsing Live Indicator -->
    <g transform="translate({width - 240}, 1)">
      <rect x="0" y="0" width="195" height="20" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1" />
      <circle cx="12" cy="10" r="3.5" fill="#39d353">
        <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />
        <animate attributeName="r" values="3.5;5;3.5" dur="2s" repeatCount="indefinite" />
      </circle>
      <text x="24" y="14" class="badge-text">
        <tspan class="stat-number">{total_count}</tspan> CONTRIBUTIONS
      </text>
    </g>
  </g>

  <!-- Horizontal divider -->
  <line x1="16" y1="46" x2="{width - 16}" y2="46" stroke="#21262d" stroke-width="1" />
''')

    # Month Labels
    svg_parts.append('  <!-- Month Labels -->\n  <g>')
    for m_col, m_name in months_data:
        mx = left_margin + (m_col * step)
        my = top_margin - 10
        svg_parts.append(f'    <text x="{mx}" y="{my}" class="month-label">{m_name}</text>')
    svg_parts.append('  </g>\n')

    # Day Labels (Mon, Wed, Fri)
    svg_parts.append('  <!-- Day Labels -->\n  <g>')
    day_labels = {1: "Mon", 3: "Wed", 5: "Fri"}
    for r_idx, day_name in day_labels.items():
        dy = top_margin + (r_idx * step) + 9
        svg_parts.append(f'    <text x="{left_margin - 28}" y="{dy}" class="day-label">{day_name}</text>')
    svg_parts.append('  </g>\n')

    # 53x7 Grid Cells with Slant Reveal & Specular Glint Animations
    svg_parts.append('  <!-- Contribution Grid Cells -->\n  <g id="contribution-grid">')

    for col in range(cols_count):
        for row in range(rows_count):
            cell_data = grid.get((row, col), {"level": 0, "count": 0, "date": ""})
            lvl = cell_data["level"]
            cnt = cell_data.get("count", 0)
            date_str = cell_data.get("date", "")

            # Target color
            final_color = COLORS.get(lvl, COLORS[0])
            # Highlight highest active days with subtle cyberpunk purple or neon accent
            if lvl == 4 and cnt >= 15:
                final_color = COLORS["purple"]

            # Diagonal slant calculation:
            # Bottom-left (col=0, row=6) reveals first (diag=0)
            # Top-right (col=52, row=0) reveals last (diag=58)
            slant_diag = col + (6 - row)
            delay = slant_diag * delay_step

            cx = left_margin + col * step
            cy = top_margin + row * step

            filter_attr = ""
            if lvl == 3:
                filter_attr = ' filter="url(#neon-glow-l3)"'
            elif lvl == 4:
                filter_attr = ' filter="url(#neon-glow-l4)"'

            # Build SMIL animated rect
            # Behavior:
            # 1. Initially opacity=0, width=0, height=0
            # 2. At t=delay: bursts in with intense white/green specular glint (#ffffff -> #7ee787 -> final_color)
            # 3. Settles into final_color and full dimensions (11x11, rx=2.5)
            glint_color_start = "#ffffff" if lvl > 0 else "#388bfd"
            glint_color_mid = "#7ee787" if lvl > 0 else "#21262d"

            svg_parts.append(f'''    <rect x="{cx}" y="{cy}" width="{cell_size}" height="{cell_size}" rx="2.5" fill="{COLORS[0]}" opacity="0"{filter_attr}>
      <!-- Opacity reveal -->
      <animate attributeName="opacity" values="0; 1; 1" keyTimes="0; 0.2; 1" dur="0.45s" begin="{delay:.3f}s" fill="freeze" />
      <!-- Specular glint / flash transition -->
      <animate attributeName="fill" values="{glint_color_start}; {glint_color_mid}; {final_color}" keyTimes="0; 0.3; 1" dur="0.65s" begin="{delay:.3f}s" fill="freeze" />
      <!-- Subtle pop expansion -->
      <animate attributeName="width" values="{cell_size * 0.4}; {cell_size + 1.5}; {cell_size}" keyTimes="0; 0.4; 1" dur="0.5s" begin="{delay:.3f}s" fill="freeze" />
      <animate attributeName="height" values="{cell_size * 0.4}; {cell_size + 1.5}; {cell_size}" keyTimes="0; 0.4; 1" dur="0.5s" begin="{delay:.3f}s" fill="freeze" />
    </rect>''')

    svg_parts.append('  </g>\n')

    # Bottom Footer: Legend & Info
    legend_y = height - 20
    legend_x = width - 180
    svg_parts.append(f'''  <!-- Footer Legend & Info -->
  <g transform="translate(18, {legend_y})">
    <text x="0" y="9" class="legend-text">
      <tspan fill="#7d8590">STATUS: </tspan>
      <tspan fill="#39d353">READY_FOR_COMMITS</tspan>
      <tspan fill="#7d8590"> | USER: </tspan>
      <tspan fill="#00f0ff">@exepngsam</tspan>
      <tspan fill="#7d8590"> | SYSTEM: </tspan>
      <tspan fill="#a855f7">CYBERDECK_V2</tspan>
    </text>
  </g>

  <g transform="translate({legend_x}, {legend_y - 2})">
    <text x="-32" y="10" class="legend-text">Less</text>
    <rect x="0" y="1" width="10" height="10" rx="2" fill="{COLORS[0]}" />
    <rect x="14" y="1" width="10" height="10" rx="2" fill="{COLORS[1]}" />
    <rect x="28" y="1" width="10" height="10" rx="2" fill="{COLORS[2]}" />
    <rect x="42" y="1" width="10" height="10" rx="2" fill="{COLORS[3]}" filter="url(#neon-glow-l3)" />
    <rect x="56" y="1" width="10" height="10" rx="2" fill="{COLORS[4]}" filter="url(#neon-glow-l4)" />
    <text x="72" y="10" class="legend-text">More</text>
  </g>
</svg>''')

    svg_content = "\n".join(svg_parts)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[SUCCESS] Generated {output_path} ({len(svg_content)} bytes)")
    return output_path


def main():
    print(f"[*] Starting GitHub Contribution SVG Generation for user: {USERNAME}")
    grid, total, months = fetch_contributions(USERNAME)
    generate_svg(grid, total, months, OUTPUT_FILE)


if __name__ == "__main__":
    main()
