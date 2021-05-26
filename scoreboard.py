from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../Desktop/highscore.txt") as f:
            self.highscore = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        with open("../../Desktop/highscore.txt","w") as f:
            f.write(f"{self.highscore}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("game over", align=ALIGN, font=FONT)

