
import turtle 
screen = turtle.Screen()  #creates the canvas we draw on.
screen.bgcolor("black")#background
screen.title("Neon Mandala") #title


pen = turtle.Turtle() #drawing pen
pen.speed("fastest")
pen.hideturtle() #hides the arrow


colors = ["white", "orange", "yellow", "cyan", "lime", "red", "pink", "white"]
for i in range(100): #repeats 100 times
    pen.color(colors[i % len(colors)]) #stands for modulus
    pen.width(2)
    pen.forward(i * 2)
    pen.right(91) #extra 1 for the drift

pen.penup() 
pen.goto(0, -80)
pen.setheading(90)
pen.pendown()
pen.color("yellow", "gold")
pen.begin_fill()
for i in range(10):
    pen.forward(140)
    pen.right(154)
pen.end_fill()

pen.penup()
pen.goto(0, 0)
pen.pendown()
petal_colors = ["cyan", "lime", "deeppink", "orange", "yellow"] 
for i in range(96):
    pen.color(petal_colors[i % len(petal_colors)],  #always used to make a clockwise circle using another shape 
                petal_colors[(i + 1) % len(petal_colors)])
    pen.begin_fill()
    for j in range(4):
        pen.forward(55)
        pen.right(90)
    pen.end_fill()
    pen.right(10)

# KEEP WINDOW OPEN
turtle.done()