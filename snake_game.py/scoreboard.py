from turtle import Turtle
Alignment = "center"
Font = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/umakantmanore/Desktop/amu/practice/snake_game.py/data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align= Alignment, font = Font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/Users/umakantmanore/Desktop/amu/practice/snake_game.py/data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= Alignment, font = Font)

    def increase_score(self):
        self.score += 1
        self.update()