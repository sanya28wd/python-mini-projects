import random
from collections.abc import Sequence


DECK: tuple[int, ...] = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)


def deal_card(randomizer: random.Random) -> int:
    return randomizer.choice(DECK)


def calculate_score(cards: Sequence[int]) -> int:
    total: int = sum(cards)
    aces: int = cards.count(11)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def is_blackjack(cards: Sequence[int]) -> bool:
    return len(cards) == 2 and calculate_score(cards) == 21


def compare_hands(player: Sequence[int], dealer: Sequence[int]) -> str:
    player_score: int = calculate_score(player)
    dealer_score: int = calculate_score(dealer)
    if is_blackjack(player) and not is_blackjack(dealer):
        return "Blackjack! You win."
    if is_blackjack(dealer) and not is_blackjack(player):
        return "The dealer has Blackjack. You lose."
    if player_score > 21:
        return "You went over 21. You lose."
    if dealer_score > 21:
        return "The dealer went over 21. You win."
    if player_score == dealer_score:
        return "Draw."
    return "You win." if player_score > dealer_score else "You lose."


def request_choice(prompt: str, choices: set[str]) -> str:
    while True:
        choice: str = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Choose one of: {', '.join(sorted(choices))}.")


def play_round(randomizer: random.Random) -> None:
    player: list[int] = [deal_card(randomizer), deal_card(randomizer)]
    dealer: list[int] = [deal_card(randomizer), deal_card(randomizer)]

    while calculate_score(player) < 21:
        print(f"Your cards: {player} (score: {calculate_score(player)})")
        print(f"Dealer's visible card: {dealer[0]}")
        if request_choice("Draw another card? (y/n): ", {"y", "n"}) == "n":
            break
        player = [*player, deal_card(randomizer)]

    while calculate_score(dealer) < 17:
        dealer = [*dealer, deal_card(randomizer)]

    print(f"Your final hand: {player} (score: {calculate_score(player)})")
    print(f"Dealer's final hand: {dealer} (score: {calculate_score(dealer)})")
    print(compare_hands(player, dealer))


def main() -> None:
    randomizer: random.Random = random.Random()
    print("Blackjack")
    while request_choice("Play a round? (y/n): ", {"y", "n"}) == "y":
        play_round(randomizer)


if __name__ == "__main__":
    main()
