"""
generate_snake_svg.py
Generates an ultra-premium CyberDeck Contribution Snake Game SVG for @exepngsam with:
- Authentic smooth cell-by-cell slithering snake (connected body segments s0-s3)
- Smooth keyframe transition animations for snake pathing and dot consumption
- Dynamic real-time GitHub contribution score & live dots consumed counter
- Neon cyberpunk palette (Head: glowing cyan, Body: bright cyan/emerald, Tail: purple)
- Obsidian glass container with animated liquid border and HUD brackets (Zero specular glare)
- Perfectly centered 53x7 grid with month and day headers
- Width: 920px (matching header banner, terminal card, and streak card)
"""

import os
import re
import requests
import xml.etree.ElementTree as ET
import generate_contribution_svg

USERNAME = "exepngsam"
OUTPUT_FILE = "github-contribution-grid-snake.svg"

WIDTH = 920
HEIGHT = 240
GRID_X = 36
GRID_Y = 48


def fetch_platane_svg():
    """Fetches the authentic Platane snake SVG from the remote output branch or local fallback."""
    url = f"https://raw.githubusercontent.com/{USERNAME}/{USERNAME}/output/github-contribution-grid-snake-dark.svg"
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200 and len(r.text) > 1000:
            print(f"[OK] Fetched live Platane snake SVG from output branch ({len(r.text)} bytes)")
            return r.text
    except Exception as e:
        print(f"[WARN] Failed to fetch remote Platane SVG: {e}")

    for local_f in ["platane_snake_dark.svg", "platane_snake.svg"]:
        if os.path.exists(local_f):
            print(f"[OK] Loaded local Platane SVG: {local_f}")
            with open(local_f, "r", encoding="utf-8") as f:
                return f.read()
    return None


def generate_snake_svg(output_path=OUTPUT_FILE, grid=None, total_contribs=None, months=None):
    if total_contribs is None:
        grid, total_contribs, months = generate_contribution_svg.fetch_contributions(USERNAME)

    platane_raw = fetch_platane_svg()
    if not platane_raw:
        raise RuntimeError("Could not retrieve Platane snake SVG data")

    # Extract CSS from Platane SVG
    style_match = re.search(r"<style>(.*?)</style>", platane_raw, re.DOTALL)
    platane_css = style_match.group(1) if style_match else ""

    # Extract all rect elements
    rects = re.findall(r"<rect [^>]+/>", platane_raw)
    cells = [r for r in rects if 'class="c' in r]
    # Seamless, connected snake segments (virtually zero gap, eliminating disjointed block separation)
    snake_rects = [
        '<rect class="s s0" x="0.2" y="0.2" width="15.6" height="15.6" rx="4.6" ry="4.6"/>',
        '<rect class="s s1" x="0.3" y="0.3" width="15.4" height="15.4" rx="4.2" ry="4.2"/>',
        '<rect class="s s2" x="0.4" y="0.4" width="15.2" height="15.2" rx="3.9" ry="3.9"/>',
        '<rect class="s s3" x="0.5" y="0.5" width="15.0" height="15.0" rx="3.6" ry="3.6"/>',
    ]
    progress_rects = [r for r in rects if 'class="u' in r]

    # CyberDeck theme styling overrides with unified, fluid neon gradient (Zero per-frame drop-shadow lag)
    cyberdeck_css_overrides = """
      :root {
        --cb: rgba(48, 54, 61, 0.4);
        --cs: #00f0ff;
        --ce: #161b22;
        --c0: #161b22;
        --c1: #0e4429;
        --c2: #006d32;
        --c3: #26a641;
        --c4: #39d353;
      }
      .c {
        shape-rendering: geometricPrecision;
        fill: var(--ce);
        stroke-width: 0.8px;
        stroke: var(--cb);
        animation: none 14700ms linear infinite;
        width: 12px;
        height: 12px;
        rx: 2.5px;
        ry: 2.5px;
      }
      .u {
        transform-origin: 0 0;
        transform: scale(0, 1);
        animation: none linear 14700ms infinite;
        rx: 3px;
        ry: 3px;
      }
      .s {
        shape-rendering: geometricPrecision;
        animation: none linear 14700ms infinite;
      }
      .s.s0 {
        fill: #00f0ff;
        stroke: #ffffff;
        stroke-width: 0.8px;
        stroke-opacity: 0.85;
      }
      .s.s1 {
        fill: #00e5ff;
        stroke: #00f0ff;
        stroke-width: 0.5px;
        stroke-opacity: 0.5;
      }
      .s.s2 {
        fill: #00dfa2;
        stroke: #00e5ff;
        stroke-width: 0.5px;
        stroke-opacity: 0.5;
      }
      .s.s3 {
        fill: #39d353;
        stroke: #00dfa2;
        stroke-width: 0.5px;
        stroke-opacity: 0.5;
      }
      .game-title { font-size: 11.5px; font-weight: 700; fill: #7d8590; font-family: monospace; }
      .month-lbl { font-size: 9px; fill: #58a6ff; font-weight: 600; font-family: monospace; }
      .day-lbl { font-size: 8.5px; fill: #7d8590; font-family: monospace; font-weight: 600; }
      .footer-stat { font-size: 9.5px; font-weight: 700; fill: #7d8590; font-family: monospace; }
    """

    full_css = platane_css + cyberdeck_css_overrides

    cells_svg = "\n    ".join(cells)
    progress_svg = "\n    ".join(progress_rects)
    snake_svg = "\n    ".join(snake_rects)

    # 13 month markers along 53 columns
    months_data = [
        ("Sep", 0), ("Oct", 4), ("Nov", 9), ("Dec", 13),
        ("Jan", 18), ("Feb", 22), ("Mar", 26), ("Apr", 31),
        ("May", 35), ("Jun", 40), ("Jul", 44), ("Aug", 48),
        ("Sep", 51)
    ]
    months_svg_lines = []
    for name, col in months_data:
        fill_attr = ' fill="#39d353"' if name == "Sep" and col == 51 else ''
        months_svg_lines.append(f'<text x="{col * 16}" y="0" class="month-lbl"{fill_attr}>{name}</text>')
    months_svg = "\n    ".join(months_svg_lines)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="auto" style="max-width: {WIDTH}px; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SFMono-Regular', Consolas, monospace;">
  <defs>
    <!-- Dark Obsidian Glass Background -->
    <linearGradient id="snake-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141c28" stop-opacity="0.96" />
      <stop offset="50%" stop-color="#0e141e" stop-opacity="0.98" />
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

    <!-- Ultra-Smooth Hardware-Accelerated Glow Filter (Pure 60 FPS, Zero Jitter) -->
    <filter id="smooth-snake-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1.6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
{full_css}
  </style>

  <!-- Outer Liquid Glass Frame (Pure Clean Aesthetics, Zero Specular Glare) -->
  <rect x="3" y="3" width="{WIDTH - 6}" height="{HEIGHT - 6}" rx="18" fill="url(#snake-card-bg)" stroke="url(#snake-border)" stroke-width="1.8" />

  <!-- Corner HUD Sci-Fi Brackets on Game Board -->
  <path d="M 26 42 L 20 42 L 20 50" fill="none" stroke="#00f0ff" stroke-width="1.5" opacity="0.8" />
  <path d="M {WIDTH - 26} 42 L {WIDTH - 20} 42 L {WIDTH - 20} 50" fill="none" stroke="#00f0ff" stroke-width="1.5" opacity="0.8" />
  <path d="M 26 {HEIGHT - 28} L 20 {HEIGHT - 28} L 20 {HEIGHT - 36}" fill="none" stroke="#39d353" stroke-width="1.5" opacity="0.8" />
  <path d="M {WIDTH - 26} {HEIGHT - 28} L {WIDTH - 20} {HEIGHT - 28} L {WIDTH - 20} {HEIGHT - 36}" fill="none" stroke="#39d353" stroke-width="1.5" opacity="0.8" />

  <!-- ==================== TOP TITLE BAR ==================== -->
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
  <g transform="translate({GRID_X + 2}, 38)">
    {months_svg}
  </g>

  <!-- Day Labels (Mon, Wed, Fri) -->
  <g transform="translate(14, {GRID_Y + 2})">
    <text x="0" y="{1 * 16 + 9}" class="day-lbl">Mon</text>
    <text x="0" y="{3 * 16 + 9}" class="day-lbl">Wed</text>
    <text x="0" y="{5 * 16 + 9}" class="day-lbl">Fri</text>
  </g>

  <!-- ==================== PLATANE CONTRIBUTION GRID & SMOOTH SNAKE ==================== -->
  <g transform="translate({GRID_X}, {GRID_Y})">
    <!-- Base Contribution Grid Cells -->
    {cells_svg}

    <!-- Progress Track Background -->
    <rect x="0" y="144" width="848" height="12" rx="3" ry="3" fill="#161b22" stroke="#30363d" stroke-width="0.8" opacity="0.6" />

    <!-- Progress Score Expansion Segments -->
    {progress_svg}

    <!-- Smooth Slithering Snake Segments (Seamless Connected Serpent with Hardware-Accelerated Bloom) -->
    <g filter="url(#smooth-snake-glow)">
      {snake_svg}
    </g>
  </g>

  <!-- ==================== FOOTER TELEMETRY & CONTROLS ==================== -->
  <g transform="translate(24, {HEIGHT - 12})">
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
