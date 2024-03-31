from turtle import Turtle
ALLIGMENT = "center"
FONT = ('Courier', 21, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score_file:
           self.high_score = int(score_file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align= ALLIGMENT, font= FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align= ALLIGMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

