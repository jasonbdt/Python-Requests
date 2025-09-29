from typing import Any
from datetime import datetime
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


def display_countries(countries: dict[str, Any]) -> None:
    print("Available Countries:\n")
    for country in countries:
        print(f"({country['codes']['alpha-2']}) {country['name']}")
    print()


def display_holidays(holidays: dict[str, Any], year: int) -> None:
    print(f"List of holidays in the last year ({year}):")
    for holiday in holidays:
        date_obj = datetime.fromisoformat(holiday['date'])
        date_lst = date_obj.strftime("%A,%B,%d").split(',')
        weekday, month, day = date_lst
        suffix = (
            "st" if day.endswith("1") else
            "nd" if day.endswith("2") else
            "rd" if day.endswith("3") else "th"
        )
        print(f"{holiday['name']} ({weekday}, {month} {day}{suffix})")
    print()


def main() -> None:
    # name = get_user_input("Enter name:")
    # color = get_user_input("Enter color:")
    # print(task1(name, color))

    # username = get_user_input("Enter Username:")
    # password = get_user_input("Enter Password:")
    # print(task2(username, password))

    # meal_name = get_user_input("Enter meal name:")
    # meals, meals_len = get_meals(meal_name)
    # print(f"We found {meals_len} meal(s):")
    # display_meal_info(meals)

    last_year = datetime.now().year - 1
    countries, countries_len = get_available_countries()
    display_countries(countries)

    country_code = get_user_input("Enter Country (two-letter code):").upper()
    holidays, holidays_len = get_holidays(country_code, last_year)
    display_holidays(holidays, last_year)

if __name__ == '__main__':
    main()
