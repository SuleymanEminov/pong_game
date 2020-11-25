import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# Coordinates for left paddle
LEFT_SIDE = (-350, 0)
RIGHT_SIDE = (350, 0)

# flag for the game
game_is_on = True


screen = Screen()

# Screen settings
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# State machine to track which keys are pressed
keys_pressed = {}


def main():
    # Create objects
    left_paddle = Paddle(LEFT_SIDE)
    right_paddle = Paddle(RIGHT_SIDE)
    ball = Ball()
    scoreboard = Scoreboard()
    scoreboard.update_scoreboard()

    # Game loop
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Check state of key presses and respond accordingly
        if keys_pressed["w"]:
            if left_paddle.ycor() < 350: left_paddle.go_up()
        if keys_pressed["s"]:
            if left_paddle.ycor() > -350: left_paddle.go_down()
        if keys_pressed["Up"]:
            if right_paddle.ycor() < 350: right_paddle.go_up()
        if keys_pressed["Down"]:
            if right_paddle.ycor() > -350: right_paddle.go_down()

        # Detect collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect if the ball is out of screen
        # reset the positions of ball and paddles
        if ball.xcor() > 380:
            left_paddle.reset_position(LEFT_SIDE)
            right_paddle.reset_position(RIGHT_SIDE)
            ball.reset_position()
            scoreboard.l_point()
            scoreboard.update_scoreboard()

        # Detect if the ball is out of screen
        # reset the positions of ball and paddles
        if ball.xcor() < -380:
            left_paddle.reset_position(LEFT_SIDE)
            right_paddle.reset_position(RIGHT_SIDE)
            ball.reset_position()
            scoreboard.r_point()
            scoreboard.update_scoreboard()


# Callback for KeyPress event listener. Sets key pressed state to True
def pressed(event):
    keys_pressed[event.keysym] = True


# Callback for KeyRelease event listener. Sets key pressed state to False
def released(event):
    keys_pressed[event.keysym] = False


# Setup the event listeners, bypassing the Turtle Screen to use the underlying TKinter canvas directly
# This needs to be done to get access to the event object so the state machine can determine which key was pressed
def set_key_binds():
    for key in ["Up", "Down", "w", "s"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


screen.listen()
set_key_binds()

main()

screen.exitonclick()








