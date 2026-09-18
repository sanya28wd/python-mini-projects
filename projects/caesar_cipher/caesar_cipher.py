from typing import Literal


Mode = Literal["encode", "decode"]
ALPHABET_SIZE: int = 26


def shift_character(character: str, shift: int) -> str:
    if not character.isascii() or not character.isalpha():
        return character
    alphabet_start: int = ord("A") if character.isupper() else ord("a")
    position: int = ord(character) - alphabet_start
    return chr(alphabet_start + (position + shift) % ALPHABET_SIZE)


def transform(text: str, shift: int, mode: Mode) -> str:
    signed_shift: int = shift if mode == "encode" else -shift
    return "".join(shift_character(character, signed_shift) for character in text)


def request_mode() -> Mode:
    while True:
        mode: str = input("Encode or decode? ").strip().lower()
        if mode == "encode" or mode == "decode":
            return mode
        print("Enter 'encode' or 'decode'.")


def request_shift() -> int:
    while True:
        raw_shift: str = input("Shift amount: ").strip()
        try:
            return int(raw_shift)
        except ValueError:
            print("Enter a whole number.")


def main() -> None:
    print("Caesar Cipher")
    while True:
        mode: Mode = request_mode()
        text: str = input("Message: ")
        shift: int = request_shift()
        print(transform(text, shift, mode))
        if input("Process another message? (y/n): ").strip().lower() != "y":
            return


if __name__ == "__main__":
    main()
