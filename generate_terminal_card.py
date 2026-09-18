"""
generate_terminal_card.py
Generates an ultra-premium, fully animated Cyberpunk & Liquid Glass Terminal Card SVG.
Features:
- Animated matrix digital rain & floating binary code streams in the background
- Clean, high-contrast ASCII art portrait without noisy hyphen background
- Animated scanning biometric laser beam sweeping across the portrait
- Pulsing sci-fi targeting HUD brackets and identity telemetry
- 16-channel dancing audio visualizer spectrum bars
- macOS window header with liquid glass border and whoami typewriter footer
Pure SMIL vector animation, 60 FPS, zero lag, self-contained SVG.
"""

import os
import requests
from io import BytesIO
from PIL import Image, ImageOps, ImageEnhance

USERNAME = "exepngsam"
AVATAR_URL = f"https://avatars.githubusercontent.com/u/295740281?v=4"
OUTPUT_FILE = "terminal-card.svg"

RAMP = "   ..::--==++**##%%@@"


def fetch_and_convert_avatar(username=USERNAME, width_chars=40):
    """Fetches user avatar and extracts clean character silhouette without flat background."""
    avatar_url = f"https://github.com/{username}.png"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    img = None
    for url in [AVATAR_URL, avatar_url]:
        try:
            r = requests.get(url, headers=headers, timeout=8)
            if r.status_code == 200:
                img = Image.open(BytesIO(r.content))
                break
        except Exception as e:
            print(f"[WARN] Fetch from {url} failed: {e}")

    if img is None:
        if os.path.exists("avatar_test.png"):
            img = Image.open("avatar_test.png")
        else:
            img = Image.new("RGB", (200, 200), color=(15, 23, 42))

    # Crop closer to character face/silhouette
    w, h = img.size
    cropped = img.crop((int(w * 0.10), int(h * 0.10), int(w * 0.90), int(h * 0.96)))
    gray = cropped.convert("L")
    gray = ImageOps.autocontrast(gray, cutoff=2)
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(2.4)

    target_h = int(width_chars * (gray.height / gray.width) * 0.5)
    target_h = max(18, min(23, target_h))
    resized = gray.resize((width_chars, target_h), Image.Resampling.LANCZOS)

    ascii_lines = []
    ramp_len = len(RAMP)
    for y in range(target_h):
        line_chars = []
        for x in range(width_chars):
            pixel = resized.getpixel((x, y))
            # Filter out flat background tone (between 46 and 74 in enhanced gray)
            if 46 <= pixel <= 74:
                line_chars.append(" ")
            else:
                idx = int(pixel / 256 * ramp_len)
                char = RAMP[min(idx, ramp_len - 1)]
                if char == "<":
                    char = "&lt;"
                elif char == ">":
                    char = "&gt;"
                elif char == "&":
                    char = "&amp;"
                line_chars.append(char)
        ascii_lines.append("".join(line_chars))

    return ascii_lines


def generate_svg(ascii_lines, output_path=OUTPUT_FILE):
    """Generates the macOS terminal card SVG with rich background animations."""
    card_width = 510
    card_height = 570

    start_x = 36
    start_y = 78
    line_height = 14.8

    num_lines = len(ascii_lines)
    row_delay_step = 0.05
    anim_start = 0.3

    svg_parts = []
    # Header & SVG Defs
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {card_width} {card_height}" width="100%" height="auto" style="max-width: {card_width}px; font-family: -apple-system, BlinkMacSystemFont, 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;">
  <defs>
    <!-- Liquid Glass Dark Background -->
    <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141d2a" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#0c121a" stop-opacity="0.97" />
      <stop offset="100%" stop-color="#070b10" stop-opacity="0.99" />
    </linearGradient>

    <!-- Glowing Liquid Glass Border -->
    <linearGradient id="term-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#00f0ff;#39d353;#a855f7;#00f0ff" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#39d353" stop-opacity="0.8">
        <animate attributeName="stop-color" values="#39d353;#a855f7;#00f0ff;#39d353" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Laser & Cursor Glow -->
    <filter id="laser-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="hud-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .term-title {{ font-size: 13px; fill: #7d8590; font-weight: 700; font-family: monospace; }}
    .ascii-text {{ font-size: 11.5px; fill: #00f0ff; letter-spacing: 2px; font-weight: 700; font-family: 'SFMono-Regular', Consolas, monospace; }}
    .matrix-code {{ font-size: 9.5px; font-family: monospace; font-weight: 600; fill: #00f0ff; opacity: 0.16; }}
    .cmd-prompt {{ font-size: 13px; fill: #39d353; font-weight: 700; font-family: monospace; }}
    .cmd-text {{ font-size: 13px; fill: #ffffff; font-weight: 600; font-family: monospace; }}
    .whoami-title {{ font-size: 13.5px; fill: #00f0ff; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, monospace; }}
    .whoami-sub {{ font-size: 12px; fill: #a855f7; font-weight: 600; font-family: monospace; }}
    .hud-txt {{ font-size: 9px; font-weight: 700; font-family: monospace; fill: #7d8590; }}
  </style>

  <!-- Outer Liquid Glass Frame -->
  <rect x="2" y="2" width="{card_width - 4}" height="{card_height - 4}" rx="16" fill="url(#term-bg)" stroke="url(#term-border)" stroke-width="1.8" />

  <!-- Window Header Bar -->
  <g transform="translate(20, 20)">
    <circle cx="0" cy="5" r="5" fill="#ff5f56" />
    <circle cx="15" cy="5" r="5" fill="#ffbd2e" />
    <circle cx="30" cy="5" r="5" fill="#27c93f" />

    <text x="48" y="9.5" class="term-title">
      <tspan fill="#00f0ff">exepngsam</tspan>@<tspan fill="#39d353">cyberdeck</tspan>: <tspan fill="#e6edf3">~/avatar.ascii</tspan>
    </text>

    <!-- Top Right Status Pill -->
    <rect x="{card_width - 148}" y="-2" width="108" height="18" rx="9" fill="#161b22" stroke="#30363d" stroke-width="1" />
    <circle cx="{card_width - 138}" cy="7" r="2.8" fill="#39d353">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <text x="{card_width - 128}" y="11" font-size="9" fill="#00f0ff" font-weight="800" font-family="monospace">BIO_MATCH: 99%</text>
  </g>

  <!-- Header Separator -->
  <line x1="16" y1="48" x2="{card_width - 16}" y2="48" stroke="#21262d" stroke-width="1" />

  <!-- Background Animated Matrix Digital Streams -->
  <g class="matrix-code">
    <text x="35" y="-10">010110010101
      <animate attributeName="y" values="-20; {card_height + 20}" dur="5s" repeatCount="indefinite" />
    </text>
    <text x="110" y="-10">SYS_AI_CORE
      <animate attributeName="y" values="-20; {card_height + 20}" dur="6.5s" repeatCount="indefinite" begin="1s" />
    </text>
    <text x="190" y="-10">AUTONOMOUS
      <animate attributeName="y" values="-20; {card_height + 20}" dur="5.2s" repeatCount="indefinite" begin="0.4s" />
    </text>
    <text x="280" y="-10">011010010110
      <animate attributeName="y" values="-20; {card_height + 20}" dur="7s" repeatCount="indefinite" begin="2s" />
    </text>
    <text x="360" y="-10">QUANTUM_DECK
      <animate attributeName="y" values="-20; {card_height + 20}" dur="4.8s" repeatCount="indefinite" begin="1.2s" />
    </text>
    <text x="440" y="-10">101100101001
      <animate attributeName="y" values="-20; {card_height + 20}" dur="6s" repeatCount="indefinite" begin="0.8s" />
    </text>
  </g>

  <!-- Cyberpunk Biometric HUD Targeting Reticles around Portrait -->
  <g stroke="#00f0ff" stroke-width="1.2" fill="none" opacity="0.65" filter="url(#hud-glow)">
    <!-- Top-Left Corner -->
    <path d="M 28 85 L 28 65 L 48 65" />
    <!-- Top-Right Corner -->
    <path d="M {card_width - 28} 85 L {card_width - 28} 65 L {card_width - 48} 65" />
    <!-- Bottom-Left Corner -->
    <path d="M 28 375 L 28 395 L 48 395" />
    <!-- Bottom-Right Corner -->
    <path d="M {card_width - 28} 375 L {card_width - 28} 395 L {card_width - 48} 395" />
  </g>

  <!-- Animated Scanning Laser Beam -->
  <line x1="28" y1="70" x2="{card_width - 28}" y2="70" stroke="#00f0ff" stroke-width="2" opacity="0.75" filter="url(#laser-glow)">
    <animate attributeName="y1" values="70; 390; 70" dur="3.2s" repeatCount="indefinite" />
    <animate attributeName="y2" values="70; 390; 70" dur="3.2s" repeatCount="indefinite" />
    <animate attributeName="stroke" values="#00f0ff;#39d353;#a855f7;#00f0ff" dur="6.4s" repeatCount="indefinite" />
  </line>

  <!-- ASCII Art Section (Row-by-Row Reveal + Sweeping Cursor) -->
  <g id="ascii-portrait">
''')

    for i, line in enumerate(ascii_lines):
        y_pos = start_y + (i * line_height)
        r_delay = anim_start + (i * row_delay_step)
        sweep_dur = row_delay_step

        # ASCII text line
        svg_parts.append(f'''    <!-- Row {i} -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.04s" begin="{r_delay:.3f}s" fill="freeze" />
      <text x="{start_x}" y="{y_pos}" class="ascii-text">{line}</text>
    </g>''')

        # Cursor block sweeping left to right
        end_x = start_x + (len(line) * 7.5)
        svg_parts.append(f'''    <rect x="{start_x}" y="{y_pos - 10}" width="8" height="13" fill="#ffffff" filter="url(#laser-glow)" opacity="0">
      <animate attributeName="opacity" values="0; 0.9; 0.9; 0" keyTimes="0; 0.15; 0.85; 1" dur="{sweep_dur:.3f}s" begin="{r_delay:.3f}s" fill="freeze" />
      <animate attributeName="x" values="{start_x}; {end_x}" dur="{sweep_dur:.3f}s" begin="{r_delay:.3f}s" fill="freeze" />
      <animate attributeName="fill" values="#00f0ff; #ffffff; #39d353" dur="{sweep_dur:.3f}s" begin="{r_delay:.3f}s" fill="freeze" />
    </rect>''')

    svg_parts.append('  </g>\n')

    # Animated Audio Visualizer / Spectrum Analyzer Bars at base of portrait
    spectrum_y = start_y + (num_lines * line_height) + 12
    svg_parts.append(f'''  <!-- 16-Channel Audio / Telemetry Spectrum Bars -->
  <g transform="translate({start_x}, {spectrum_y})">
''')

    spec_colors = ["#00f0ff", "#39d353", "#a855f7", "#00f0ff", "#39d353", "#ffa657", "#00f0ff", "#39d353"]
    for bar_i in range(16):
        bx = bar_i * 26
        bcol = spec_colors[bar_i % len(spec_colors)]
        h1 = (bar_i * 3 % 16) + 6
        h2 = (bar_i * 7 % 20) + 8
        h3 = (bar_i * 5 % 14) + 5
        dur = 0.8 + (bar_i * 0.08)
        svg_parts.append(f'''    <rect x="{bx}" y="0" width="16" height="{h1}" rx="3" fill="{bcol}" opacity="0.8">
      <animate attributeName="height" values="{h1}; {h2}; {h3}; {h2}; {h1}" dur="{dur:.2f}s" repeatCount="indefinite" />
      <animate attributeName="y" values="{20 - h1}; {20 - h2}; {20 - h3}; {20 - h2}; {20 - h1}" dur="{dur:.2f}s" repeatCount="indefinite" />
    </rect>''')

    svg_parts.append('  </g>\n')

    # Footer Divider & Typewriter Console
    footer_start_delay = anim_start + (num_lines * row_delay_step) + 0.2
    whoami_typed_delay = footer_start_delay + 0.6
    res1_delay = whoami_typed_delay + 0.3
    res2_delay = res1_delay + 0.25
    res3_delay = res2_delay + 0.25

    footer_y = spectrum_y + 44
    div_y = footer_y - 12

    svg_parts.append(f'''  <!-- Footer Divider -->
  <line x1="16" y1="{div_y}" x2="{card_width - 16}" y2="{div_y}" stroke="#21262d" stroke-width="1" />

  <!-- Terminal Footer: $ whoami animation -->
  <g transform="translate(24, {footer_y})">
    <!-- Prompt symbol -->
    <text x="0" y="13" class="cmd-prompt">exepngsam@deck:~$</text>

    <!-- Typewritten 'whoami' command -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.05s" begin="{footer_start_delay:.3f}s" fill="freeze" />
      <text x="142" y="13" class="cmd-text">whoami</text>
    </g>

    <!-- Blinking command cursor -->
    <rect x="198" y="2" width="8" height="14" fill="#00f0ff">
      <animate attributeName="opacity" values="1; 0; 1" dur="0.8s" repeatCount="indefinite" begin="{footer_start_delay:.3f}s" />
    </rect>

    <!-- Output Line 1: Identity -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.15s" begin="{res1_delay:.3f}s" fill="freeze" />
      <text x="2" y="34" class="whoami-title">
        <tspan fill="#39d353">➜ </tspan>
        <tspan fill="#ffffff">Sam</tspan>
        <tspan fill="#7d8590"> (@exepngsam)</tspan>
      </text>
    </g>

    <!-- Output Line 2: Role & System -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.15s" begin="{res2_delay:.3f}s" fill="freeze" />
      <text x="16" y="52" class="whoami-sub">
        <tspan fill="#00f0ff">⚡</tspan> AI Systems &amp; Full-Stack Architect
      </text>
    </g>

    <!-- Output Line 3: Live Telemetry Pulse -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.15s" begin="{res3_delay:.3f}s" fill="freeze" />
      <text x="16" y="68" font-size="10" font-family="monospace" fill="#7d8590">
        <tspan fill="#39d353">>>> </tspan>
        <tspan fill="#ffa657">111 COMMITS IN 2026</tspan>
        <tspan fill="#7d8590"> // </tspan>
        <tspan fill="#00f0ff">100% OPERATIONAL</tspan>
      </text>
    </g>
  </g>
</svg>''')

    svg_content = "\n".join(svg_parts)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[SUCCESS] Generated {output_path} ({len(svg_content)} bytes)")
    return output_path


def main():
    print(f"[*] Starting Upgraded Terminal ASCII Card SVG Generation for user: {USERNAME}")
    ascii_lines = fetch_and_convert_avatar(USERNAME)
    generate_svg(ascii_lines, OUTPUT_FILE)


if __name__ == "__main__":
    main()
