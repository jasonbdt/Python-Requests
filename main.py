import requests

URL_BASE = "https://learningserver.masterschool.com"

def send_get(url: str, params: dict[str, str]) -> str:
    res = requests.get(URL_BASE+url, params)
    return res.text


def get_user_input(prompt: str) -> str:
    return input(f"{prompt} ")


def main() -> None:
    task1_params = {
        "name": get_user_input("Enter name:"),
        "color": get_user_input("Enter color:")
    }
    task1 = send_get("/http-basics/get-me", task1_params)
    print(task1)

if __name__ == '__main__':
    main()
