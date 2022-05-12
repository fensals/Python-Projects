from turtle import Turtle


FONT = ('Arial', 10, 'bold')
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
