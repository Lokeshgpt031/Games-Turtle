import turtle,time


win = turtle.Screen()
win.bgcolor('black')
win.setup(600,600)
win.title('Analog Clock')
win.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def drawClock(pen=pen,h=0,m=0,s=0):
    # drawClock()
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color('green')
    pen.pendown()
    pen.circle(210)

    # lines of hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    # hours hand
    pen.penup()
    pen.goto(0,0)
    pen.color('white')
    pen.setheading(90)
    angle = (h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)
 # Minutes hand
    pen.penup()
    pen.goto(0,0)
    pen.color('blue')
    pen.setheading(90)
    angle = (m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(140)
 # Seconds hand
    pen.penup()
    pen.goto(0,0)
    pen.color('orange')
    pen.setheading(90)
    angle = (s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

while True:
    h=int(time.strftime('%I'))
    m=int(time.strftime('%M'))
    s=int(time.strftime('%S'))
    t=time.strftime('%T')
    d=time.strftime('%d %b %Y')
    am=time.strftime('%p')
    pen.penup()
    pen.goto(0,100)
    pen.pendown()
    pen.color('white')
    pen.write(t,align = 'Center',font = ('Arial Black',20))
    pen.penup()
    pen.goto(0,-100)
    pen.pendown()
    pen.write(d,align = 'Center',font = ('Arial Black',20))
    # print(h,m,s)
    pen.penup()
    pen.goto(0,50)
    pen.pendown()
    pen.write(am,align = 'Center',font = ('Arial Black',20))

    win.update()
    time.sleep(1)
    pen.clear()
    drawClock(pen,h,m,s)
win.mainloop()