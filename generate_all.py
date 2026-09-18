"""
generate_all.py
Master Python orchestrator for generating the complete premium animated GitHub Profile suite
for @exepngsam.

Executes:
1. generate_contribution_svg.py -> github-contribution-animation.svg (53x7 slant reveal & glint)
2. generate_terminal_card.py    -> terminal-card.svg (ASCII avatar + sweeping cursor + whoami)
3. generate_info_card.py        -> info-card.svg (Neofetch terminal card with staggered reveals)
4. Injects side-by-side table and centered contribution animation into README.md
"""

import os
import sys
import generate_contribution_svg
import generate_terminal_card
import generate_info_card

USERNAME = "exepngsam"

README_CONTENT = f"""<div align="center">

# ⚡ SAM // ARCHITECT &amp; BUILDER
### 🌌 Autonomous AI Systems • Serverless Edge • Full-Stack Architecture
```text
[ SYSTEM INITIALIZED: CYBERDECK OS v2.4 ] ~ CONNECTED TO GITHUB:@{USERNAME}
```

[![GitHub Followers](https://img.shields.io/github/followers/{USERNAME}?style=for-the-badge&logo=github&color=00f0ff&labelColor=0d1117)](https://github.com/{USERNAME})
[![Total Repos](https://img.shields.io/badge/Public_Repos-7-39d353?style=for-the-badge&logo=git&labelColor=0d1117)](https://github.com/{USERNAME}?tab=repositories)
[![Annual Contributions](https://img.shields.io/badge/Contributions_2026-109-ffa657?style=for-the-badge&logo=github&labelColor=0d1117)](https://github.com/{USERNAME})
[![Tech Stack](https://img.shields.io/badge/Stack-TypeScript_%7C_Python_%7C_AWS_Bedrock-a855f7?style=for-the-badge&logo=vibe&labelColor=0d1117)](https://github.com/{USERNAME})

<br />

<!-- Side-by-Side Terminal & Neofetch Cards via HTML Table -->
<table border="0" cellpadding="0" cellspacing="0" style="border: none; background: transparent; width: 100%; max-width: 880px;">
  <tr>
    <td width="50%" align="center" valign="top" style="border: none; padding: 6px;">
      <img src="./terminal-card.svg" alt="Terminal ASCII Portrait" width="100%" />
    </td>
    <td width="50%" align="center" valign="top" style="border: none; padding: 6px;">
      <img src="./info-card.svg" alt="Neofetch System Telemetry" width="100%" />
    </td>
  </tr>
</table>

<br />

<!-- Centered Animated Contribution Activity Calendar -->
<div align="center">
  <img src="./github-contribution-animation.svg" alt="GitHub 53x7 Contribution Activity Calendar" width="100%" style="max-width: 880px;" />
</div>

<br />

</div>

---

## 🚀 Featured Platforms & Systems

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🤖 <a href="https://github.com/{USERNAME}/Nexora">Nexora</a></h3>
      <p><strong>Autonomous AI Incident Coordination Platform</strong> that turns operational incidents into immediate action. Powered by Featherless AI &amp; Caspian for reasoning, autonomous escalation, and real-time coordination.</p>
      <p>
        <a href="https://nexora-three-mu.vercel.app"><b>🌐 Live Demo</b></a> • 
        <code>TypeScript</code> <code>Featherless AI</code> <code>Next.js</code>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🧠 <a href="https://github.com/{USERNAME}/Stark-Ai">Stark-Ai</a></h3>
      <p><strong>Futuristic Personal AI Operating System</strong> that transforms natural-language commands into automated intelligent workflows, agentic tool execution, and continuous real-time assistance.</p>
      <p>
        <a href="https://starkai-fawn.vercel.app/"><b>🌐 Live Demo</b></a> • 
        <code>TypeScript</code> <code>Agentic AI</code> <code>Automation</code>
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🔐 <a href="https://github.com/{USERNAME}/TruthSeal-AI">TruthSeal AI</a></h3>
      <p><strong>Digital Trust &amp; Media Forensics Platform</strong> combining cryptographic verification, AI forensic analysis, provenance tracking, and credential revocation to detect manipulated communications.</p>
      <p>
        <a href="https://truth-seal-ai.vercel.app"><b>🌐 Live Demo</b></a> • 
        <code>Cryptographic Verification</code> <code>Media Forensics</code>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🌾 <a href="https://github.com/{USERNAME}/YieldWay-Ai">YieldWay AI</a></h3>
      <p><strong>100% Serverless AgriTech Logistics Engine</strong> engineered for the 'Bharat Builds' AWS Hackathon. Powered by Amazon Bedrock (GenAI), Next.js, and AWS CDK to mitigate post-harvest supply loss.</p>
      <p>
        <a href="https://frontend-lake-zeta-88.vercel.app"><b>🌐 Live Demo</b></a> • 
        <code>AWS Bedrock</code> <code>AWS CDK</code> <code>Serverless</code>
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏙️ <a href="https://github.com/{USERNAME}/Civicfix-ai">CivicFix AI</a></h3>
      <p><strong>AI-Powered Civic Issue Intelligence &amp; Resolution Engine</strong> built on AWS with automated severity detection, duplicate deduplication, and real-time escalation workflows.</p>
      <p>
        <a href="https://civicfix-ai-roan.vercel.app"><b>🌐 Live Demo</b></a> • 
        <code>AWS Cloud</code> <code>Next.js</code> <code>Issue Deduplication</code>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>✨ <a href="https://github.com/{USERNAME}/Portfolio">Terminal OS &amp; Physics Engine</a></h3>
      <p><strong>Brutalist Zero-Bloat Portfolio OS</strong> featuring an interactive local AI chatbot, an 800-node 3D particle physics simulation, and custom system-level UI components.</p>
      <p>
        <a href="https://portfolio19s.vercel.app/"><b>🌐 Live Demo</b></a> • 
        <code>3D Physics Engine</code> <code>Zero-Bloat</code> <code>Local AI</code>
      </p>
    </td>
  </tr>
</table>

---

## 🛠️ Core Tech Arsenal

<div align="center">

| Domain | Technologies |
| :--- | :--- |
| **Languages** | `TypeScript` • `Python` • `JavaScript` • `SQL` • `HTML5 / CSS3` |
| **Frontend &amp; UI** | `Next.js 15` • `React 19` • `TailwindCSS` • `Lucide` • `Canvas / WebGL` |
| **AI &amp; Autonomous Agents** | `Amazon Bedrock` • `Featherless AI` • `Agentic Workflows` • `Media Forensics` |
| **Cloud &amp; Infrastructure** | `AWS (CDK, Lambda, S3)` • `Vercel Edge` • `Serverless Architecture` • `Docker` |
| **Database &amp; Storage** | `PostgreSQL` • `Redis` • `Vector DBs` • `Cloudflare / Edge KV` |

</div>

---

<div align="center">

```
>>> [CONNECTION ESTABLISHED] ~ ping exepngsam.dev: 0.12ms (status: optimal)
```

**Crafted with pure SMIL vector animations &amp; Cyberpunk aesthetics.**

</div>
"""


def main():
    print("=" * 65)
    print("   CYBERPUNK GITHUB PROFILE GENERATOR SUITE — @exepngsam")
    print("=" * 65)

    # 1. Generate Contribution Graph SVG
    print("\n[1/4] Generating 53x7 Animated Contribution Calendar...")
    grid, total, months = generate_contribution_svg.fetch_contributions(USERNAME)
    contrib_svg = generate_contribution_svg.generate_svg(grid, total, months)
    print(f"      -> {contrib_svg} created.")

    # 2. Generate Terminal ASCII Card SVG
    print("\n[2/4] Generating macOS Terminal ASCII Portrait Card...")
    ascii_lines = generate_terminal_card.fetch_and_convert_avatar(USERNAME)
    terminal_svg = generate_terminal_card.generate_svg(ascii_lines)
    print(f"      -> {terminal_svg} created.")

    # 3. Generate Neofetch Info Card SVG
    print("\n[3/4] Generating Neofetch Telemetry Info Card...")
    info_svg = generate_info_card.generate_svg()
    print(f"      -> {info_svg} created.")

    # 4. Inject into README.md
    print("\n[4/4] Writing README.md with side-by-side cards & centered calendar...")
    readme_path = "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(README_CONTENT.strip() + "\n")
    print(f"      -> {readme_path} created ({len(README_CONTENT)} bytes).")

    print("\n" + "=" * 65)
    print("   [ALL ASSETS GENERATED SUCCESSFULLY]")
    print("   - github-contribution-animation.svg")
    print("   - terminal-card.svg")
    print("   - info-card.svg")
    print("   - README.md")
    print("=" * 65)


if __name__ == "__main__":
    main()
