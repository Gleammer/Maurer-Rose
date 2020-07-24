import math
import turtle as tr

screen = tr.Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor('#000')
pen = tr.Turtle()
pen.speed(0)
tr.ht()
#tr.tracer(0)

#n = int(input("n = "))
n = 6
#d = int(input("d = "))
d = 71

pen.color('blue')
pen.pensize(0.5)
for theta in range(361):
    k = theta * d * math.pi / 180
    r = 300 * math.sin(n * k)
    x = r * math.cos(k)
    y = r * math.sin(k)
    pen.goto(x, y)

pen.color('red')
pen.pensize(4)
for theta in range(361):
    k = theta * math.pi / 180
    r = 300 * math.sin(n * k)
    x = r * math.cos(k)
    y = r * math.sin(k)
    pen.goto(x, y)


tr.done()
