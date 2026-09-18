import random
from turtle import Screen, Turtle


COLORS: tuple[str, ...] = ("red", "orange", "green", "blue", "purple")
Y_POSITIONS: tuple[int, ...] = (-80, -40, 0, 40, 80)


def create_racers() -> list[Turtle]:
    racers: list[Turtle] = []
    for color, y_position in zip(COLORS, Y_POSITIONS, strict=True):
        racer: Turtle = Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.goto(-230, y_position)
        racers.append(racer)
    return racers


def request_bet(screen: Screen) -> str | None:
    while True:
        bet: str | None = screen.textinput("Make your bet", f"Choose: {', '.join(COLORS)}")
        if bet is None:
            return None
        normalized: str = bet.strip().lower()
        if normalized in COLORS:
            return normalized


def race(racers: list[Turtle], randomizer: random.Random) -> str:
    while True:
        for racer in racers:
            racer.forward(randomizer.randint(1, 10))
            if racer.xcor() >= 230:
                return str(racer.pencolor())


def main() -> None:
    screen: Screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("Turtle Race")
    bet: str | None = request_bet(screen)
    if bet is None:
        screen.bye()
        return

    winner: str = race(create_racers(), random.Random())
    result: str = "You won!" if winner == bet else "You lost."
    screen.title(f"{result} The {winner} turtle won.")
    screen.exitonclick()


if __name__ == "__main__":
    main()
