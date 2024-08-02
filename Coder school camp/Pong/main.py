import turtle

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(700, 600)

leftPaddle = turtle.Turtle()
leftPaddle.penup()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=6, stretch_len=1)
leftPaddle.goto(-300, 0)

rightPaddle = turtle.Turtle()
rightPaddle.penup()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=6, stretch_len=1)
rightPaddle.goto(300,0)

ball_speed = 5

ball = turtle.Turtle()
ball.penup()
ball.speed(1000)
ball.shape("circle")
ball.color("white")
ball.goto(0,0)
ball.dx = ball_speed
ball.dy = -(ball_speed)

left_player = 0
right_player = 0

score = turtle.Turtle()
score.penup()
score.speed(0)
score.color("white")
score.hideturtle()
score.goto(0,250)
score.write("Left Player: 0      Right Player: 0", align="center", font=("Courier", 24, "normal"))

def leftPaddleUp():
    leftPaddle.sety(leftPaddle.ycor() + 40)
def leftPaddleDown():
    leftPaddle.sety(leftPaddle.ycor() - 40)

def rightPaddleUp():
    rightPaddle.sety(rightPaddle.ycor() + 40)
def rightPaddleDown():
    rightPaddle.sety(rightPaddle.ycor() - 40)

def move_ball():
    screen.update()
    global left_player, right_player

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.dy *= -1

    if (ball.xcor() < -280 and ball.xcor() > -300) and (ball.ycor() < leftPaddle.ycor() + 60 and ball.ycor() > leftPaddle.ycor() - 60):
        ball.dx *= -1
    elif (ball.xcor() > 280 and ball.xcor() < 300) and (ball.ycor() < rightPaddle.ycor() + 60 and ball.ycor() > rightPaddle.ycor() - 60):
        ball.dx *= -1

    if ball.xcor() < -350:
        right_player += 1
        score.clear()
        score.write("Left Player: {}      Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() > 350:
        left_player += 1
        score.clear()
        score.write("Left Player: {}      Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    screen.ontimer(move_ball, 20)

move_ball()

screen.tracer(0)
screen.onkey(leftPaddleUp, "w")
screen.onkey(leftPaddleDown, "s")
screen.onkey(rightPaddleUp, "Up")
screen.onkey(rightPaddleDown, "Down")
screen.listen()

turtle.mainloop()