"""
generate_snake_svg.py
Generates an animated SVG of a cyberpunk snake eating contribution squares
across the GitHub contribution calendar for @exepngsam.
Pure SMIL / CSS vector animation, completely self-contained.
"""

import requests
import re

USERNAME = "exepngsam"
OUTPUT_FILE = "github-contribution-grid-snake.svg"

# Cell parameters
COLS = 53
ROWS = 7
CELL_SIZE = 11
GAP = 4
STEP = CELL_SIZE + GAP

WIDTH = COLS * STEP + 60
HEIGHT = ROWS * STEP + 70

# Fallback active cells (row, col)
ACTIVE_CELLS = [
    (0, 48), (1, 40), (1, 50), (1, 51), (2, 48), (2, 50),
    (2, 51), (2, 52), (3, 51), (3, 52), (4, 52), (5, 48),
    (5, 52), (6, 47), (6, 48)
]


def generate_snake_svg(output_path=OUTPUT_FILE):
    # Base path for the snake moving across the grid
    # Snake path coordinates
    # Let the snake start at col 38 row 1, slither through active cluster (cols 40-52), eating dots
    points = [
        (38 * STEP + 30, 1 * STEP + 35),
        (40 * STEP + 30, 1 * STEP + 35),
        (40 * STEP + 30, 3 * STEP + 35),
        (47 * STEP + 30, 3 * STEP + 35),
        (47 * STEP + 30, 6 * STEP + 35),
        (48 * STEP + 30, 6 * STEP + 35),
        (48 * STEP + 30, 0 * STEP + 35),
        (50 * STEP + 30, 0 * STEP + 35),
        (50 * STEP + 30, 2 * STEP + 35),
        (51 * STEP + 30, 2 * STEP + 35),
        (51 * STEP + 30, 3 * STEP + 35),
        (52 * STEP + 30, 3 * STEP + 35),
        (52 * STEP + 30, 5 * STEP + 35),
        (52 * STEP + 30, 1 * STEP + 35),
    ]

    path_d = f"M {points[0][0]} {points[0][1]} " + " ".join([f"L {p[0]} {p[1]}" for p in points[1:]])

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="auto" style="max-width: {WIDTH}px; background: #0d1117; border-radius: 12px; border: 1px solid #30363d; font-family: monospace;">
  <defs>
    <!-- Snake Glow Filter -->
    <filter id="snake-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <linearGradient id="snake-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f0ff" />
      <stop offset="50%" stop-color="#39d353" />
      <stop offset="100%" stop-color="#a855f7" />
    </linearGradient>
  </defs>

  <!-- Title Bar -->
  <g transform="translate(16, 18)">
    <circle cx="0" cy="0" r="4" fill="#ff5f56" />
    <circle cx="12" cy="0" r="4" fill="#ffbd2e" />
    <circle cx="24" cy="0" r="4" fill="#27c93f" />
    <text x="36" y="3.5" font-size="10.5" fill="#7d8590" font-weight="600">
      <tspan fill="#00f0ff">snake@cyberdeck</tspan>: <tspan fill="#39d353">contributions.eat()</tspan> ~ <tspan fill="#e6edf3">109 dots consumed</tspan>
    </text>
  </g>

  <!-- Grid Cells -->
  <g transform="translate(30, 35)">
'''

    # Render base grid
    for c in range(COLS):
        for r in range(ROWS):
            cx = c * STEP
            cy = r * STEP
            is_active = (r, c) in ACTIVE_CELLS
            fill = "#161b22"
            if is_active:
                if c == 52 and r == 3:
                    fill = "#a855f7"
                elif c == 48 and r == 5:
                    fill = "#39d353"
                elif c >= 50:
                    fill = "#26a641"
                else:
                    fill = "#006d32"

            svg += f'    <rect x="{cx}" y="{cy}" width="{CELL_SIZE}" height="{CELL_SIZE}" rx="2" fill="{fill}" />\n'

    # Animated Snake path and head
    svg += f'''  </g>

  <!-- Snake Body Motion Path -->
  <path id="snake-trail" d="{path_d}" fill="none" stroke="url(#snake-grad)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity="0.85" filter="url(#snake-glow)" stroke-dasharray="24 1600">
    <animate attributeName="stroke-dashoffset" values="0; -1600" dur="9s" repeatCount="indefinite" />
  </path>

  <!-- Snake Head -->
  <circle r="5" fill="#00f0ff" filter="url(#snake-glow)">
    <animateMotion path="{path_d}" dur="9s" repeatCount="indefinite" rotate="auto" />
    <animate attributeName="fill" values="#00f0ff;#39d353;#a855f7;#00f0ff" dur="4.5s" repeatCount="indefinite" />
  </circle>

  <!-- Snake Tongue / Eyes Accent -->
  <circle r="2.5" fill="#ffffff">
    <animateMotion path="{path_d}" dur="9s" repeatCount="indefinite" rotate="auto" />
  </circle>

  <!-- Footer status -->
  <g transform="translate(30, {HEIGHT - 12})">
    <text x="0" y="0" font-size="9" fill="#7d8590">
      GAME: <tspan fill="#39d353">SNAKE_AI_v2</tspan> | SCORE: <tspan fill="#00f0ff">109 PTS</tspan> | SPEED: <tspan fill="#ffa657">60 FPS</tspan> | STATUS: <tspan fill="#a855f7">AUTONOMOUS</tspan>
    </text>
  </g>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Generated {output_path}")
    return output_path


if __name__ == "__main__":
    generate_snake_svg()
