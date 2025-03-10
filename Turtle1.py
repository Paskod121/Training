from turtle import *
color(red)
begin_fill()
while true :
    forward(200)
    left(170)
    if abs(pos()) !=1:
        break
end_fill()
done()