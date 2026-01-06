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
   *No ads, spam, or messaging — authentication is used only to protect AI resources from bots and abuse.*

3. **Explore pickup patterns**

   * Examine the **pickups‑per‑hour histogram**
   * Select an hour to visualize pickup density on the NYC map
   * Default view starts at **00:00 (midnight)**

4. **Customize the AI prompt**

   * Modify the user prompt text area to experiment with different GPT requests

5. **Choose response format**

   **JSON (API‑ready)**

   * Demonstrates an LLM response suitable for downstream processing
   * Can be used to generate new maps or points of interest programmatically

   **Text (Human‑readable)**

   * Produces standard GPT‑formatted recommendations
   * Includes reasoning and prioritization helpful for drivers

6. **Submit and analyze**
   Review hotspot suggestions and insights directly in the dashboard.

---

## Output Formats

The prompt toolkit supports two primary response modes:

* **`output='json'`**
  Enforces strictly valid JSON output, ideal for:

  * Automated pipelines
  * Map rendering
  * Further algorithmic processing

* **`output='txt'`**
  Produces clear, human‑friendly explanations, including:

  * Street‑level guidance
  * Priority reasoning
  * Contextual insights for drivers

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
* **LLMs** — hotspot interpretation and recommendation generation

---

## Notes & Limitations

* This is a **prototype**, not a production dispatch or navigation system
* Pickup data is historical and may not reflect real‑time demand
* Recommendations should be treated as **decision support**, not guarantees

---

