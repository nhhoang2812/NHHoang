import turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor('red')
def square(w):
    for i in range(4):
        t.forward(w)
        t.right(90)
    turtle.done()
if __name__=='__main__':
    square(100)