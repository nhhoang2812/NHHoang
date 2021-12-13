#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = float(input("Give me a price in total: "))
if num >= 150:
    print("Final payment: ", num - 50)
elif num >= 100:
    print("Final payment: ", num - 25)
elif num >= 75:
    print("Final payment: ", num - 15)
else:
    print("Final payment: ", num)


# In[ ]:




