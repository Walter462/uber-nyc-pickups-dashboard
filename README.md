# New York City Uber Driver — AI‑Powered Helper

🔗 **Live app:** [https://spotted-watery-tomorrow.anvil.app](https://spotted-watery-tomorrow.anvil.app)

An interactive analytics dashboard and LLM‑assisted helper for exploring historical Uber pickup density in **New York City**. The app helps drivers (and analysts) identify demand hotspots by hour and generate actionable recommendations using large language models.

---

## Overview

**Uber NYC Pickups Dashboard** is a lightweight prototype built in Python and Anvil. It combines:

* Historical pickup coordinate analysis
* An interactive, browser‑based dashboard
* Prompt templates for LLM‑powered hotspot interpretation

The goal is not to replace full‑scale mapping or dispatch systems, but to provide a **driver‑facing analytics assistant** and a **prompt toolkit** that can produce either:

* **Machine‑readable JSON** for downstream automation, or
* **Human‑readable recommendations** with clear reasoning.

**Status:** Prototype
**Tech stack:** Python · Anvil · LLMs

---

## Repository Structure

```
server_code/
├── prompts_lib.py        # LLM prompt templates for hotspot analysis
├── ServerModule1.py      # Backend logic and data handling

client_code/              # Client UI code and shared utilities

theme/                    # UI styling, themes, and templates
```

### Key Files

* **`server_code/prompts_lib.py`**
  Prompt templates used to ask an LLM to analyze pickup coordinates and identify demand hotspots. Supports multiple output formats:

  * `output='json'`
  * `output='txt'`

* **`server_code/ServerModule1.py`**
  Backend logic powering the dashboard and LLM interactions.

---

## Features

* 📊 **Hourly pickup density analysis** for New York City
* 🗺️ **Interactive map visualization** of pickup hotspots
* 🤖 **LLM‑powered recommendations** for drivers
* 📦 **Structured JSON output** for programmatic workflows
* 📝 **Readable text guidance** with street‑level prioritization
* 🪶 **Small, dependency‑light Python codebase**

---

## How to Use the Web App

1. **Open the app**
   Visit: [https://spotted-watery-tomorrow.anvil.app](https://spotted-watery-tomorrow.anvil.app)

2. **Sign up / log in**
   You may use any authentication method you prefer.
   <img src="/readme_src/Screenshot%202026-01-06%20at%2018.34.51-1.jpg" width="200" />
   *No ads, spam, or messaging — authentication is used only to protect AI resources from bots and abuse.*

3. **Explore pickup patterns**

   * Examine the **pickups‑per‑hour histogram**
   * Select an hour to visualize pickup density on the NYC map
   * Default view starts at **00:00 (midnight)**
   <img src="/readme_src/Screenshot%202026-01-06%20at%2018.40.37%20copy.png" width="600" />

4. **Customize the AI prompt**

   * Modify the user prompt text area to experiment with different GPT requests
  <img src="/readme_src/Screenshot%202026-01-06%20at%2018.43.10.png" width="1000"/>
5. **Choose response format**
  ![](/readme_src/Screenshot%202026-01-06%20at%2018.43.52.png)
   **Show API ready AI response**
   <img src="/readme_src/Screenshot%202026-01-06%20at%2018.56.35.png" width="250" />
   * Demonstrates an LLM response suitable for downstream processing
   * Can be used to generate new maps or points of interest programmatically

   **SUBMIT**
<img src="/readme_src/Screenshot%202026-01-06%20at%2018.56.52.png" width="250" />
   * Produces standard GPT‑formatted recommendations
   * Includes reasoning and prioritization helpful for drivers

6. **Analyze**
   Review hotspot suggestions and insights directly in the dashboard.

---

## Output Formats

The prompt toolkit supports two primary response modes:

* **`output='json'`**
  Enforces strictly valid JSON output, ideal for:

  * Automated pipelines
  * Map rendering
  * Further algorithmic processing
   <img src="/readme_src/Screenshot%202026-01-06%20at%2019.01.34.png" width="600" />

* **`output='txt'`**
  Produces clear, human‑friendly explanations, including:

  * Street‑level guidance
  * Priority reasoning
  * Contextual insights for drivers
   <img src="/readme_src/Screenshot%202026-01-06%20at%2019.01.10.png" width="600" />
---

## Intended Use Cases

* Uber or rideshare drivers seeking data‑driven positioning strategies
* Prototyping LLM‑assisted geospatial analytics
* Experimenting with prompt design for structured vs. narrative outputs
* Educational or exploratory data analysis projects

---

## Built With

* **[Anvil](https://anvil.works/?utm_source=github:app_README)** — full‑stack Python web framework
* Python, Pandas, NumPy — data handling, data manipulation, sorting backend logic, and prompt generation
* **OpenAI LLM** —  hotspot interpretation and recommendation generation

---

## Notes & Limitations

* This is a **prototype**, not a production dispatch or navigation system
* Pickup data is historical and may not reflect real‑time demand
* Recommendations should be treated as **decision support**, not guarantees

---

