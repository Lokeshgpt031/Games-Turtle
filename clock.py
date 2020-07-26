import turtle
import time



tk = turtle.Turtle()

win = turtle.Screen()

score = 0
high_score = 0
win = turtle.Screen()
win.title('Snake Python')
win.bgcolor('black')
win.setup(width = 600,height = 600)
win.tracer(0)  # Turn off graphics


while True:
    a = (time.ctime(time.time()))

    tk.goto(0,0)
    tk.color('white')
    tk.clear()
    tk.write(a,align = 'center',font = ('Courier New',24,'normal'))

win.mainloop()

