from turtle import Turtle,Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


# setting up screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snakeyy")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# controls

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# creating snake


segments = []



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collisiom
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        game_is_on= False
        scoreboard.game_over()
        
        
    # detect collision with tail
    for segments in snake.segments:
        if segments==snake.head:
            pass
        elif snake.head.distance(segments)<10:
            game_is_on= False
            scoreboard.game_over()
    
    
    
    
    
screen.exitonclick()