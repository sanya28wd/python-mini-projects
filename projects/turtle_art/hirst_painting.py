import random
from turtle import Screen, Turtle, colormode


PALETTE: tuple[tuple[int, int, int], ...] = (
    (202, 164, 109),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (145, 178, 148),
)


def draw_dot_grid(artist: Turtle, randomizer: random.Random, rows: int, columns: int) -> None:
    start_x: int = -225
    start_y: int = -225
    spacing: int = 50
    for row in range(rows):
        artist.goto(start_x, start_y + row * spacing)
        for _ in range(columns):
            artist.dot(20, randomizer.choice(PALETTE))
            artist.forward(spacing)


def main() -> None:
    colormode(255)
    artist: Turtle = Turtle()
    artist.speed("fastest")
    artist.penup()
    artist.hideturtle()
    draw_dot_grid(artist, random.Random(), 10, 10)
    screen: Screen = Screen()
    screen.title("Hirst-Style Dot Painting")
    screen.exitonclick()


if __name__ == "__main__":
    main()
