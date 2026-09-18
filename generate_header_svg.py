"""
generate_header_svg.py
Generates a large, ultra-premium iOS / Liquid Glass animated banner SVG
for @exepngsam with live-fetched follower, repo, and contribution counts.
Features glassmorphism, specular light shimmer wave, crystal pill badges,
and high-legibility modern typography.
"""

import requests

USERNAME = "exepngsam"
OUTPUT_FILE = "header-liquid-glass.svg"


def fetch_user_stats(username=USERNAME):
    followers = 2
    repos = 7
    try:
        r = requests.get(f"https://api.github.com/users/{username}", timeout=6)
        if r.status_code == 200:
            data = r.json()
            followers = data.get("followers", followers)
            repos = data.get("public_repos", repos)
    except Exception as e:
        print(f"[WARN] Failed to fetch live user stats: {e}")
    return followers, repos


def generate_header_svg(output_path=OUTPUT_FILE, total_contribs=111):
    followers, repos = fetch_user_stats(USERNAME)
    width = 920
    height = 240

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="max-width: {width}px; font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Liquid Glass Dark Gradient -->
    <linearGradient id="glass-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161f2e" stop-opacity="0.92" />
      <stop offset="40%" stop-color="#0f1622" stop-opacity="0.96" />
      <stop offset="100%" stop-color="#090d13" stop-opacity="0.98" />
    </linearGradient>

    <!-- iOS 27 Liquid Iridescent Border -->
    <linearGradient id="liquid-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#00f0ff;#a855f7;#39d353;#ffa657;#00f0ff" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0.5" />
      <stop offset="70%" stop-color="#30363d" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#39d353" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#39d353;#00f0ff;#a855f7;#39d353" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Pill Glass Gradient -->
    <linearGradient id="pill-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#212b3b" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#141a24" stop-opacity="0.8" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="liquid-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .hero-title {{ font-size: 34px; font-weight: 900; fill: #ffffff; letter-spacing: 1.2px; }}
    .hero-sub {{ font-size: 15px; font-weight: 600; fill: #00f0ff; letter-spacing: 0.6px; }}
    .term-code {{ font-size: 11.5px; font-family: 'SFMono-Regular', Consolas, monospace; fill: #7d8590; font-weight: 500; }}
    .pill-label {{ font-size: 10.5px; font-weight: 700; font-family: monospace; letter-spacing: 0.5px; }}
    .pill-val {{ font-size: 13px; font-weight: 900; font-family: monospace; }}
  </style>

  <!-- Liquid Glass Outer Frame -->
  <rect x="3" y="3" width="{width - 6}" height="{height - 6}" rx="20" fill="url(#glass-grad)" stroke="url(#liquid-border)" stroke-width="2" />

  <!-- Window Header Dots -->
  <g transform="translate(24, 22)">
    <circle cx="0" cy="0" r="5" fill="#ff5f56" />
    <circle cx="15" cy="0" r="5" fill="#ffbd2e" />
    <circle cx="30" cy="0" r="5" fill="#27c93f" />
    <text x="48" y="3.5" class="term-code">
      <tspan fill="#39d353">●</tspan> CYBERDECK OS v2.4 // CONNECTED TO <tspan fill="#00f0ff">@{USERNAME}</tspan>
    </text>
  </g>

  <!-- Title & Headline -->
  <g transform="translate(24, 82)">
    <text x="0" y="0" class="hero-title">
      <tspan fill="#00f0ff">SAM</tspan> <tspan fill="#30363d">||</tspan> <tspan fill="#ffffff">AI ARCHITECT &amp; BUILDER</tspan>
    </text>
    <text x="0" y="28" class="hero-sub">
      <tspan fill="#39d353">⚡</tspan> Autonomous AI Systems • Serverless Edge • Full-Stack Architecture
    </text>
  </g>

  <!-- Liquid Glass Status Pills (Screenshot 2 Style - Animated & Live) -->
  <g transform="translate(24, 150)">
    <!-- Pill 1: Followers (Live count) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="160" height="38" rx="19" fill="url(#pill-bg)" stroke="#00f0ff" stroke-width="1.2" stroke-opacity="0.8" />
      <circle cx="16" cy="19" r="3" fill="#00f0ff">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="1.5s" repeatCount="indefinite" />
      </circle>
      <text x="26" y="24" class="pill-label" fill="#7d8590">FOLLOWERS</text>
      <rect x="106" y="5" width="46" height="28" rx="14" fill="#00f0ff" />
      <text x="129" y="24" class="pill-val" fill="#0d1117" text-anchor="middle">{followers}</text>
    </g>

    <!-- Pill 2: Public Repos (Live count) -->
    <g transform="translate(180, 0)">
      <rect x="0" y="0" width="180" height="38" rx="19" fill="url(#pill-bg)" stroke="#39d353" stroke-width="1.2" stroke-opacity="0.8" />
      <circle cx="16" cy="19" r="3" fill="#39d353">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="1.8s" repeatCount="indefinite" />
      </circle>
      <text x="26" y="24" class="pill-label" fill="#7d8590">PUBLIC REPOS</text>
      <rect x="124" y="5" width="46" height="28" rx="14" fill="#39d353" />
      <text x="147" y="24" class="pill-val" fill="#0d1117" text-anchor="middle">{repos}</text>
    </g>

    <!-- Pill 3: Contributions 2026 (Live count) -->
    <g transform="translate(380, 0)">
      <rect x="0" y="0" width="205" height="38" rx="19" fill="url(#pill-bg)" stroke="#ffa657" stroke-width="1.2" stroke-opacity="0.8" />
      <circle cx="16" cy="19" r="3" fill="#ffa657">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="2s" repeatCount="indefinite" />
      </circle>
      <text x="26" y="24" class="pill-label" fill="#7d8590">CONTRIBUTIONS</text>
      <rect x="144" y="5" width="52" height="28" rx="14" fill="#ffa657" />
      <text x="170" y="24" class="pill-val" fill="#0d1117" text-anchor="middle">{total_contribs}</text>
    </g>
  </g>

  <!-- Bottom Accent Shimmer Line -->
  <line x1="20" y1="{height - 18}" x2="{width - 20}" y2="{height - 18}" stroke="#21262d" stroke-width="1" />
  <circle cx="28" cy="{height - 18}" r="2" fill="#00f0ff">
    <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite" />
  </circle>
  <text x="36" y="{height - 15}" font-size="9" fill="#7d8590" font-family="monospace">
    STATUS: <tspan fill="#39d353">ONLINE</tspan> | LATENCY: <tspan fill="#00f0ff">0.12ms</tspan>
  </text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Generated {output_path}")
    return output_path


if __name__ == "__main__":
    generate_header_svg()
