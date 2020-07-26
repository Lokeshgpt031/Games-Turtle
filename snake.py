import turtle
import time,random

delay = 0.1

score = 0
high_score = 0
win = turtle.Screen()
win.title('Snake Python')
win.bgcolor('black')
win.setup(width = 600,height = 600)
win.tracer(0)  # Turn off graphics

# Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'up'

# Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,-50)

segments = [ ]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write('Score:0 High Score:0',align = 'center',font = ('Courier New',24,'normal'))


def go_up ():
    if head.direction != 'down':
        head.direction = 'up'


def go_down ():
    if head.direction != 'up':
        head.direction = 'down'


def go_left ():
    if head.direction != 'right':
        head.direction = 'left'


def go_right ():
    if head.direction != 'left':
        head.direction = 'right'


def move ():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard Bindings()
win.listen()
win.onkeypress(go_up,'w')
win.onkeypress(go_right,'d')
win.onkeypress(go_down,'s')
win.onkeypress(go_left,'a')

while True:
    win.update()
    # Check for collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        print(f'Score: {len(segments)}')

        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        # Clear the segments
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f'Score:{score} High Score:{high_score}',align = 'center',font = ('Courier New',24,'normal'))

    if head.distance(food) < 20:
        # Move food to new position.
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        # Add segments in list
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape('square')
        new_segments.color('grey')
        new_segments.penup()
        segments.append(new_segments)
        # Shorten delay
        delay -= 0.005
        # Increasing scores
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f'Score:{score} High Score:{high_score}',align = 'center',font = ('Courier New',24,'normal'))

    for index in range(len(segments) - 1,0,-1):
        x = segments [ index - 1 ].xcor()
        y = segments [ index - 1 ].ycor()
        segments [ index ].goto(x,y)
    # Move segments zero

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments [ 0 ].goto(x,y)

    move()

    # Snake Collision Detection
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            # Hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            # Clear the segments
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f'Score:{score} High Score:{high_score}',align = 'center',font = ('Courier New',24,'normal'))

    time.sleep(delay)
    # print(segments)

win.mainloop()
