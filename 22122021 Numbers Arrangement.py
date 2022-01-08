def num_arrange(num1, num2, num3):
    '''Sắp xếp các số nguyên theo thứ tự từ bé đến lớn'''
    temp=0
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    return num1, num2, num3
if __name__=='__main__':
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    z = int(input('Enter third number: '))
    a,b,c = num_arrange(x,y,z)
    print("Initial Sort: ", x, y, z)
    print("After being sorted: ", a, b, c)