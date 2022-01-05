#!/usr/bin/env python
# coding: utf-8

# In[1]:


def greet(name,counter):
    return f"Hi, {name}!", counter + 1
if __name__ == "__main__":
   counter = 0
   greeting,counter = greet("Alice",counter)
   print(f"{greeting}\n Counter is {counter}")
   greeting,counter = greet("Bob",counter)
   print(f"{greeting}\n Counter is {counter}")


# In[3]:


def greet(name,counter):
    return f"Hi, {name}!", counter + 1
if __name__ == "__main__":
   counter = 0
   print(greet("Alice",counter))
   print(f"Counter is {counter}")
   print(greet("Bob",counter))
   print(f"Counter is {counter}")


# In[ ]:




