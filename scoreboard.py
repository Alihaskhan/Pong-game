from turtle import Turtle
ALIGN = "center"
FONT = ("Courier" , 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(100, 230)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.color("red")
        self.write(f"GAME OVER", align=ALIGN,font =('Courier', 50, 'normal') )
