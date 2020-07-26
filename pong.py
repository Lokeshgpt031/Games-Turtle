import turtle,time

win = turtle.Screen()
win.title('Python Pong Game')
win.bgcolor('black')
win.setup(width = 800,height = 600)
win.tracer(0)
turtle.speed(speed=1)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle_B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize()
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)


def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


# Windows keyboard Bindings
win.listen()
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,'s')
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,'Down')


# print(paddle_a_up())
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.xcor()+ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>350:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor()<-350:
        ball.goto(0,0)
        ball.dx*=-1
    # paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
    time.sleep(0.01)