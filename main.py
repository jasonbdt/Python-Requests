from api import *


def get_user_input(prompt: str) -> str:
    return input(f"{prompt} ")


def main() -> None:
    # name = get_user_input("Enter name:")
    # color = get_user_input("Enter color:")
    # print(task1(name, color))

    # username = get_user_input("Enter Username:")
    # password = get_user_input("Enter Password:")
    # print(task2(username, password))

    meal_name = get_user_input("Enter meal name:")
    meal_info = get_meal(meal_name)
    print(meal_info)

if __name__ == '__main__':
    main()
