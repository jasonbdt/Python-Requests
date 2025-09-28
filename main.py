import requests

URL_BASE = "https://learningserver.masterschool.com"

def send_get(url: str, params: dict[str, str]) -> str:
    return requests.get(URL_BASE+url, params).text


def send_post(url: str, data: dict[str, str]) -> str:
    return requests.post(URL_BASE+url, data).text


def get_user_input(prompt: str) -> str:
    return input(f"{prompt} ")


def main() -> None:
    # task1_params = {
    #     "name": get_user_input("Enter name:"),
    #     "color": get_user_input("Enter color:")
    # }
    # task1 = send_get("/http-basics/get-me", task1_params)
    # print(task1)

    task2_data = {
        "username": get_user_input("Enter Username:"),
        "password": get_user_input("Enter Password:")
    }
    task2 = send_post("/http-basics/post-me", task2_data)
    print(task2)

if __name__ == '__main__':
    main()
