from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("white")
        # self.write(f"SCORE: {self.score}",align="center",font=("Arial",24,"normal"))
        self.update_score()
        
    def update_score(self):
        self.write(f"SCORE: {self.score}",align="center",font=("Arial",24,"normal"))
        
            
        
        
    def increase_score(self):
        self.score +=1
        self.write(f"SCORE: {self.score}",align="center",font=("Courier",24,"normal"))
        self.clear()
        self.update_score()
        
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Courier",24,"normal"))
        
        
        
        