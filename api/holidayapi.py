from typing import Any
import requests


API_BASE = "https://holidayapi.com/v1"
API_KEY = "69bf2d9b-7fd2-42ee-93a4-c9df84ea2714"


def get_available_countries() -> tuple[dict[str, Any], int]:
    res = requests.get(f"{API_BASE}/countries", {
        "key": API_KEY
    }).json()["countries"]

    return res, len(res)


def get_holidays(country_code: str, year: int) -> tuple[dict[str, Any], int]:
    res = requests.get(f"{API_BASE}/holidays", {
        "country": country_code,
        "key": API_KEY,
        "year": year
    }).json()["holidays"]

    return res, len(res)
