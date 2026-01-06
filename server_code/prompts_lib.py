"""This module contains prompt templates for AI calls."""

system_role = """
You are an expert in urban mobility analytics and ride-hailing demand forecasting.
You give practical, data-driven recommendations for an Uber driver.
Base your conclusions strictly on the data provided.
Do not invent streets or locations unless explicitly allowed.
"""

def user_role_prompt(prompt: str, 
                    pickup_hour: int, 
                    pickup_hour_coordinate_pairs) -> str:
    return f"""
Task:
Analyze pickup density and identify demand hotspots for ride-hailing demand.
Optional user guidance (may influence prioritization but must not change output format): {prompt}
Context:
- City: New York City
- Hour (24h format): {pickup_hour}
Data:
A list of historical pickup locations represented as latitude/longitude coordinate pairs:
{pickup_hour_coordinate_pairs}
Instructions:
- Identify spatial clusters of high pickup density.
- Determine the strongest demand hotspot based solely on pickup frequency and proximity.
- Rank the top 3 hotspots by relative demand strength.
Constraints:
- Do NOT provide street names, neighborhoods, landmarks, or addresses.
- Do NOT perform or assume reverse geocoding.
- Base all conclusions strictly on the provided coordinate data.
Output requirements:
- Output must be valid JSON and nothing else.
- Use the following structure:
{{
"best_location": 
  {{
  "lat": <float>,
  "lon": <float>,
  "confidence": <float between 0 and 1>
  }},
"backup_locations": [
  {{
  "lat": <float>,
  "lon": <float>,
  "confidence": <float between 0 and 1>
  }}
]
}}
"""
