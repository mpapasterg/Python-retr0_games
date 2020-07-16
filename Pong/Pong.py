# Pong game


import turtle
import time


# FPS System

current_frame = 0
fps = 20000000
current_time = time.time()


def tick(fps_requested=60):
    global current_frame, fps, current_time
    n = fps / fps_requested
    current_frame += n
    while n > 0:
        n -= 1
    if time.time() - current_time > 1:
        current_time = time.time()
        fps = current_frame
        current_frame = 0


# Dimensions of Window

width = 800
height = 600

# Turtle screen boundaries allow for some bottom offset from expected pixel output.
# This is fixed by adding the following when needed
bottom_offset = 10

wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0)

# Score Print

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (height / 2) - 60)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "bold"))

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(- (width / 2) + 40, 0)
paddle_a.score = 0

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto((width / 2) - 40, 0)
paddle_b.score = 0

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = width / 1000
ball.dy = height / 1000


# Functions

def paddle_a_up():
    if paddle_a.ycor() >= (height / 2) - 80:
        return
    else:
        paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    if paddle_a.ycor() <= - (height / 2) + 80:
        return
    else:
        paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    if paddle_b.ycor() >= (height / 2) - 80:
        return
    else:
        paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    if paddle_b.ycor() <= - (height / 2) + 80:
        return
    else:
        paddle_b.sety(paddle_b.ycor() - 20)


# Key Binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(wn.bye, "Escape")


def game():
    wn.update()

    if ball.ycor() + ball.dy >= (height / 2) - 10:
        ball.sety((height / 2) - 10)
        ball.dy *= -1
    elif ball.ycor() + ball.dy <= - (height / 2) + 10 + bottom_offset:
        ball.sety(- (height / 2) + 10 + bottom_offset)
        ball.dy *= -1
    else:
        ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() + ball.dx >= (width / 2) - 10:
        ball.dx *= -1
        paddle_a.score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(paddle_a.score, paddle_b.score), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
    elif ball.xcor() + ball.dx <= - (width / 2) + 10:
        ball.dx *= -1
        paddle_b.score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(paddle_a.score, paddle_b.score), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
    elif ball.xcor() + ball.dx >= paddle_b.xcor() - 20 \
            and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(paddle_b.xcor() - 20)
        ball.dx *= -1
    elif ball.xcor() + ball.dx <= paddle_a.xcor() + 20 \
            and paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(paddle_a.xcor() + 20)
        ball.dx *= -1
    else:
        ball.setx(ball.xcor() + ball.dx)


# Game loop

while True:
    tick(120)
    game()
    if paddle_a.score == 10 or paddle_b.score == 10:
        break
