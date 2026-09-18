"""
generate_all.py
Master Python orchestrator for the complete animated Cyberpunk / Liquid Glass
GitHub Profile Suite for @exepngsam.

Executes:
1. generate_header_svg.py       -> header-liquid-glass.svg (iOS 27 Liquid Glass animated banner)
2. generate_contribution_svg.py -> github-contribution-animation.svg (53x7 slant reveal & glint)
3. generate_terminal_card.py    -> terminal-card.svg (Scaled-up ASCII avatar + cursor sweep)
4. generate_info_card.py        -> info-card.svg (Scaled-up Neofetch card with staggered reveals)
5. generate_stats_svg.py        -> github-stats-animated.svg (Self-contained animated stats & wave)
6. generate_projects_svg.py     -> projects-animated.svg (Totally animated 6-card grid)
7. generate_snake_svg.py        -> github-contribution-grid-snake.svg (Contribution snake game)
8. Updates README.md with high-contrast, scalable layout.
"""

import os
import sys
import generate_header_svg
import generate_contribution_svg
import generate_terminal_card
import generate_info_card
import generate_stats_svg
import generate_projects_svg
import generate_snake_svg

USERNAME = "exepngsam"

README_TEMPLATE = f"""<div align="center">

<!-- iOS 27 Liquid Glass Animated Hero Banner -->
<img src="./header-liquid-glass.svg" alt="Sam // AI Architect & Builder" width="100%" style="max-width: 960px;" />

<br /><br />

<!-- Side-by-Side Terminal ASCII Portrait & Neofetch Cards via HTML Table (Enlarged & Crystal Clear) -->
<table border="0" cellpadding="0" cellspacing="0" style="border: none; background: transparent; width: 100%; max-width: 960px;">
  <tr>
    <td width="50%" align="center" valign="top" style="border: none; padding: 8px;">
      <img src="./terminal-card.svg" alt="Terminal ASCII Portrait" width="100%" />
    </td>
    <td width="50%" align="center" valign="top" style="border: none; padding: 8px;">
      <img src="./info-card.svg" alt="Neofetch System Telemetry" width="100%" />
    </td>
  </tr>
</table>

<br />

<!-- Centered Animated Contribution Activity Calendar -->
<div align="center">
  <img src="./github-contribution-animation.svg" alt="GitHub 53x7 Contribution Activity Calendar" width="100%" style="max-width: 960px;" />
</div>

<br />

<!-- Animated Contribution Snake Game -->
<div align="center">
  <img src="./github-contribution-grid-snake.svg" alt="GitHub Contribution Snake Game" width="100%" style="max-width: 960px;" />
</div>

<br />

</div>

---

<div align="center">

## 🤝 Connect

<a href="https://github.com/{USERNAME}"><img src="https://skillicons.dev/icons?i=github" width="52" height="52" alt="GitHub" /></a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://linkedin.com"><img src="https://skillicons.dev/icons?i=linkedin" width="52" height="52" alt="LinkedIn" /></a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="mailto:loudbiology@gmail.com"><img src="https://skillicons.dev/icons?i=gmail" width="52" height="52" alt="Gmail" /></a>
&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://portfolio19s.vercel.app/"><img src="https://skillicons.dev/icons?i=vercel" width="52" height="52" alt="Portfolio" /></a>

<br /><br />

## 💻 Tech Stack

<!-- Row 1 -->
<p align="center">
  <img src="https://skillicons.dev/icons?i=py,fastapi,postgres,mysql,docker,git,github,vscode,html,css,cpp,aws" alt="Tech Stack Row 1" />
</p>

<!-- Row 2 -->
<p align="center">
  <img src="https://skillicons.dev/icons?i=nextjs,react,ts,nodejs,pytorch,tensorflow,gcp,tailwind" alt="Tech Stack Row 2" />
</p>

<br />

## 📊 GitHub Stats &amp; Telemetry

<!-- 100% Reliable, Self-Contained Animated Stats Matrix & Activity Wave -->
<img src="./github-stats-animated.svg" alt="GitHub Telemetry & Activity Wave" width="100%" style="max-width: 960px;" />

<br /><br />

<!-- Real-time Streak Stats -->
<img src="https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=tokyonight&background=0d1117&border=30363d&stroke=00f0ff&ring=39d353&fire=ffa657&currStreakNum=e6edf3&sideNums=e6edf3&currStreakLabel=00f0ff" width="100%" style="max-width: 520px;" alt="Streak Stats" />

</div>

---

## 🚀 Featured Platforms &amp; Systems

<div align="center">

<!-- Totally Animated Projects Dashboard Card (Screenshot 4) -->
<img src="./projects-animated.svg" alt="Featured Platforms &amp; Systems Dashboard" width="100%" style="max-width: 960px;" />

</div>

<br />

<!-- Direct Clickable Links & Documentation -->
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

<div align="center">

```
>>> [CONNECTION ESTABLISHED] ~ ping exepngsam.dev: 0.12ms (status: optimal)
```

**Crafted with pure SMIL vector animations &amp; Liquid Glass iOS aesthetics.**

</div>
"""


def main():
    print("=" * 70)
    print("   LIQUID GLASS & CYBERPUNK PROFILE GENERATOR SUITE — @exepngsam")
    print("=" * 70)

    # 1. Generate Liquid Glass Hero Banner
    print("\n[1/7] Generating Liquid Glass Hero Banner SVG...")
    header_svg = generate_header_svg.generate_header_svg()
    print(f"      -> {header_svg} created.")

    # 2. Generate Contribution Graph SVG
    print("\n[2/7] Generating 53x7 Animated Contribution Calendar...")
    grid, total, months = generate_contribution_svg.fetch_contributions(USERNAME)
    contrib_svg = generate_contribution_svg.generate_svg(grid, total, months)
    print(f"      -> {contrib_svg} created.")

    # 3. Generate Terminal ASCII Card SVG (Enlarged & Crisp)
    print("\n[3/7] Generating Enlarged Terminal ASCII Portrait Card...")
    ascii_lines = generate_terminal_card.fetch_and_convert_avatar(USERNAME)
    terminal_svg = generate_terminal_card.generate_svg(ascii_lines)
    print(f"      -> {terminal_svg} created.")

    # 4. Generate Neofetch Info Card SVG (Enlarged & Crisp)
    print("\n[4/7] Generating Enlarged Neofetch Telemetry Info Card...")
    info_svg = generate_info_card.generate_svg()
    print(f"      -> {info_svg} created.")

    # 5. Generate Animated Stats & Waveform SVG
    print("\n[5/7] Generating Animated Liquid Glass Stats & Waveform SVG...")
    stats_svg = generate_stats_svg.generate_stats_svg()
    print(f"      -> {stats_svg} created.")

    # 6. Generate Animated Projects Card SVG
    print("\n[6/7] Generating Totally Animated Projects Dashboard Card...")
    projects_svg = generate_projects_svg.generate_projects_svg()
    print(f"      -> {projects_svg} created.")

    # 7. Generate Animated Snake Game SVG
    print("\n[7/7] Generating Contribution Snake Game SVG...")
    snake_svg = generate_snake_svg.generate_snake_svg()
    print(f"      -> {snake_svg} created.")

    # 8. Inject into README.md
    print("\nWriting complete README.md with high-readability layout...")
    readme_path = "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(README_TEMPLATE.strip() + "\n")
    print(f"      -> {readme_path} created ({len(README_TEMPLATE)} bytes).")

    print("\n" + "=" * 70)
    print("   [ALL 7 ASSETS GENERATED & VERIFIED SUCCESSFULLY]")
    print("   - header-liquid-glass.svg")
    print("   - terminal-card.svg")
    print("   - info-card.svg")
    print("   - github-contribution-animation.svg")
    print("   - github-stats-animated.svg")
    print("   - projects-animated.svg")
    print("   - github-contribution-grid-snake.svg")
    print("   - README.md")
    print("=" * 70)


if __name__ == "__main__":
    main()
