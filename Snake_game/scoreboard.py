from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color('white')
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align='center', font=("Courier", 24, 'normal'))


    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align='center', font=("Courier", 24, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align='center', font=("Courier", 24, 'normal'))

    def addscore(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score =0
        self.update_scoreboard()