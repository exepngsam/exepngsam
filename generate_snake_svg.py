"""
generate_snake_svg.py
Generates the ultra-premium CyberDeck Contribution Snake Game SVG for @exepngsam.
Features live-fetched GitHub contributions, autonomous multi-segment glowing snake,
eating pulse animations, real-time score tracking, and 60 FPS zero-lag SMIL animations.
Width: 920px (matching header-liquid-glass.svg and terminal-card.svg).
"""

import re
import xml.etree.ElementTree as ET
import generate_contribution_svg

USERNAME = "exepngsam"
OUTPUT_FILE = "github-contribution-grid-snake.svg"

# Grid parameters matching 920px card width
COLS = 53
ROWS = 7
CELL_SIZE = 12
GAP = 4
STEP = CELL_SIZE + GAP  # 16px per column -> 53 * 16 = 848px
OFFSET_X = 36
OFFSET_Y = 52
WIDTH = 920
HEIGHT = 220


def generate_snake_svg(output_path=OUTPUT_FILE, grid=None, total_contribs=None, months=None):
    if grid is None or total_contribs is None:
        grid, total_contribs, months = generate_contribution_svg.fetch_contributions(USERNAME)

    # Coordinates for snake navigation path across the active cluster
    # Starting around col 28 and slithering through the commits at cols 40-52
    points = [
        (28 * STEP + OFFSET_X, 1 * STEP + OFFSET_Y),
        (35 * STEP + OFFSET_X, 1 * STEP + OFFSET_Y),
        (38 * STEP + OFFSET_X, 3 * STEP + OFFSET_Y),
        (40 * STEP + OFFSET_X, 1 * STEP + OFFSET_Y),
        (42 * STEP + OFFSET_X, 4 * STEP + OFFSET_Y),
        (45 * STEP + OFFSET_X, 4 * STEP + OFFSET_Y),
        (47 * STEP + OFFSET_X, 6 * STEP + OFFSET_Y),
        (48 * STEP + OFFSET_X, 6 * STEP + OFFSET_Y),
        (48 * STEP + OFFSET_X, 0 * STEP + OFFSET_Y),
        (50 * STEP + OFFSET_X, 0 * STEP + OFFSET_Y),
        (50 * STEP + OFFSET_X, 2 * STEP + OFFSET_Y),
        (51 * STEP + OFFSET_X, 2 * STEP + OFFSET_Y),
        (51 * STEP + OFFSET_X, 3 * STEP + OFFSET_Y),
        (52 * STEP + OFFSET_X, 3 * STEP + OFFSET_Y),
        (52 * STEP + OFFSET_X, 5 * STEP + OFFSET_Y),
        (51 * STEP + OFFSET_X, 5 * STEP + OFFSET_Y),
        (48 * STEP + OFFSET_X, 5 * STEP + OFFSET_Y),
        (48 * STEP + OFFSET_X, 2 * STEP + OFFSET_Y),
        (40 * STEP + OFFSET_X, 2 * STEP + OFFSET_Y),
        (28 * STEP + OFFSET_X, 1 * STEP + OFFSET_Y),
    ]

    path_d = f"M {points[0][0]} {points[0][1]} " + " ".join([f"L {p[0]} {p[1]}" for p in points[1:]]) + " Z"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="auto" style="max-width: {WIDTH}px; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SFMono-Regular', Consolas, monospace;">
  <defs>
    <!-- Liquid Glass Dark Background -->
    <linearGradient id="snake-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141c28" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#0e141e" stop-opacity="0.97" />
      <stop offset="100%" stop-color="#080c12" stop-opacity="0.99" />
    </linearGradient>

    <!-- Liquid Iridescent Border -->
    <linearGradient id="snake-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#00f0ff;#39d353;#a855f7;#00f0ff" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#39d353" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#39d353;#a855f7;#00f0ff;#39d353" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Specular Light Sweep Gradient -->
    <linearGradient id="snake-shimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.16" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <!-- Snake Gradient Body -->
    <linearGradient id="snake-body-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f0ff" />
      <stop offset="50%" stop-color="#39d353" />
      <stop offset="100%" stop-color="#a855f7" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-filter" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="intense-glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="5" result="b1" />
      <feGaussianBlur stdDeviation="2" result="b2" />
      <feMerge>
        <feMergeNode in="b1" />
        <feMergeNode in="b2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .game-title {{ font-size: 11.5px; font-weight: 700; fill: #7d8590; font-family: monospace; }}
    .month-lbl {{ font-size: 9px; fill: #58a6ff; font-weight: 600; font-family: monospace; }}
    .day-lbl {{ font-size: 8.5px; fill: #7d8590; font-family: monospace; font-weight: 600; }}
    .footer-stat {{ font-size: 9.5px; font-weight: 700; fill: #7d8590; font-family: monospace; }}
  </style>

  <!-- Outer Liquid Glass Frame (Matching 920px wide) -->
  <rect x="3" y="3" width="{WIDTH - 6}" height="{HEIGHT - 6}" rx="18" fill="url(#snake-card-bg)" stroke="url(#snake-border)" stroke-width="1.8" />

  <!-- Animated Specular Light Beam -->
  <rect x="-220" y="3" width="220" height="{HEIGHT - 6}" rx="18" fill="url(#snake-shimmer)" pointer-events="none">
    <animate attributeName="x" values="-220; {WIDTH + 220}" dur="6s" repeatCount="indefinite" />
  </rect>

  <!-- Title Bar -->
  <g transform="translate(24, 20)">
    <circle cx="0" cy="0" r="4.5" fill="#ff5f56" />
    <circle cx="14" cy="0" r="4.5" fill="#ffbd2e" />
    <circle cx="28" cy="0" r="4.5" fill="#27c93f" />
    <text x="44" y="4" class="game-title">
      <tspan fill="#00f0ff">snake@cyberdeck</tspan>: <tspan fill="#39d353">contributions.eat()</tspan> ~ <tspan fill="#ffffff">{total_contribs} dots consumed</tspan>
    </text>

    <!-- Top Right Live Status Pill -->
    <g transform="translate({WIDTH - 48 - 180}, -8)">
      <rect x="0" y="0" width="160" height="20" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1" />
      <circle cx="14" cy="10" r="3" fill="#39d353">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="1.2s" repeatCount="indefinite" />
      </circle>
      <text x="26" y="13.5" font-size="9" fill="#39d353" font-weight="800" font-family="monospace">
        LIVE_AI: <tspan fill="#00f0ff">AUTONOMOUS</tspan>
      </text>
    </g>
  </g>

  <!-- Month Headers -->
  <g transform="translate({OFFSET_X}, 42)">
    <text x="0" y="0" class="month-lbl">Sep</text>
    <text x="{4 * STEP}" y="0" class="month-lbl">Oct</text>
    <text x="{9 * STEP}" y="0" class="month-lbl">Nov</text>
    <text x="{13 * STEP}" y="0" class="month-lbl">Dec</text>
    <text x="{18 * STEP}" y="0" class="month-lbl">Jan</text>
    <text x="{22 * STEP}" y="0" class="month-lbl">Feb</text>
    <text x="{26 * STEP}" y="0" class="month-lbl">Mar</text>
    <text x="{31 * STEP}" y="0" class="month-lbl">Apr</text>
    <text x="{35 * STEP}" y="0" class="month-lbl">May</text>
    <text x="{40 * STEP}" y="0" class="month-lbl">Jun</text>
    <text x="{44 * STEP}" y="0" class="month-lbl">Jul</text>
    <text x="{48 * STEP}" y="0" class="month-lbl">Aug</text>
    <text x="{51 * STEP}" y="0" class="month-lbl" fill="#39d353">Sep</text>
  </g>

  <!-- Day Labels (Mon, Wed, Fri) -->
  <g transform="translate(14, {OFFSET_Y})">
    <text x="0" y="{1 * STEP + 9}" class="day-lbl">Mon</text>
    <text x="0" y="{3 * STEP + 9}" class="day-lbl">Wed</text>
    <text x="0" y="{5 * STEP + 9}" class="day-lbl">Fri</text>
  </g>

  <!-- Grid Cells (53 x 7) -->
  <g transform="translate({OFFSET_X}, {OFFSET_Y})">
'''

    for c in range(COLS):
        for r in range(ROWS):
            cx = c * STEP
            cy = r * STEP
            cell_info = grid.get((r, c), {"level": 0, "count": 0})
            lvl = cell_info.get("level", 0)
            count = cell_info.get("count", 0)

            if lvl == 0:
                fill = "#161b22"
                svg += f'    <rect x="{cx}" y="{cy}" width="{CELL_SIZE}" height="{CELL_SIZE}" rx="2.5" fill="{fill}" />\n'
            else:
                # Active commit cell
                if lvl == 4:
                    fill = "#39d353"
                    glow = 'filter="url(#glow-filter)"'
                elif lvl == 3:
                    fill = "#26a641"
                    glow = ""
                elif lvl == 2:
                    fill = "#006d32"
                    glow = ""
                else:
                    fill = "#0e4429"
                    glow = ""

                # Neon purple / cyan highlights for featured active commits
                if c == 52 and r in (3, 5):
                    fill = "#a855f7"
                    glow = 'filter="url(#glow-filter)"'
                elif c == 48 and r in (0, 5):
                    fill = "#00f0ff"
                    glow = 'filter="url(#glow-filter)"'

                svg += f'''    <rect x="{cx}" y="{cy}" width="{CELL_SIZE}" height="{CELL_SIZE}" rx="2.5" fill="{fill}" {glow}>
      <animate attributeName="opacity" values="0.75; 1; 0.75" dur="{2 + (c % 3)}s" repeatCount="indefinite" />
    </rect>\n'''

    # Snake body trail and multi-segment slithering snake
    svg += f'''  </g>

  <!-- ==================== AUTONOMOUS NEON SNAKE ==================== -->
  <!-- Snake Glowing Body Trail -->
  <path d="{path_d}" fill="none" stroke="url(#snake-body-grad)" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.88" filter="url(#glow-filter)" stroke-dasharray="32 1800">
    <animate attributeName="stroke-dashoffset" values="0; -1800" dur="11s" repeatCount="indefinite" />
  </path>

  <!-- Snake Segment 4 (Tail) -->
  <circle r="3.2" fill="#a855f7" opacity="0.7">
    <animateMotion path="{path_d}" dur="11s" begin="-0.32s" repeatCount="indefinite" rotate="auto" />
  </circle>

  <!-- Snake Segment 3 -->
  <circle r="4" fill="#39d353" opacity="0.85">
    <animateMotion path="{path_d}" dur="11s" begin="-0.22s" repeatCount="indefinite" rotate="auto" />
  </circle>

  <!-- Snake Segment 2 -->
  <circle r="4.8" fill="#00f0ff" opacity="0.95" filter="url(#glow-filter)">
    <animateMotion path="{path_d}" dur="11s" begin="-0.12s" repeatCount="indefinite" rotate="auto" />
  </circle>

  <!-- Snake Head (Glowing Singularity) -->
  <circle r="6" fill="#ffffff" filter="url(#intense-glow)">
    <animateMotion path="{path_d}" dur="11s" begin="0s" repeatCount="indefinite" rotate="auto" />
    <animate attributeName="fill" values="#ffffff;#00f0ff;#39d353;#ffffff" dur="4s" repeatCount="indefinite" />
  </circle>

  <!-- Snake Inner Eye -->
  <circle r="2.2" fill="#0d1117">
    <animateMotion path="{path_d}" dur="11s" begin="0s" repeatCount="indefinite" rotate="auto" />
  </circle>

  <!-- ==================== FOOTER TELEMETRY & CONTROLS ==================== -->
  <g transform="translate(24, {HEIGHT - 14})">
    <text x="0" y="0" class="footer-stat">
      GAME: <tspan fill="#39d353">SNAKE_AI_v2</tspan> | SCORE: <tspan fill="#00f0ff">{total_contribs} PTS</tspan> | SPEED: <tspan fill="#ffa657">60 FPS</tspan> | STATUS: <tspan fill="#a855f7">AUTONOMOUS</tspan>
    </text>

    <!-- Right Side Indicator -->
    <g transform="translate({WIDTH - 48 - 140}, 0)">
      <text x="0" y="0" font-size="9" fill="#7d8590" font-family="monospace">
        LESS <tspan fill="#161b22">■</tspan> <tspan fill="#0e4429">■</tspan> <tspan fill="#006d32">■</tspan> <tspan fill="#26a641">■</tspan> <tspan fill="#39d353">■</tspan> MORE
      </text>
    </g>
  </g>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

    ET.fromstring(svg)
    print(f"[OK] Generated {output_path} ({len(svg)} bytes, valid XML)")
    return output_path


if __name__ == "__main__":
    generate_snake_svg()
