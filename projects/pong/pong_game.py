import time
from turtle import Screen, Turtle


SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
PADDLE_X: int = 350
PADDLE_STEP: int = 25
FRAME_DELAY: float = 0.03


class Paddle(Turtle):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self) -> None:
        self.sety(min(self.ycor() + PADDLE_STEP, 250))

    def move_down(self) -> None:
        self.sety(max(self.ycor() - PADDLE_STEP, -250))


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_velocity: float = 6.0
        self.y_velocity: float = 6.0

    def move(self) -> None:
        self.goto(self.xcor() + self.x_velocity, self.ycor() + self.y_velocity)

    def bounce_vertical(self) -> None:
        self.y_velocity *= -1

    def bounce_horizontal(self) -> None:
        self.x_velocity *= -1.05

    def reset_after_score(self, direction: int) -> None:
        self.goto(0, 0)
        self.x_velocity = 6.0 * direction
        self.y_velocity = 6.0


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 245)

    def display(self, left_score: int, right_score: int) -> None:
        self.clear()
        self.write(
            f"{left_score}     {right_score}",
            align="center",
            font=("Courier", 28, "normal"),
        )


def configure_screen() -> Screen:
    screen: Screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    return screen


def hits_paddle(ball: Ball, paddle: Paddle) -> bool:
    horizontal_distance: float = abs(ball.xcor() - paddle.xcor())
    vertical_distance: float = abs(ball.ycor() - paddle.ycor())
    return horizontal_distance < 25 and vertical_distance < 60


def main() -> None:
    screen: Screen = configure_screen()
    left_paddle: Paddle = Paddle((-PADDLE_X, 0))
    right_paddle: Paddle = Paddle((PADDLE_X, 0))
    ball: Ball = Ball()
    scoreboard: Scoreboard = Scoreboard()
    left_score: int = 0
    right_score: int = 0
    scoreboard.display(left_score, right_score)

    screen.listen()
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")

    while True:
        time.sleep(FRAME_DELAY)
        ball.move()

        if abs(ball.ycor()) >= 285:
            ball.bounce_vertical()
        if (ball.x_velocity < 0 and hits_paddle(ball, left_paddle)) or (
            ball.x_velocity > 0 and hits_paddle(ball, right_paddle)
        ):
            ball.bounce_horizontal()
        if ball.xcor() > 400:
            left_score += 1
            scoreboard.display(left_score, right_score)
            ball.reset_after_score(-1)
        elif ball.xcor() < -400:
            right_score += 1
            scoreboard.display(left_score, right_score)
            ball.reset_after_score(1)

        screen.update()


if __name__ == "__main__":
    main()
