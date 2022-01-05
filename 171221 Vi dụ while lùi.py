#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 10
while True:
    if i==0: break
    else:
        print("*"*i)
        i=i-1
print("Ngoài vòng lặp while")


# In[4]:


i = 10
while i>0:
    print("*"*i)
    i=i-1
print("Ngoài vòng lặp while")


# In[8]:


try:
    i = int(input("Nhập vào chiều cao tam giác: "))
    while i>0:
        print("*"*i)
        i=i-1
    print("Ngoài vòng lặp while")
except: 
    print("Sai thông tin. Vui lòng nhập lại số nguyên.")
    


# In[ ]:




