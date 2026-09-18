"""
generate_info_card.py
Generates an animated macOS-style Neofetch terminal card SVG tailored for @exepngsam.
Includes About, Stack, and Highlights with Cyan, Orange, Blue, Green, White & Purple accents.
Features staggered line-by-line slide-up & fade-in SMIL animations (0.06s delay per row).
"""

OUTPUT_FILE = "info-card.svg"

# Structured lines for Neofetch display
LINES_DATA = [
    # (type, label, value, label_color, value_color)
    ("header", "sam", "cyberdeck", "#00f0ff", "#39d353"),
    ("divider", "---------------------------------------------", "", "#30363d", ""),
    ("field", "OS", "CyberDeck OS x86_64 [Linux Kernel 6.12]", "#58a6ff", "#e6edf3"),
    ("field", "Host", "AWS Cloud / Serverless Edge Engine", "#58a6ff", "#e6edf3"),
    ("field", "Role", "AI Systems & Full-Stack Architect", "#ffa657", "#00f0ff"),
    ("field", "Location", "Cyberspace / Dev Hub", "#58a6ff", "#e6edf3"),
    ("blank", "", "", "", ""),
    ("section", "━━━ CORE STACK ━━━━━━━━━━━━━━━━━━━━━━━━━", "", "#ffa657", ""),
    ("field", "Languages", "TypeScript, Python, JavaScript, SQL", "#39d353", "#e6edf3"),
    ("field", "Frameworks", "Next.js 15, React 19, FastAPI, TailwindCSS", "#39d353", "#e6edf3"),
    ("field", "Cloud & AI", "AWS Bedrock, GenAI, CDK, Serverless, Docker", "#39d353", "#e6edf3"),
    ("blank", "", "", "", ""),
    ("section", "━━━ FEATURED PLATFORMS ━━━━━━━━━━━━━━━━━", "", "#bc8cff", ""),
    ("field", "Nexora", "Autonomous AI Incident Coordination", "#bc8cff", "#00f0ff"),
    ("field", "Stark-Ai", "Futuristic Personal AI Operating System", "#bc8cff", "#00f0ff"),
    ("field", "TruthSeal", "Cryptographic Trust & AI Forensics", "#bc8cff", "#00f0ff"),
    ("field", "YieldWay", "Bedrock AgriTech Logistics Engine", "#bc8cff", "#00f0ff"),
    ("field", "Portfolio", "3D Particle Physics Engine Terminal OS", "#bc8cff", "#00f0ff"),
    ("blank", "", "", "", ""),
    ("section", "━━━ TELEMETRY ━━━━━━━━━━━━━━━━━━━━━━━━━━", "", "#00f0ff", ""),
    ("field", "Contributions", "109 Commits in 2026 (Active)", "#00f0ff", "#39d353"),
    ("field", "Architecture", "100% Serverless • Zero-Bloat Code", "#00f0ff", "#e6edf3"),
]

COLOR_SWATCHES = [
    "#161b22", "#ff5f56", "#39d353", "#ffbd2e",
    "#58a6ff", "#bc8cff", "#00f0ff", "#e6edf3"
]


def generate_svg(output_path=OUTPUT_FILE):
    """Generates the macOS terminal Neofetch card SVG with pure SMIL animations (scaled up & enhanced)."""
    card_width = 510
    card_height = 570

    start_x = 28
    start_y = 74
    line_height = 19.8
    stagger_step = 0.06  # 60ms delay between rows as requested
    base_delay = 0.25

    svg_parts = []
    # Header & Styles
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {card_width} {card_height}" width="100%" height="auto" style="max-width: {card_width}px; font-family: -apple-system, BlinkMacSystemFont, 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;">
  <defs>
    <!-- Liquid Glass Background Gradient -->
    <linearGradient id="info-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141d2a" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#0c121a" stop-opacity="0.97" />
      <stop offset="100%" stop-color="#070b10" stop-opacity="0.99" />
    </linearGradient>

    <!-- Glowing Liquid Glass Border Gradient -->
    <linearGradient id="info-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#39d353" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#39d353;#a855f7;#00f0ff;#39d353" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#00f0ff;#39d353;#a855f7;#00f0ff" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Swatch Drop Shadow -->
    <filter id="swatch-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#000000" flood-opacity="0.6" />
    </filter>
  </defs>

  <style>
    .term-title {{ font-size: 13px; fill: #7d8590; font-weight: 700; font-family: monospace; }}
    .hdr-user {{ font-size: 15.5px; font-weight: 900; fill: #00f0ff; letter-spacing: 0.6px; font-family: -apple-system, BlinkMacSystemFont, monospace; }}
    .hdr-host {{ font-size: 15.5px; font-weight: 900; fill: #39d353; letter-spacing: 0.6px; font-family: -apple-system, BlinkMacSystemFont, monospace; }}
    .divider-line {{ font-size: 11px; fill: #30363d; font-family: monospace; }}
    .sec-label {{ font-size: 11px; font-weight: 800; letter-spacing: 1px; font-family: monospace; }}
    .f-key {{ font-size: 13px; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, monospace; }}
    .f-sep {{ font-size: 13px; fill: #7d8590; font-weight: 400; font-family: monospace; }}
    .f-val {{ font-size: 13px; font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, monospace; }}
  </style>

  <!-- Outer Liquid Glass Frame -->
  <rect x="2" y="2" width="{card_width - 4}" height="{card_height - 4}" rx="16" fill="url(#info-bg)" stroke="url(#info-border)" stroke-width="1.8" />

  <!-- Window Header Bar -->
  <g transform="translate(20, 20)">
    <!-- macOS buttons -->
    <circle cx="0" cy="5" r="5" fill="#ff5f56" />
    <circle cx="15" cy="5" r="5" fill="#ffbd2e" />
    <circle cx="30" cy="5" r="5" fill="#27c93f" />

    <!-- Window Title -->
    <text x="48" y="9.5" class="term-title">
      <tspan fill="#00f0ff">sam</tspan>@<tspan fill="#39d353">cyberdeck</tspan>: <tspan fill="#e6edf3">~/neofetch</tspan>
    </text>

    <!-- Right status pill -->
    <rect x="{card_width - 138}" y="-2" width="98" height="18" rx="9" fill="#161b22" stroke="#30363d" stroke-width="1" />
    <text x="{card_width - 124}" y="11" font-size="9.5" fill="#39d353" font-weight="800" font-family="monospace">SYS.ONLINE</text>
  </g>

  <!-- Header Separator -->
  <line x1="16" y1="48" x2="{card_width - 16}" y2="48" stroke="#21262d" stroke-width="1" />

  <!-- Neofetch Content: Staggered Line Reveals -->
  <g id="neofetch-lines">
''')

    cur_y = start_y
    anim_idx = 0

    for item in LINES_DATA:
        itype = item[0]
        if itype == "blank":
            cur_y += 6
            continue

        delay = base_delay + (anim_idx * stagger_step)
        anim_idx += 1

        if itype == "header":
            user, host = item[1], item[2]
            svg_parts.append(f'''    <!-- Line {anim_idx}: Header -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.22s" begin="{delay:.3f}s" fill="freeze" />
      <animateTransform attributeName="transform" type="translate" values="0 6; 0 0" dur="0.22s" begin="{delay:.3f}s" fill="freeze" />
      <text x="{start_x}" y="{cur_y}">
        <tspan class="hdr-user">{user}</tspan><tspan fill="#e6edf3">@</tspan><tspan class="hdr-host">{host}</tspan>
      </text>
    </g>''')

        elif itype == "divider":
            div_text = item[1]
            svg_parts.append(f'''    <!-- Line {anim_idx}: Divider -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.22s" begin="{delay:.3f}s" fill="freeze" />
      <text x="{start_x}" y="{cur_y}" class="divider-line">{div_text}</text>
    </g>''')

        elif itype == "section":
            sec_text = item[1].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            sec_col = item[3]
            svg_parts.append(f'''    <!-- Line {anim_idx}: Section -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.22s" begin="{delay:.3f}s" fill="freeze" />
      <animateTransform attributeName="transform" type="translate" values="0 6; 0 0" dur="0.22s" begin="{delay:.3f}s" fill="freeze" />
      <text x="{start_x}" y="{cur_y}" class="sec-label" fill="{sec_col}">{sec_text}</text>
    </g>''')

        elif itype == "field":
            label = item[1].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            value = item[2].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            l_col, v_col = item[3], item[4]
            svg_parts.append(f'''    <!-- Line {anim_idx}: {label} -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.22s" begin="{delay:.3f}s" fill="freeze" />
      <animateTransform attributeName="transform" type="translate" values="0 6; 0 0" dur="0.22s" begin="{delay:.3f}s" fill="freeze" />
      <text x="{start_x}" y="{cur_y}">
        <tspan class="f-key" fill="{l_col}">{label}</tspan>
        <tspan class="f-sep"> ~ </tspan>
        <tspan class="f-val" fill="{v_col}">{value}</tspan>
      </text>
    </g>''')

        cur_y += line_height

    svg_parts.append('  </g>\n')

    # Color Swatches Palette Bar at Bottom
    swatches_start_delay = base_delay + (anim_idx * stagger_step) + 0.1
    swatch_y = card_height - 34
    swatch_size = 16
    swatch_gap = 8

    svg_parts.append(f'''  <!-- Terminal Color Swatches Palette -->
  <g transform="translate({start_x}, {swatch_y})" filter="url(#swatch-glow)">
''')

    for s_idx, scolor in enumerate(COLOR_SWATCHES):
        sx = s_idx * (swatch_size + swatch_gap)
        s_delay = swatches_start_delay + (s_idx * 0.04)
        svg_parts.append(f'''    <rect x="{sx}" y="0" width="{swatch_size}" height="{swatch_size}" rx="4" fill="{scolor}" opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.2s" begin="{s_delay:.3f}s" fill="freeze" />
      <animateTransform attributeName="transform" type="scale" values="0.3; 1.1; 1" keyTimes="0; 0.7; 1" dur="0.25s" begin="{s_delay:.3f}s" fill="freeze" />
    </rect>''')

    # Status text next to swatches
    text_x = len(COLOR_SWATCHES) * (swatch_size + swatch_gap) + 16
    svg_parts.append(f'''    <text x="{text_x}" y="13" font-size="10.5" fill="#7d8590" font-weight="700" font-family="monospace" opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.3s" begin="{swatches_start_delay + 0.3:.3f}s" fill="freeze" />
      TERM_COLORS [8-BIT]
    </text>
  </g>
</svg>''')

    svg_content = "\n".join(svg_parts)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[SUCCESS] Generated {output_path} ({len(svg_content)} bytes)")
    return output_path


def main():
    print(f"[*] Starting Neofetch Info Card SVG Generation")
    generate_svg(OUTPUT_FILE)


if __name__ == "__main__":
    main()
