from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = "0"
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.update_highscore()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} \t\t High Score: {self.high_score}", False, align="center", font=('', 20, ''))

    def reset_game(self):
        if self.score > int(self.high_score):

            with open("/Users/kevin/PycharmProjects/Snake/data.txt", mode="w") as file:
                file.write(str(self.score))

            self.high_score = self.score
        self.score = 0
        self.update_score()
        self.update_highscore()

    def update_highscore(self):
        with open("/Users/kevin/PycharmProjects/Snake/data.txt") as file:
            self.high_score = file.read()
