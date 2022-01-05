#!/usr/bin/env python
# coding: utf-8

# In[1]:

import turtle
screen = turtle.Screen()

# Hàm vẽ elip
def draw(rad):
    k=0
    while k<2:
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)
        k+=1
 
screen.setup(500,500)
screen.bgcolor('black')

# Màu
mau=['red','orange','yellow','green','blue','indigo','violet']
 
val=10
ind=0
i=0
 
turtle.speed(100)
 
while i<36:
     
    # xoay hướng elip
    turtle.seth(-val)
     
    # màu elip
    turtle.color(mau[ind])
     
    if ind==6:
        ind=0
    else:
        ind+=1
    # Vẽ elip
    draw(80)
    
    val+=10
    i+=1
 
turtle.hideturtle()
turtle.exitonclick()


# In[ ]:




