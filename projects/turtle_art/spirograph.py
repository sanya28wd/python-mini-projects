import colorsys
from turtle import Screen, Turtle, colormode


def rgb_color(index: int, total: int) -> tuple[int, int, int]:
    red, green, blue = colorsys.hsv_to_rgb(index / total, 0.75, 0.95)
    return int(red * 255), int(green * 255), int(blue * 255)


def draw_spirograph(artist: Turtle, circles: int, radius: int) -> None:
    angle: float = 360 / circles
    for index in range(circles):
        artist.pencolor(rgb_color(index, circles))
        artist.circle(radius)
        artist.setheading(artist.heading() + angle)


def main() -> None:
    colormode(255)
    artist: Turtle = Turtle()
    artist.speed("fastest")
    artist.pensize(2)
    draw_spirograph(artist, 60, 100)
    screen: Screen = Screen()
    screen.title("Spirograph")
    screen.exitonclick()


if __name__ == "__main__":
    main()
