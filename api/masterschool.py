import requests

API_BASE = "https://learningserver.masterschool.com"

def task1(name: str, color: str) -> str:
    params: dict[str, str] = {
        "name": name,
        "color": color
    }
    res = requests.get(f"{API_BASE}/http-basics/get-me", params)

    return res.text

def task2(username: str, password: str) -> str:
    data: dict[str, str] = {
        "username": username,
        "password": password
    }
    res = requests.post(f"{API_BASE}/http-basics/post-me", data)

    return res.text
