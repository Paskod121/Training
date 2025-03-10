from turtle import *
bgcolor("black")
pencolor("Blue")
pensize(12)
fillcolor("red")
begin_fill()
speed(1)
for i in range(4):
    forward(100)
    left(90)
end_fill()

goto(100,100)
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
done()