import random

from words import WORDS


STAGES: tuple[str, ...] = (
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
)


def render_word(word: str, guesses: set[str]) -> str:
    return " ".join(letter if letter in guesses else "_" for letter in word)


def request_letter() -> str:
    while True:
        guess: str = input("Guess a letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Enter exactly one letter.")


def main() -> None:
    randomizer: random.Random = random.Random()
    word: str = randomizer.choice(WORDS)
    guesses: set[str] = set()
    mistakes: int = 0

    print("Hangman")
    while mistakes < len(STAGES) - 1:
        print(STAGES[mistakes])
        print(render_word(word, guesses))
        if all(letter in guesses for letter in word):
            print("You win!")
            return

        guess: str = request_letter()
        if guess in guesses:
            print("You already guessed that letter.")
            continue
        guesses = guesses | {guess}
        if guess not in word:
            mistakes += 1
            print(f"No '{guess}' in the word.")

    print(STAGES[mistakes])
    print(f"You lose. The word was '{word}'.")


if __name__ == "__main__":
    main()
