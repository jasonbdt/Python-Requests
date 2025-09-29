from typing import Any
from api import *


def get_user_input(prompt: str) -> str:
    return input(f"{prompt} ")


def display_meal_info(meals: dict[str, Any]) -> None:
    for meal_info in meals:
        print(f" MEAL START ".center(40, "*"))
        print(
            f" {meal_info["strMeal"]} ".center(40, "*"),
            f"\nCategory: {meal_info["strCategory"]}"
            f"\nArea: {meal_info["strArea"]}"
            f"\nInstructions:"
            f"\n{meal_info["strInstructions"]}\n",
        )
        print(f" MEAL END ".center(40, "*"), "\n")


def main() -> None:
    # name = get_user_input("Enter name:")
    # color = get_user_input("Enter color:")
    # print(task1(name, color))

    # username = get_user_input("Enter Username:")
    # password = get_user_input("Enter Password:")
    # print(task2(username, password))

    meal_name = get_user_input("Enter meal name:")
    meals, meals_len = get_meals(meal_name)
    print(f"We found {meals_len} meal(s):")
    display_meal_info(meals)

if __name__ == '__main__':
    main()
