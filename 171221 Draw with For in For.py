import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Star")

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

for j in range (1,100):
    for i in range (1,6):
        myPen.left(144)
        myPen.forward(200)
    myPen.left(5)

turtle.done()