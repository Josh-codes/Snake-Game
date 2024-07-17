from turtle import Screen, Turtle
from snake import Snake
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key= "Up", fun= snake.up)
screen.onkey(key = "Down", fun= snake.down)
screen.onkey(key = "Left", fun= snake.left)
screen.onkey(key = "Right", fun= snake.right)
# Movement of snake body
game_is_on = True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()




screen.exitonclick()