# draw rainbow benzene
import turtle
colours = ["red", "purple", "green", "orange", "blue", ]
t = turtle.pen()
turtle.bicolor("black")
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(//100 + 1)
    t.forward(x)
    t.left(59)
 
