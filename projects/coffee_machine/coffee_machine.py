from typing import TypedDict


class Recipe(TypedDict):
    ingredients: dict[str, int]
    cost: float


MENU: dict[str, Recipe] = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}
INITIAL_RESOURCES: dict[str, int] = {"water": 300, "milk": 200, "coffee": 100}
COIN_VALUES: dict[str, float] = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def missing_resource(resources: dict[str, int], ingredients: dict[str, int]) -> str | None:
    for ingredient, required in ingredients.items():
        if resources.get(ingredient, 0) < required:
            return ingredient
    return None


def deduct_resources(resources: dict[str, int], ingredients: dict[str, int]) -> dict[str, int]:
    return {
        ingredient: available - ingredients.get(ingredient, 0)
        for ingredient, available in resources.items()
    }


def read_non_negative_integer(prompt: str) -> int:
    while True:
        raw_value: str = input(prompt).strip()
        try:
            value: int = int(raw_value)
        except ValueError:
            print("Enter a whole number.")
            continue
        if value >= 0:
            return value
        print("Enter zero or a positive number.")


def collect_payment() -> float:
    total: float = 0.0
    print("Insert coins.")
    for coin_name, coin_value in COIN_VALUES.items():
        total += read_non_negative_integer(f"How many {coin_name}? ") * coin_value
    return round(total, 2)


def print_report(resources: dict[str, int], profit: float) -> None:
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${profit:.2f}")


def main() -> None:
    resources: dict[str, int] = dict(INITIAL_RESOURCES)
    profit: float = 0.0

    while True:
        choice: str = input("Choose espresso, latte, cappuccino, report, or off: ").strip().lower()
        if choice == "off":
            return
        if choice == "report":
            print_report(resources, profit)
            continue
        if choice not in MENU:
            print("Unknown selection.")
            continue

        recipe: Recipe = MENU[choice]
        unavailable: str | None = missing_resource(resources, recipe["ingredients"])
        if unavailable is not None:
            print(f"There is not enough {unavailable}.")
            continue

        payment: float = collect_payment()
        if payment < recipe["cost"]:
            print("Insufficient payment. Money refunded.")
            continue

        resources = deduct_resources(resources, recipe["ingredients"])
        profit += recipe["cost"]
        print(f"Change: ${payment - recipe['cost']:.2f}")
        print(f"Here is your {choice}. Enjoy!")


if __name__ == "__main__":
    main()
