"""
generate_stats_svg.py
Generates an animated, ultra-crisp Liquid Glass / iOS 27 GitHub Stats & Telemetry SVG
for @exepngsam. Solves the broken third-party image issue permanently with 100%
self-contained SMIL animations, glowing streak flames, and activity waveform.
"""

OUTPUT_FILE = "github-stats-animated.svg"


def generate_stats_svg(output_path=OUTPUT_FILE):
    width = 920
    height = 300

    # Path for glowing activity wave
    wave_path = "M 490 200 C 530 140, 560 210, 600 170 C 640 130, 670 190, 710 150 C 750 110, 780 180, 820 130 C 850 90, 875 140, 895 100"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="max-width: {width}px; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Liquid Glass Card Background -->
    <linearGradient id="stats-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141c29" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#0f1622" stop-opacity="0.96" />
      <stop offset="100%" stop-color="#080c12" stop-opacity="0.98" />
    </linearGradient>

    <!-- Liquid Glass Border Gradient -->
    <linearGradient id="stats-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.85">
        <animate attributeName="stop-color" values="#00f0ff;#39d353;#a855f7;#00f0ff" dur="9s" repeatCount="indefinite" />
      </stop>
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#39d353" stop-opacity="0.85">
        <animate attributeName="stop-color" values="#39d353;#a855f7;#00f0ff;#39d353" dur="9s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Inner Glass Block Background -->
    <linearGradient id="block-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1c2636" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#101722" stop-opacity="0.85" />
    </linearGradient>

    <!-- Glowing Wave Gradient -->
    <linearGradient id="wave-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f0ff" />
      <stop offset="50%" stop-color="#39d353" />
      <stop offset="100%" stop-color="#a855f7" />
    </linearGradient>

    <!-- Flame Glow Filter -->
    <filter id="flame-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="3.5" result="b1" />
      <feMerge>
        <feMergeNode in="b1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="wave-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b2" />
      <feMerge>
        <feMergeNode in="b2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .sec-title {{ font-size: 13px; font-weight: 700; fill: #00f0ff; letter-spacing: 0.8px; font-family: monospace; }}
    .metric-big {{ font-size: 32px; font-weight: 900; fill: #ffffff; letter-spacing: 0.5px; font-family: -apple-system, BlinkMacSystemFont, monospace; }}
    .metric-lbl {{ font-size: 11px; font-weight: 600; fill: #7d8590; letter-spacing: 0.5px; }}
    .sub-lbl {{ font-size: 10px; fill: #58a6ff; font-weight: 500; font-family: monospace; }}
    .lang-name {{ font-size: 11px; font-weight: 700; fill: #e6edf3; font-family: monospace; }}
    .lang-pct {{ font-size: 11px; font-weight: 800; font-family: monospace; }}
  </style>

  <!-- Outer Liquid Glass Frame -->
  <rect x="3" y="3" width="{width - 6}" height="{height - 6}" rx="18" fill="url(#stats-bg)" stroke="url(#stats-border)" stroke-width="1.8" />

  <!-- Top Title Bar -->
  <g transform="translate(24, 20)">
    <circle cx="0" cy="5" r="4.5" fill="#ff5f56" />
    <circle cx="14" cy="5" r="4.5" fill="#ffbd2e" />
    <circle cx="28" cy="5" r="4.5" fill="#27c93f" />
    <text x="46" y="9" font-size="12" font-weight="700" fill="#e6edf3" font-family="monospace">
      <tspan fill="#00f0ff">~/telemetry</tspan>
      <tspan fill="#7d8590"> / </tspan>
      <tspan fill="#39d353">github-stats-matrix</tspan>
      <tspan fill="#7d8590">.live</tspan>
    </text>

    <!-- Pulsing Live Telemetry Badge -->
    <g transform="translate({width - 245}, 0)">
      <rect x="0" y="-2" width="195" height="22" rx="11" fill="#161b22" stroke="#30363d" stroke-width="1" />
      <circle cx="12" cy="9" r="3.5" fill="#39d353">
        <animate attributeName="r" values="3.5; 5; 3.5" dur="1.8s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="1; 0.3; 1" dur="1.8s" repeatCount="indefinite" />
      </circle>
      <text x="24" y="13" font-size="9.5" font-weight="700" fill="#00f0ff" font-family="monospace">
        REALTIME // TELEMETRY
      </text>
    </g>
  </g>

  <!-- Header Divider -->
  <line x1="16" y1="46" x2="{width - 16}" y2="46" stroke="#21262d" stroke-width="1" />

  <!-- Left Stats Grid: 3 Glass Blocks -->
  <g transform="translate(24, 62)">
    <!-- Block 1: Total Contributions -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="135" height="105" rx="14" fill="url(#block-bg)" stroke="#30363d" stroke-width="1.2" />
      <rect x="0" y="0" width="135" height="105" rx="14" fill="none" stroke="#ffa657" stroke-width="1" stroke-opacity="0.4" />
      <text x="16" y="24" class="metric-lbl">TOTAL PUSHES</text>
      <text x="16" y="62" class="metric-big" fill="#ffffff">110</text>
      <text x="16" y="86" class="sub-lbl" fill="#ffa657">▲ 2026 ACTIVE</text>
    </g>

    <!-- Block 2: Current Streak (with flame animation) -->
    <g transform="translate(150, 0)">
      <rect x="0" y="0" width="145" height="105" rx="14" fill="url(#block-bg)" stroke="#39d353" stroke-width="1.4" stroke-opacity="0.6" />
      <!-- Pulsing circle badge -->
      <circle cx="116" cy="24" r="14" fill="#39d353" fill-opacity="0.18" stroke="#39d353" stroke-width="1.2" />
      <text x="116" y="29" font-size="14" text-anchor="middle" filter="url(#flame-glow)">🔥</text>
      <text x="16" y="24" class="metric-lbl">CURRENT STREAK</text>
      <text x="16" y="62" class="metric-big" fill="#39d353">4 <tspan font-size="16" fill="#7d8590">DAYS</tspan></text>
      <text x="16" y="86" class="sub-lbl" fill="#39d353">LONGEST: 4 DAYS</text>
    </g>

    <!-- Block 3: Public Repos & Architecture -->
    <g transform="translate(310, 0)">
      <rect x="0" y="0" width="135" height="105" rx="14" fill="url(#block-bg)" stroke="#30363d" stroke-width="1.2" />
      <rect x="0" y="0" width="135" height="105" rx="14" fill="none" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.4" />
      <text x="16" y="24" class="metric-lbl">PUBLIC REPOS</text>
      <text x="16" y="62" class="metric-big" fill="#00f0ff">7</text>
      <text x="16" y="86" class="sub-lbl" fill="#00f0ff">GRADE: A+ [OPTIMAL]</text>
    </g>
  </g>

  <!-- Left Bottom: Language Breakdown Bars -->
  <g transform="translate(24, 185)">
    <!-- TypeScript -->
    <g transform="translate(0, 0)">
      <text x="0" y="12" class="lang-name">TypeScript</text>
      <text x="445" y="12" class="lang-pct" fill="#00f0ff" text-anchor="end">58%</text>
      <rect x="0" y="20" width="445" height="8" rx="4" fill="#161b22" />
      <rect x="0" y="20" width="0" height="8" rx="4" fill="#00f0ff">
        <animate attributeName="width" values="0; 258" dur="1.2s" fill="freeze" />
      </rect>
    </g>

    <!-- Python -->
    <g transform="translate(0, 36)">
      <text x="0" y="12" class="lang-name">Python</text>
      <text x="445" y="12" class="lang-pct" fill="#39d353" text-anchor="end">26%</text>
      <rect x="0" y="20" width="445" height="8" rx="4" fill="#161b22" />
      <rect x="0" y="20" width="0" height="8" rx="4" fill="#39d353">
        <animate attributeName="width" values="0; 115" dur="1.2s" fill="freeze" />
      </rect>
    </g>

    <!-- Web / React / Tailwind -->
    <g transform="translate(0, 72)">
      <text x="0" y="12" class="lang-name">Next.js • TailwindCSS • React</text>
      <text x="445" y="12" class="lang-pct" fill="#a855f7" text-anchor="end">16%</text>
      <rect x="0" y="20" width="445" height="8" rx="4" fill="#161b22" />
      <rect x="0" y="20" width="0" height="8" rx="4" fill="#a855f7">
        <animate attributeName="width" values="0; 72" dur="1.2s" fill="freeze" />
      </rect>
    </g>
  </g>

  <!-- Vertical Divider -->
  <line x1="475" y1="56" x2="475" y2="{height - 20}" stroke="#21262d" stroke-width="1" />

  <!-- Right Side: Animated Activity Waveform Graph -->
  <g transform="translate(490, 62)">
    <!-- Header -->
    <text x="0" y="18" class="sec-title">CONTRIBUTION VELOCITY &amp; ACTIVITY PULSE</text>
    <text x="0" y="36" font-size="11" fill="#7d8590">Real-time commit telemetry across active cycles</text>

    <!-- Activity Waveform Box -->
    <rect x="0" y="50" width="395" height="155" rx="14" fill="url(#block-bg)" stroke="#30363d" stroke-width="1.2" />

    <!-- Grid lines inside wave box -->
    <line x1="20" y1="90" x2="375" y2="90" stroke="#21262d" stroke-width="0.8" stroke-dasharray="4 4" />
    <line x1="20" y1="130" x2="375" y2="130" stroke="#21262d" stroke-width="0.8" stroke-dasharray="4 4" />
    <line x1="20" y1="170" x2="375" y2="170" stroke="#21262d" stroke-width="0.8" stroke-dasharray="4 4" />

    <!-- Waveform Path -->
    <path d="M 20 160 C 60 110, 90 170, 130 130 C 170 90, 200 150, 240 110 C 280 70, 310 140, 350 90 L 375 120" fill="none" stroke="url(#wave-grad)" stroke-width="3" stroke-linecap="round" filter="url(#wave-glow)">
      <animate attributeName="stroke-dasharray" values="0 500; 500 0" dur="2s" fill="freeze" />
    </path>

    <!-- Traveling Glowing Laser Beacon along wave -->
    <circle r="4.5" fill="#ffffff" filter="url(#flame-glow)">
      <animateMotion path="M 20 160 C 60 110, 90 170, 130 130 C 170 90, 200 150, 240 110 C 280 70, 310 140, 350 90 L 375 120" dur="4s" repeatCount="indefinite" />
    </circle>

    <!-- Key Metrics Badges at Bottom of Wave -->
    <g transform="translate(15, 175)">
      <text x="0" y="16" font-size="9.5" font-family="monospace" fill="#7d8590">
        PEAK: <tspan fill="#39d353">25 COMMITS/DAY</tspan> | VELOCITY: <tspan fill="#00f0ff">HIGH</tspan> | HEALTH: <tspan fill="#a855f7">100%</tspan>
      </text>
    </g>
  </g>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Generated {output_path}")
    return output_path


if __name__ == "__main__":
    generate_stats_svg()
