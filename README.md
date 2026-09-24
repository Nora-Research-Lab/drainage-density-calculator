![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Drainage Density Calculator
 
*For geomorphologists and hydrologists: enter watershed area and total stream length to instantly compute drainage density and classify the landscape as low, medium, or high drainage texture.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geomorphology
 
Inputs: (1) Watershed area in square kilometers (km²) — numeric float input with a label 'Watershed Area (km²)'. (2) Total stream length in kilometers (km) — numeric float input with a label 'Total Stream Length (km)'. The core calculation: Drainage Density (Dd) = Total Stream Length / Watershed Area (km/km²). The tool then classifies Dd using standard geomorphic thresholds: Dd < 1.0 km/km² → 'Low drainage density (coarse texture)'; 1.0 ≤ Dd ≤ 3.0 km/km² → 'Medium drainage density (moderate texture)'; Dd > 3.0 km/km² → 'High drainage density (fine texture)'. The Gradio UI consists of: a row with two number inputs side by side, a 'Calculate Drainage Density' button beneath, and an output area showing the computed Dd value (with two decimal places) and the classification text. No chart or file output is needed; the result is displayed as a formatted number and color-coded classification (green for low, yellow for medium, red for high). There is no AI/ML component — it is a pure domain calculation. No data persists; the tool is stateless. Input validation: both values must be positive numbers; if zero or negative, show an error message. The UI is clean, with a header and brief instructions.
 
## Run it
 
```bash
docker build -t drainage-density-calculator .
docker run -p 7860:7860 drainage-density-calculator
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
 
Built 2026-09-24.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
