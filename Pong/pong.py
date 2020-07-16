# Pong game


import turtle
import time

# Global Variables

paused = 0

# Dimensions of Window

width = 800
height = 600

# Turtle screen boundaries allow for some bottom offset from expected pixel output.
# This is fixed by adding the following when needed

bottom_offset = 10


# Pause Menu

def select(x, y):
    global paused, current_time
    if -60 < x < 60 and (height / 2) - 140 < y < (height / 2) - 100:
        paused = 0
        current_time = time.time()
        return
    elif -60 < x < 60 and (height / 2) - 200 < y < (height / 2) - 160:
        wn.bye()
        return
    else:
        return


def pause():
    global paused, paddle_a, paddle_b, ball
    paused = 1

    paddle_a.hideturtle()
    paddle_b.hideturtle()
    ball.hideturtle()

    pause_pen = turtle.Turtle()
    pause_pen.hideturtle()
    pause_pen.pencolor("white")
    pause_pen.fillcolor("#000000")
    pause_pen.penup()
    pause_pen.begin_fill()
    pause_pen.begin_poly()
    pause_pen.goto(- (width / 2), - (height / 2))
    pause_pen.goto(width / 2, - (height / 2))
    pause_pen.goto(width / 2, height / 2)
    pause_pen.goto(- (width / 2), height / 2)
    pause_pen.end_poly()
    pause_pen.end_fill()

    pause_pen.goto(0, (height / 2) - 60)
    pause_pen.write("PONG", align="center", font=("Courier", 24, "bold"))
    pause_pen.goto(0, (height / 2) - 120)
    pause_pen.write("Resume", align="center", font=("Courier", 24, "normal"))
    pause_pen.goto(0, (height / 2) - 180)
    pause_pen.write("Quit", align="center", font=("Courier", 24, "normal"))
    pause_pen.penup()

    wn.listen()
    wn.onclick(select)

    while paused:
        wn.update()

    wn.onclick(None)
    pause_pen.clear()
    paddle_a.showturtle()
    paddle_b.showturtle()
    ball.showturtle()


# Start Menu

def start():
    global paused
    paused = 1

    pause_pen = turtle.Turtle()
    pause_pen.hideturtle()
    pause_pen.pencolor("white")
    pause_pen.penup()

    pause_pen.goto(0, (height / 2) - 60)
    pause_pen.write("PONG", align="center", font=("Courier", 24, "bold"))
    pause_pen.goto(0, (height / 2) - 120)
    pause_pen.write("Start", align="center", font=("Courier", 24, "normal"))
    pause_pen.goto(0, (height / 2) - 180)
    pause_pen.write("Quit", align="center", font=("Courier", 24, "normal"))

    wn.listen()
    wn.onclick(select)

    while paused:
        wn.update()

    wn.onclick(None)
    pause_pen.clear()


# Game Function

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
        pen.goto(0, (height / 2) - 60)
        pen.write("Player A: {}  Player B: {}".format(paddle_a.score, paddle_b.score), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
    elif ball.xcor() + ball.dx <= - (width / 2) + 10:
        ball.dx *= -1
        paddle_b.score += 1
        pen.clear()
        pen.goto(0, (height / 2) - 60)
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


# Movement Functions

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


# FPS System

current_frame = 0
fps = 20000000
current_time = 0


def tick(fps_requested=60):
    global current_frame, fps, current_time
    n = fps / fps_requested
    current_frame += n
    while n > 0:
        if not paused:
            n -= 1
    if time.time() - current_time > 1:
        current_time = time.time()
        fps = current_frame
        current_frame = 0


wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0)

# Start Game

start()

# Score Print

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, (height / 2) - 60)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

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

# Key Binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(pause, "Escape")

# Game loop

while True:
    tick(120)
    game()
    if paddle_a.score == 10 or paddle_b.score == 10:
        break
