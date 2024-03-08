from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score.update_scoreboard()

game_is_on = True
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.addscore()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        score.reset_score()
        snake.reset()


    #Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            score.reset_score()
            snake.reset()

