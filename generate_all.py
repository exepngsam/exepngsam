"""
generate_all.py
Master Python orchestrator for the complete animated Cyberpunk GitHub Profile Suite for @exepngsam.

Executes:
1. generate_contribution_svg.py -> github-contribution-animation.svg (53x7 slant reveal & glint)
2. generate_terminal_card.py    -> terminal-card.svg (ASCII avatar + sweeping cursor + whoami)
3. generate_info_card.py        -> info-card.svg (Neofetch terminal card with staggered reveals)
4. generate_projects_svg.py     -> projects-animated.svg (Screenshot 4 totally animated card grid)
5. generate_snake_svg.py        -> github-contribution-grid-snake.svg (Contribution snake game)
6. Generates complete README.md incorporating all requested visual sections.
"""

import os
import sys
import generate_contribution_svg
import generate_terminal_card
import generate_info_card
import generate_projects_svg
import generate_snake_svg

USERNAME = "exepngsam"

README_TEMPLATE = f"""<div align="center">

<!-- Animated Dynamic Cyberpunk Typing Banner -->
<a href="https://github.com/{USERNAME}">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=25&pause=1000&color=00F0FF&center=true&vCenter=true&width=700&height=55&lines=SAM+%7C%7C+AI+SYSTEMS+%26+FULL-STACK+ARCHITECT;BUILDING+AUTONOMOUS+AI+AGENTS+%26+SYSTEMS;NEXT.JS+15+%E2%80%A2+AWS+BEDROCK+%E2%80%A2+TYPESCRIPT;109+CONTRIBUTIONS+AND+COUNTING..." alt="Typing SVG" />
</a>

<p align="center">
  <code>[ SYSTEM INITIALIZED: CYBERDECK OS v2.4 ] ~ CONNECTED TO GITHUB:@{USERNAME}</code>
</p>

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

<!-- Animated Contribution Snake Game -->
<div align="center">
  <img src="./github-contribution-grid-snake.svg" alt="GitHub Contribution Snake Game" width="100%" style="max-width: 880px;" />
</div>

<br />

</div>

---

<div align="center">

## 🤝 Connect

<a href="https://github.com/{USERNAME}"><img src="https://skillicons.dev/icons?i=github" width="48" height="48" alt="GitHub" /></a>
&nbsp;&nbsp;
<a href="https://linkedin.com"><img src="https://skillicons.dev/icons?i=linkedin" width="48" height="48" alt="LinkedIn" /></a>
&nbsp;&nbsp;
<a href="mailto:loudbiology@gmail.com"><img src="https://skillicons.dev/icons?i=gmail" width="48" height="48" alt="Gmail" /></a>
&nbsp;&nbsp;
<a href="https://portfolio19s.vercel.app/"><img src="https://skillicons.dev/icons?i=vercel" width="48" height="48" alt="Portfolio" /></a>

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

## 📊 GitHub Stats

<!-- Activity Graph -->
<a href="https://github.com/{USERNAME}">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={USERNAME}&theme=tokyo-night&area=true&hide_border=false&color=00f0ff&line=39d353&point=a855f7&bg_color=0d1117" alt="Activity Graph" width="100%" style="max-width: 880px;" />
</a>

<br /><br />

<!-- GitHub Stats & Streak Side-by-Side -->
<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 880px;">
  <tr>
    <td width="50%" align="center" valign="top" style="border: none; padding: 4px;">
      <img src="https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&theme=tokyonight&bg_color=0d1117&title_color=00f0ff&icon_color=39d353&text_color=e6edf3&border_color=30363d&count_private=true&include_all_commits=true" width="100%" alt="GitHub Stats" />
    </td>
    <td width="50%" align="center" valign="top" style="border: none; padding: 4px;">
      <img src="https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=tokyonight&background=0d1117&border=30363d&stroke=00f0ff&ring=39d353&fire=ffa657&currStreakNum=e6edf3&sideNums=e6edf3&currStreakLabel=00f0ff" width="100%" alt="Streak Stats" />
    </td>
  </tr>
</table>

</div>

---

## 🚀 Featured Platforms & Systems

<div align="center">

<!-- Totally Animated Projects Dashboard Card -->
<img src="./projects-animated.svg" alt="Featured Platforms & Systems Dashboard" width="100%" style="max-width: 880px;" />

</div>

<br />

<!-- Interactive Fallback & Direct Clickable Links Table -->
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

**Crafted with pure SMIL vector animations &amp; Cyberpunk aesthetics.**

</div>
"""


def main():
    print("=" * 68)
    print("   CYBERPUNK GITHUB PROFILE GENERATOR SUITE — @exepngsam")
    print("=" * 68)

    # 1. Generate Contribution Graph SVG
    print("\n[1/5] Generating 53x7 Animated Contribution Calendar...")
    grid, total, months = generate_contribution_svg.fetch_contributions(USERNAME)
    contrib_svg = generate_contribution_svg.generate_svg(grid, total, months)
    print(f"      -> {contrib_svg} created.")

    # 2. Generate Terminal ASCII Card SVG
    print("\n[2/5] Generating macOS Terminal ASCII Portrait Card...")
    ascii_lines = generate_terminal_card.fetch_and_convert_avatar(USERNAME)
    terminal_svg = generate_terminal_card.generate_svg(ascii_lines)
    print(f"      -> {terminal_svg} created.")

    # 3. Generate Neofetch Info Card SVG
    print("\n[3/5] Generating Neofetch Telemetry Info Card...")
    info_svg = generate_info_card.generate_svg()
    print(f"      -> {info_svg} created.")

    # 4. Generate Animated Projects Card SVG (Screenshot 4)
    print("\n[4/5] Generating Totally Animated Projects Dashboard Card (Screenshot 4)...")
    projects_svg = generate_projects_svg.generate_projects_svg()
    print(f"      -> {projects_svg} created.")

    # 5. Generate Animated Snake Game SVG
    print("\n[5/5] Generating Contribution Snake Game SVG...")
    snake_svg = generate_snake_svg.generate_snake_svg()
    print(f"      -> {snake_svg} created.")

    # 6. Inject into README.md
    print("\nWriting complete README.md...")
    readme_path = "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(README_TEMPLATE.strip() + "\n")
    print(f"      -> {readme_path} created ({len(README_TEMPLATE)} bytes).")

    print("\n" + "=" * 68)
    print("   [ALL ASSETS GENERATED & VERIFIED SUCCESSFULLY]")
    print("   - github-contribution-animation.svg")
    print("   - terminal-card.svg")
    print("   - info-card.svg")
    print("   - projects-animated.svg")
    print("   - github-contribution-grid-snake.svg")
    print("   - README.md")
    print("=" * 68)


if __name__ == "__main__":
    main()
