#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import math
t=turtle.Turtle()
turtle.bgcolor('blue')
t.speed(9)
t.pensize(5)
#di chuyển rùa
t.penup()
t.goto(-240,40)
t.pendown()

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
t.fd(80)
t.rt(135)
t.fd(200)
t.rt(45)
t.fd(80)
t.rt(135)
t.fd(200)
t.end_fill()

#vẽ mái nhà
t.fillcolor('red')
t.begin_fill()
t.rt(20)
t.fd(100)
for i in range (2):
    t.lt(110)
    t.fd(330)
    t.lt(70)
    t.fd(100)
m = 90 + 40*math.sqrt(2)
n = 40 + 40*math.sqrt(2)
t.goto(m,n)
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
a = 90 + 10*math.sqrt(2)
b = 25
t.goto(a,b)
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
    c = 90 + 10*math.sqrt(2)
    d = -60
    t.goto(c,d)
    t.pendown()

#VẼ CÁI CÂY
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
#Tán lá 1
t.fillcolor('green')
t.begin_fill()
t.rt(90)
t.fd(65)
t.rt(150)
t.fd(60*math.sqrt(3))
t.rt(60)
t.fd(60*math.sqrt(3))
t.rt(150)
t.fd(115)
t.end_fill()
#Tán lá 2
t.penup()
t.goto(250,-90+30*math.sqrt(3))
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.fd(50)
t.rt(150)
t.fd(50*math.sqrt(3))
t.rt(60)
t.fd(50*math.sqrt(3))
t.rt(150)
t.fd(100)
t.end_fill()
#Tán lá 3
t.penup()
t.goto(250,-90+55*math.sqrt(3))
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.fd(35)
t.rt(150)
t.fd(40*math.sqrt(3))
t.rt(60)
t.fd(40*math.sqrt(3))
t.rt(150)
t.fd(85)
t.end_fill()
#Tán lá 4
t.penup()
t.goto(250,-90+75*math.sqrt(3))
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.fd(20)
t.rt(150)
t.fd(30*math.sqrt(3))
t.rt(60)
t.fd(30*math.sqrt(3))
t.rt(150)
t.fd(70)
t.end_fill()
#Tán lá 5
t.penup()
t.goto(250,-90+90*math.sqrt(3))
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.fd(5)
t.rt(150)
t.fd(20*math.sqrt(3))
t.rt(60)
t.fd(20*math.sqrt(3))
t.rt(150)
t.fd(55)
t.end_fill()

#VẼ MẶT TRỜI
t.penup()
t.goto(200,220)
t.pendown()
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

turtle.done()


# In[ ]:





# In[ ]:




