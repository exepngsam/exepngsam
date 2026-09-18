"""
generate_terminal_card.py
Generates an animated macOS-style terminal window containing an ASCII art portrait
of the GitHub user @exepngsam, rendered with row-by-row top-to-bottom reveals,
a sweeping cursor block, and a typewriter footer for '$ whoami'.
Pure self-contained SMIL SVG.
"""

import os
import requests
from io import BytesIO
from PIL import Image, ImageOps, ImageEnhance

USERNAME = "exepngsam"
AVATAR_URL = f"https://avatars.githubusercontent.com/u/295740281?v=4"
OUTPUT_FILE = "terminal-card.svg"

# ASCII ramp for high-contrast cyberpunk display
RAMP = " .:-=+*#%@"


def fetch_and_convert_avatar(username=USERNAME, width_chars=46):
    """Fetches user avatar and converts into high-contrast ASCII art."""
    avatar_url = f"https://github.com/{username}.png"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    img = None
    # Try fetching from GitHub
    for url in [AVATAR_URL, avatar_url]:
        try:
            r = requests.get(url, headers=headers, timeout=8)
            if r.status_code == 200:
                img = Image.open(BytesIO(r.content))
                break
        except Exception as e:
            print(f"[WARN] Fetch from {url} failed: {e}")

    # Fallback if offline or network error
    if img is None:
        if os.path.exists("avatar_test.png"):
            img = Image.open("avatar_test.png")
        else:
            # Generate synthetic profile silhouette
            img = Image.new("RGB", (200, 200), color=(15, 23, 42))

    # Pre-process image for optimal ASCII representation
    gray = img.convert("L")
    # Auto-contrast to maximize range
    gray = ImageOps.autocontrast(gray, cutoff=2)
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(1.7)

    # Compute height with monospace font aspect ratio correction (~0.5)
    aspect = gray.height / gray.width
    height_chars = int(width_chars * aspect * 0.48)
    height_chars = max(18, min(24, height_chars))

    resized = gray.resize((width_chars, height_chars), Image.Resampling.LANCZOS)

    ascii_lines = []
    ramp_len = len(RAMP)
    for y in range(height_chars):
        line_chars = []
        for x in range(width_chars):
            pixel = resized.getpixel((x, y))
            idx = int(pixel / 256 * ramp_len)
            char = RAMP[min(idx, ramp_len - 1)]
            # Escape XML entities
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
    """Generates the macOS terminal card SVG with pure SMIL animations (scaled up & enhanced)."""
    card_width = 510
    card_height = 570

    start_x = 28
    start_y = 74
    line_height = 15.2

    num_lines = len(ascii_lines)
    row_delay_step = 0.06  # 60ms per line
    anim_start = 0.4       # initial pause

    svg_parts = []
    # Header & SVG Defs
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {card_width} {card_height}" width="100%" height="auto" style="max-width: {card_width}px; font-family: -apple-system, BlinkMacSystemFont, 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;">
  <defs>
    <!-- Liquid Glass Background Gradient -->
    <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141d2a" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#0c121a" stop-opacity="0.97" />
      <stop offset="100%" stop-color="#070b10" stop-opacity="0.99" />
    </linearGradient>

    <!-- Glowing Liquid Glass Border Gradient -->
    <linearGradient id="term-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9">
        <animate attributeName="stop-color" values="#00f0ff;#39d353;#a855f7;#00f0ff" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#39d353" stop-opacity="0.8">
        <animate attributeName="stop-color" values="#39d353;#a855f7;#00f0ff;#39d353" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Cursor Glow -->
    <filter id="cursor-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Scanline Pattern -->
    <pattern id="scanlines" width="100" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="100" y2="0" stroke="#000000" stroke-opacity="0.14" stroke-width="1.2" />
    </pattern>
  </defs>

  <style>
    .term-title {{ font-size: 13px; fill: #7d8590; font-weight: 700; font-family: monospace; }}
    .ascii-text {{ font-size: 11.2px; fill: #00f0ff; letter-spacing: 2.1px; font-weight: 600; font-family: 'SFMono-Regular', Consolas, monospace; }}
    .cmd-prompt {{ font-size: 13px; fill: #39d353; font-weight: 700; font-family: monospace; }}
    .cmd-text {{ font-size: 13px; fill: #ffffff; font-weight: 600; font-family: monospace; }}
    .whoami-title {{ font-size: 13.5px; fill: #00f0ff; font-weight: 800; font-family: -apple-system, BlinkMacSystemFont, monospace; }}
    .whoami-sub {{ font-size: 12px; fill: #a855f7; font-weight: 600; font-family: monospace; }}
  </style>

  <!-- Outer Liquid Glass Frame -->
  <rect x="2" y="2" width="{card_width - 4}" height="{card_height - 4}" rx="16" fill="url(#term-bg)" stroke="url(#term-border)" stroke-width="1.8" />

  <!-- Window Header Bar -->
  <g transform="translate(20, 20)">
    <!-- macOS buttons -->
    <circle cx="0" cy="5" r="5" fill="#ff5f56" />
    <circle cx="15" cy="5" r="5" fill="#ffbd2e" />
    <circle cx="30" cy="5" r="5" fill="#27c93f" />

    <!-- Window Title -->
    <text x="48" y="9.5" class="term-title">
      <tspan fill="#00f0ff">exepngsam</tspan>@<tspan fill="#39d353">cyberdeck</tspan>: <tspan fill="#e6edf3">~/avatar.ascii</tspan>
    </text>

    <!-- Right status pill -->
    <rect x="{card_width - 145}" y="-2" width="105" height="18" rx="9" fill="#161b22" stroke="#30363d" stroke-width="1" />
    <text x="{card_width - 132}" y="11" font-size="9.5" fill="#58a6ff" font-weight="800" font-family="monospace">PORTRAIT.RAW</text>
  </g>

  <!-- Header Separator -->
  <line x1="16" y1="48" x2="{card_width - 16}" y2="48" stroke="#21262d" stroke-width="1" />

  <!-- ASCII Art Section (Row-by-Row Reveal + Sweeping Cursor) -->
  <g id="ascii-portrait">
''')

    # Add each ASCII row with SMIL animation and cursor sweep
    for i, line in enumerate(ascii_lines):
        y_pos = start_y + (i * line_height)
        r_delay = anim_start + (i * row_delay_step)
        sweep_dur = row_delay_step

        # ASCII text line (reveals row-by-row)
        svg_parts.append(f'''    <!-- Row {i} -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.04s" begin="{r_delay:.3f}s" fill="freeze" />
      <text x="{start_x}" y="{y_pos}" class="ascii-text">{line}</text>
    </g>''')

        # Cursor block sweeping left to right across this row during reveal
        end_x = start_x + (len(line) * 7.2)
        svg_parts.append(f'''    <rect x="{start_x}" y="{y_pos - 9}" width="7" height="11" fill="#ffffff" filter="url(#cursor-glow)" opacity="0">
      <animate attributeName="opacity" values="0; 0.9; 0.9; 0" keyTimes="0; 0.15; 0.85; 1" dur="{sweep_dur:.3f}s" begin="{r_delay:.3f}s" fill="freeze" />
      <animate attributeName="x" values="{start_x}; {end_x}" dur="{sweep_dur:.3f}s" begin="{r_delay:.3f}s" fill="freeze" />
      <animate attributeName="fill" values="#00f0ff; #ffffff; #39d353" dur="{sweep_dur:.3f}s" begin="{r_delay:.3f}s" fill="freeze" />
    </rect>''')

    svg_parts.append('  </g>\n')

    # CRT scanline overlay
    svg_parts.append(f'''  <!-- Subtle Scanline Texture -->
  <rect x="14" y="44" width="{card_width - 28}" height="{card_height - 110}" fill="url(#scanlines)" pointer-events="none" />
''')

    # Footer Typewriter Simulation
    footer_start_delay = anim_start + (num_lines * row_delay_step) + 0.2
    whoami_typed_delay = footer_start_delay + 0.6
    res1_delay = whoami_typed_delay + 0.3
    res2_delay = res1_delay + 0.25

    footer_y = start_y + (num_lines * line_height) + 18
    div_y = footer_y - 12

    svg_parts.append(f'''  <!-- Footer Divider -->
  <line x1="14" y1="{div_y}" x2="{card_width - 14}" y2="{div_y}" stroke="#21262d" stroke-width="1" />

  <!-- Terminal Footer: $ whoami animation -->
  <g transform="translate(18, {footer_y})">
    <!-- Prompt symbol -->
    <text x="0" y="13" class="cmd-prompt">exepngsam@deck:~$</text>

    <!-- Typewritten 'whoami' command -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.05s" begin="{footer_start_delay:.3f}s" fill="freeze" />
      <text x="140" y="13" class="cmd-text">whoami</text>
    </g>

    <!-- Blinking command cursor -->
    <rect x="195" y="2" width="7.5" height="13" fill="#00f0ff">
      <animate attributeName="opacity" values="1; 0; 1" dur="0.8s" repeatCount="indefinite" begin="{footer_start_delay:.3f}s" />
    </rect>

    <!-- Output Line 1: Identity -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.15s" begin="{res1_delay:.3f}s" fill="freeze" />
      <text x="2" y="36" class="whoami-title">
        <tspan fill="#39d353">➜ </tspan>
        <tspan fill="#ffffff">Sam</tspan>
        <tspan fill="#7d8590"> (@exepngsam)</tspan>
      </text>
    </g>

    <!-- Output Line 2: Role & System -->
    <g opacity="0">
      <animate attributeName="opacity" values="0; 1" dur="0.15s" begin="{res2_delay:.3f}s" fill="freeze" />
      <text x="16" y="54" class="whoami-sub">
        <tspan fill="#00f0ff">⚡</tspan> AI Systems &amp; Full-Stack Architect
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
    print(f"[*] Starting Terminal ASCII Card SVG Generation for user: {USERNAME}")
    ascii_lines = fetch_and_convert_avatar(USERNAME)
    generate_svg(ascii_lines, OUTPUT_FILE)


if __name__ == "__main__":
    main()
