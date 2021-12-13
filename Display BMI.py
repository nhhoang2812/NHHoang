#!/usr/bin/env python
# coding: utf-8

# In[1]:


h = float(input("Chiều cao(m): "))
w = float(input("Cân nặng(kg): "))
bmi = round(w/(h**2), 2)
if bmi < 16: 
    print("BMI = "+str(bmi)+"\nGầy cấp độ III")
elif 16 <= bmi < 17:
    print("BMI = "+str(bmi)+"\nGầy cấp độ II")
elif 17<= bmi < 18.5:
    print("BMI = "+str(bmi)+"\nGầy cấp độ I")
elif 18.5 <= bmi < 25:
    print("BMI = "+str(bmi)+"\nBình thường")
elif 25 <= bmi < 30:
    print("BMI = "+str(bmi)+"\nThừa cân")
elif 30 <= bmi < 35:
    print("BMI = "+str(bmi)+"\nBéo phì cấp độ I")
elif 35 <= bmi < 40:
    print("BMI = "+str(bmi)+"\nBéo phì cấp độ II")
elif bmi > 40:
    print("BMI = "+str(bmi)+"\nBéo phì cấp độ III")

