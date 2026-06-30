import json
import re


def parse_json(text: str):
    if not text:
        raise ValueError("Received empty response from planner")

    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text, flags=re.IGNORECASE)

    return json.loads(text.strip())