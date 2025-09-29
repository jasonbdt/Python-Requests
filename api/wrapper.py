import requests
from typing import Any

API_BASE = "https://www.themealdb.com/api/json/v1/1"

def get_meal(meal_name: str) -> dict[str, Any]:
    return requests.get(f"{API_BASE}/search.php", {
        "s": meal_name
    }).json()
