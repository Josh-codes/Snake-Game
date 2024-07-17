from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#screen setup
screen = Screen()
screen.setup(width=450, height=450)
screen.bgcolor("light green")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key= "Up", fun= snake.up)
screen.onkey(key = "Down", fun= snake.down)
screen.onkey(key = "Left", fun= snake.left)
screen.onkey(key = "Right", fun= snake.right)

game_is_on = True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
                food.refresh()
                scoreboard.score_incrementer()
                snake.extend()

        if snake.head.xcor() > 220 or snake.head.xcor() < -225 or snake.head.ycor() > 220 or snake.head.ycor() < -220:
                game_is_on = False
                scoreboard.game_over()

        for segment in snake.segments[1:]:
               if snake.head.distance(segment) < 10:
                        game_is_on = False
                        scoreboard.game_over()

screen.exitonclick()