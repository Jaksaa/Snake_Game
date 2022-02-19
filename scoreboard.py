from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.high_score = 0
        self.eat_dot = 0

    def tracking_score(self):
        self.clear()
        self.goto(0,260)
        with open("snake_high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(arg=(f"Score: {self.eat_dot} High score: {self.high_score}"),move=False, align="center", font=('Arial', 20, 'bold'))

    def reset(self):
        if self.eat_dot > self.high_score:
            self.high_score = self.eat_dot
            with open("snake_high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=("Game over."), move=False, align="center", font=('Arial', 26, 'bold'))