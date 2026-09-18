import random
from typing import Literal


Difficulty = Literal["easy", "hard"]
ATTEMPTS: dict[Difficulty, int] = {"easy": 10, "hard": 5}


def request_difficulty() -> Difficulty:
    while True:
        choice: str = input("Choose easy or hard: ").strip().lower()
        if choice == "easy" or choice == "hard":
            return choice
        print("Enter 'easy' or 'hard'.")


def request_guess() -> int:
    while True:
        raw_guess: str = input("Your guess: ").strip()
        try:
            guess: int = int(raw_guess)
        except ValueError:
            print("Enter a whole number from 1 to 100.")
            continue
        if 1 <= guess <= 100:
            return guess
        print("Your guess must be from 1 to 100.")


def comparison_message(guess: int, answer: int) -> str:
    return "Too high." if guess > answer else "Too low."


def main() -> None:
    randomizer: random.Random = random.Random()
    answer: int = randomizer.randint(1, 100)
    difficulty: Difficulty = request_difficulty()

    print("I am thinking of a number from 1 to 100.")
    for remaining in range(ATTEMPTS[difficulty], 0, -1):
        print(f"Attempts remaining: {remaining}")
        guess: int = request_guess()
        if guess == answer:
            print(f"Correct! The number was {answer}.")
            return
        print(comparison_message(guess, answer))
    print(f"No attempts remain. The number was {answer}.")


if __name__ == "__main__":
    main()
