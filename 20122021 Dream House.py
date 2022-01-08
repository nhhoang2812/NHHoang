import turtle
import math
t=turtle.Turtle()
turtle.bgcolor('aquamarine')
t.speed(9)
t.pensize(5)
can2 = math.sqrt(2)
can3 = math.sqrt(3)
t.penup()
t.goto(-240,40)
t.pendown()

def House():
    '''VẼ NGÔI NHÀ'''
    #vẽ 2 mặt ngôi nhà
    t.fillcolor('grey')
    t.begin_fill()
    for i in range (2):
        t.fd(330)
        t.rt(90)
        t.fd(200)
        t.rt(90)
    t.goto(90,40)
    t.lt(45)
    for i in range (2):
        t.fd(80)
        t.rt(135)
        t.fd(200)
        t.rt(45)
    t.end_fill()
    #vẽ mái nhà
    t.fillcolor('red')
    t.begin_fill()
    t.lt(25)
    t.fd(100)
    for i in range (2):
        t.lt(110)
        t.fd(330)
        t.lt(70)
        t.fd(100)
    t.goto(90+40*can2,40+40*can2)
    t.end_fill()
    t.lt(20)
    t.pensize(3)
    #vẽ cửa ra vào
    t.penup()
    t.goto(15,-160)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range (2):
        t.fd(90)
        t.lt(90)
        t.fd(180)
        t.lt(90)
    t.end_fill()
    #vẽ cửa sổ mặt trước
    t.penup()
    t.home()
    t.goto(0,10)
    t.pendown()
    for k in range (3):
        t.fillcolor('white')
        t.begin_fill()
        for i in range (2):
            t.fd(70)
            t.rt(90)
            t.fd(30)
            t.rt(90)
        t.end_fill()
        t.penup()
        t.fd(-110)
        t.pendown()
    #vẽ cửa sổ mặt bên
    t.penup()
    t.goto(90+10*can2,25)
    t.lt(45)
    t.pendown()
    for k in range (2):
        t.fillcolor('white')
        t.begin_fill()
        for i in range(2):
            t.fd(40)
            t.rt(135)
            t.fd(60)
            t.rt(45)
        t.fd(20)
        t.rt(135)
        t.fd(60)
        t.end_fill()
        t.lt(135)
        t.penup()
        t.goto(90+10*can2,-60)
        t.pendown()

def Tree():
    '''VẼ CÁI CÂY'''
    #Thân cây
    t.penup()
    t.goto(250,-90)
    t.rt(135)
    t.pendown()
    t.fillcolor('brown')
    t.begin_fill()
    for i in range (2):
        t.fd(70)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.end_fill()
    #Tán lá
    t.rt(90)
    for l in range (5):
        t.fillcolor('green')
        t.begin_fill()
        t.fd(65-15*l)
        t.rt(150)
        t.fd((60-10*l)*can3)
        t.rt(60)
        t.fd((60-10*l)*can3)
        t.rt(150)
        t.fd(115-15*l)
        t.end_fill()
        t.penup()
        m=5*(6-l/2)*(l+1)
        t.goto(250,-90+m*can3)
        t.pendown()

def Sun():
    '''VẼ MẶT TRỜI'''
    t.penup()
    t.goto(200,220)
    t.pendown()
    t.pencolor('orange')
    for i in range (4):
        t.fd(120)
        t.fd(-120)
        t.rt(90)
    t.rt(45)
    for i in range (4):
        t.fd(90)
        t.fd(-90)
        t.rt(90)
    t.penup()
    t.rt(45)
    t.fd(60)
    t.lt(90)
    t.pendown()
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(60)
    t.end_fill()

if __name__=='__main__':
    House()
    Tree()
    Sun()
    turtle.done()
