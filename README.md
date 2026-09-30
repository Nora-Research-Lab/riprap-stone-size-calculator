![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Riprap Stone Size Calculator
 
*For construction geologists and civil engineers: enter flow velocity, bank slope angle, and rock density to instantly compute the required median stone diameter (D50) for riprap erosion protection using the Isbash equation.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Construction / Infrastructure Geology
 
Inputs: (1) Flow velocity (m/s or ft/s, user-selectable via radio button), default 3 m/s, range 0.5–10 m/s; (2) Bank slope angle (degrees), default 30°, range 0–60°; (3) Rock density (kg/m³ or lb/ft³, matching velocity unit), default 2650 kg/m³; (4) Safety factor (unitless), default 1.2, range 1.0–2.0. The core calculation uses the Isbash equation: D50 = (V² × SF) / (2 × g × (Sr − 1) × cos(θ)), where V = flow velocity, SF = safety factor, g = 9.81 m/s² or 32.174 ft/s², Sr = specific gravity of rock (rock density / water density), θ = bank slope angle in radians. Water density is 1000 kg/m³ or 62.4 lb/ft³. The output D50 is computed in meters and then converted to millimeters and inches. A classification table is applied: D50 < 150 mm → 'Small riprap (fine gravel)'; 150–300 mm → 'Medium riprap'; 300–500 mm → 'Large riprap'; > 500 mm → 'Very large riprap (boulders)'. The Gradio UI displays four input components (number input or slider for velocity, slider for slope, number input for density, slider for safety factor, and a radio button for unit system). A 'Calculate' button triggers the computation. Outputs: (a) a numeric display showing D50 in mm and inches, (b) a text display of the classification, and (c) a bar chart comparing the computed D50 against the three classification thresholds (150, 300, 500 mm) with color-coded bars (green if safe, red if exceeds threshold). No AI/ML component is used; the tool is purely deterministic.
 
## Run it
 
```bash
docker build -t riprap-stone-size-calculator .
docker run -p 7860:7860 riprap-stone-size-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-30.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
