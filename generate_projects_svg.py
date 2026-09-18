"""
generate_projects_svg.py
Generates a fully animated, cyberpunk-styled 6-card grid SVG of the Featured Platforms & Systems
for @exepngsam. Features glowing border beams, pulsing live status beacons, tag pills,
and direct clickable links. Pure SMIL SVG.
"""

OUTPUT_FILE = "projects-animated.svg"

PROJECTS = [
    {
        "icon": "🤖",
        "title": "Nexora",
        "subtitle": "Autonomous AI Incident Coordination Platform",
        "desc": "Turns incidents into action with Featherless AI & Caspian for reasoning, autonomous escalation, and real-time coordination.",
        "tags": ["TypeScript", "Featherless AI", "Next.js 15"],
        "demo": "https://nexora-three-mu.vercel.app",
        "repo": "https://github.com/exepngsam/Nexora",
        "accent": "#00f0ff",
        "col": 0, "row": 0
    },
    {
        "icon": "🧠",
        "title": "Stark-Ai",
        "subtitle": "Futuristic Personal AI Operating System",
        "desc": "Converts natural-language into intelligent tool actions, multi-agent automation, and continuous real-time assistance.",
        "tags": ["TypeScript", "Agentic AI", "Automation"],
        "demo": "https://starkai-fawn.vercel.app/",
        "repo": "https://github.com/exepngsam/Stark-Ai",
        "accent": "#a855f7",
        "col": 1, "row": 0
    },
    {
        "icon": "🔐",
        "title": "TruthSeal AI",
        "subtitle": "Digital Trust & Media Forensics Platform",
        "desc": "Combines cryptographic proof, AI media forensics, provenance tracking, and credential revocation for verified media.",
        "tags": ["Cryptographic Trust", "Forensics", "Next.js"],
        "demo": "https://truth-seal-ai.vercel.app",
        "repo": "https://github.com/exepngsam/TruthSeal-AI",
        "accent": "#ffa657",
        "col": 0, "row": 1
    },
    {
        "icon": "🌾",
        "title": "YieldWay AI",
        "subtitle": "Serverless AgriTech Logistics Platform",
        "desc": "Built for 'Bharat Builds' AWS Hackathon with Amazon Bedrock GenAI & AWS CDK to solve agricultural post-harvest logistics loss.",
        "tags": ["AWS Bedrock", "AWS CDK", "Serverless"],
        "demo": "https://frontend-lake-zeta-88.vercel.app",
        "repo": "https://github.com/exepngsam/YieldWay-Ai",
        "accent": "#39d353",
        "col": 1, "row": 1
    },
    {
        "icon": "🏙️",
        "title": "CivicFix AI",
        "subtitle": "AI-Powered Civic Issue Intelligence",
        "desc": "Intelligent civic issue classification, severity detection, automated routing, and real-time AWS resolution workflows.",
        "tags": ["AWS Cloud", "Next.js", "AI Routing"],
        "demo": "https://civicfix-ai-roan.vercel.app",
        "repo": "https://github.com/exepngsam/Civicfix-ai",
        "accent": "#58a6ff",
        "col": 0, "row": 2
    },
    {
        "icon": "✨",
        "title": "Terminal OS & Physics Engine",
        "subtitle": "Brutalist Zero-Bloat Portfolio OS",
        "desc": "Interactive local AI chatbot, an 800-node 3D particle physics simulation, and custom high-speed system architecture.",
        "tags": ["3D Physics", "Zero-Bloat", "Local AI"],
        "demo": "https://portfolio19s.vercel.app/",
        "repo": "https://github.com/exepngsam/Portfolio",
        "accent": "#f43f5e",
        "col": 1, "row": 2
    },
]


def generate_projects_svg(output_path=OUTPUT_FILE):
    width = 880
    height = 560
    card_w = 405
    card_h = 145

    gap_x = 22
    gap_y = 16
    start_x = 24
    start_y = 62

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="max-width: {width}px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="main-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d13" />
      <stop offset="50%" stop-color="#0d1117" />
      <stop offset="100%" stop-color="#141a23" />
    </linearGradient>

    <!-- Outer Border Glow -->
    <linearGradient id="outer-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8">
        <animate attributeName="stop-color" values="#00f0ff;#39d353;#a855f7;#ffa657;#00f0ff" dur="10s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#30363d" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#39d353" stop-opacity="0.7">
        <animate attributeName="stop-color" values="#39d353;#a855f7;#00f0ff;#39d353" dur="10s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Neon Glow Filter -->
    <filter id="p-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="beacon-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .card-title {{ font-size: 14px; font-weight: 700; fill: #e6edf3; letter-spacing: 0.3px; }}
    .card-sub {{ font-size: 11px; font-weight: 600; fill: #7d8590; }}
    .card-desc {{ font-size: 10.5px; fill: #8b949e; line-height: 1.4; }}
    .pill-txt {{ font-size: 9px; font-weight: 600; font-family: monospace; fill: #e6edf3; }}
    .demo-btn-txt {{ font-size: 9.5px; font-weight: 700; font-family: monospace; fill: #00f0ff; }}
    .proj-card {{ transition: transform 0.2s ease; cursor: pointer; }}
  </style>

  <!-- Container Frame -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="14" fill="url(#main-bg)" stroke="url(#outer-glow)" stroke-width="1.6" />

  <!-- Top Title Bar -->
  <g transform="translate(20, 18)">
    <circle cx="0" cy="5" r="4.5" fill="#ff5f56" />
    <circle cx="14" cy="5" r="4.5" fill="#ffbd2e" />
    <circle cx="28" cy="5" r="4.5" fill="#27c93f" />

    <text x="46" y="9" font-size="12" font-weight="700" fill="#e6edf3" font-family="monospace">
      <tspan fill="#00f0ff">~/cyberdeck</tspan>
      <tspan fill="#7d8590"> / </tspan>
      <tspan fill="#39d353">featured-platforms</tspan>
      <tspan fill="#7d8590">.sh</tspan>
    </text>

    <!-- Pulsing Live Badge -->
    <g transform="translate({width - 235}, -1)">
      <rect x="0" y="0" width="185" height="20" rx="10" fill="#161b22" stroke="#30363d" stroke-width="1" />
      <circle cx="12" cy="10" r="3.5" fill="#39d353" filter="url(#beacon-glow)">
        <animate attributeName="r" values="3.5; 5; 3.5" dur="1.8s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="1; 0.3; 1" dur="1.8s" repeatCount="indefinite" />
      </circle>
      <text x="24" y="14" font-size="10" font-weight="700" fill="#00f0ff" font-family="monospace">
        6_PLATFORMS // ACTIVE
      </text>
    </g>
  </g>

  <!-- Header line -->
  <line x1="16" y1="46" x2="{width - 16}" y2="46" stroke="#21262d" stroke-width="1" />

  <!-- Project Cards Grid -->
'''

    for i, p in enumerate(PROJECTS):
        cx = start_x + p["col"] * (card_w + gap_x)
        cy = start_y + p["row"] * (card_h + gap_y)
        delay = 0.15 + (i * 0.08)
        accent = p["accent"]

        # Truncate description into 2 neat lines
        desc_line1 = p["desc"][:56].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        desc_line2 = p["desc"][56:115].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        subtitle = p["subtitle"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        title = p["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        svg += f'''  <!-- Card {i + 1}: {title} -->
  <g transform="translate({cx}, {cy})" class="proj-card">
    <animate attributeName="opacity" values="0; 1" dur="0.3s" begin="{delay:.2f}s" fill="freeze" />
    <animateTransform attributeName="transform" type="translate" values="{cx} {cy + 10}; {cx} {cy}" dur="0.3s" begin="{delay:.2f}s" fill="freeze" />

    <!-- Card Base Box -->
    <rect x="0" y="0" width="{card_w}" height="{card_h}" rx="10" fill="#111620" stroke="#30363d" stroke-width="1.2" />

    <!-- Animated Running Accent Border Beam -->
    <rect x="0" y="0" width="{card_w}" height="{card_h}" rx="10" fill="none" stroke="{accent}" stroke-width="1.8" stroke-dasharray="70 420" opacity="0.85">
      <animate attributeName="stroke-dashoffset" values="0; -980" dur="{4 + (i * 0.5):.1f}s" repeatCount="indefinite" />
    </rect>

    <!-- Top Row: Icon + Title + Live Beacon -->
    <a href="{p["demo"]}" target="_blank">
      <text x="14" y="24" font-size="16">{p["icon"]}</text>
      <text x="38" y="24" class="card-title">{title}</text>
    </a>

    <!-- Live Status Pill in Card Header -->
    <g transform="translate({card_w - 95}, 10)">
      <rect x="0" y="0" width="80" height="18" rx="9" fill="#161b22" stroke="{accent}" stroke-width="0.8" />
      <circle cx="9" cy="9" r="2.8" fill="{accent}">
        <animate attributeName="opacity" values="1; 0.2; 1" dur="1.5s" repeatCount="indefinite" />
      </circle>
      <text x="18" y="12.5" font-size="8.5" font-weight="700" fill="{accent}" font-family="monospace">LIVE DEMO</text>
    </g>

    <!-- Subtitle -->
    <text x="14" y="44" class="card-sub">{subtitle}</text>

    <!-- Description Lines -->
    <text x="14" y="64" class="card-desc">{desc_line1}</text>
    <text x="14" y="80" class="card-desc">{desc_line2}...</text>

    <!-- Bottom Row: Tech Tag Pills -->
    <g transform="translate(14, 104)">
'''
        tag_x = 0
        for tag in p["tags"]:
            tag_escaped = tag.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            tag_w = len(tag) * 6.6 + 14
            svg += f'''      <rect x="{tag_x}" y="0" width="{tag_w}" height="18" rx="4" fill="#1c2128" stroke="#30363d" stroke-width="0.8" />
      <text x="{tag_x + 7}" y="12" class="pill-txt">{tag_escaped}</text>
'''
            tag_x += tag_w + 6

        # Link button on right
        btn_x = card_w - 95
        svg += f'''      <a href="{p["demo"]}" target="_blank">
        <rect x="{btn_x - 14}" y="0" width="80" height="18" rx="4" fill="{accent}" fill-opacity="0.15" stroke="{accent}" stroke-width="0.9" />
        <text x="{btn_x - 4}" y="12" class="demo-btn-txt">VISIT ➔</text>
      </a>
    </g>
  </g>
'''

    svg += '''</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[OK] Generated {output_path}")
    return output_path


if __name__ == "__main__":
    generate_projects_svg()
