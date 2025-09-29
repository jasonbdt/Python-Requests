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
    meals = get_meals(meal_name)
    meals_len = len(meals)
    print(f"We found {meals_len} meal(s):\n")

    for meal_info in meals:
        print(
            f" {meal_info["strMeal"]} ".center(40, "*"),
            f"\nCategory: {meal_info["strCategory"]}"
            f"\nArea: {meal_info["strArea"]}"
            f"\nInstructions:"
            f"\n{meal_info["strInstructions"]}"
        )

if __name__ == '__main__':
    main()
