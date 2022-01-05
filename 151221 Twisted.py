#!/usr/bin/env python
# coding: utf-8

# In[2]:


import turtle
d = float(input("Nhập vào chiều dài của đường xoắn ốc: "))
t = turtle.Turtle()
t.hideturtle()
t.speed(20)
i = 0.02
while True:
    t.fd(i)
    t.lt(5)
    i+=0.02
    if d=0.02*i*(i-1): break
turtle.done()


# In[ ]:





# In[ ]:




