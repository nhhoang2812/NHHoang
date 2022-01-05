Num_Start=int(input('Type start number: '))
Num_End=int(input('Type end number: '))
while Num_Start>Num_End:
    print('Start number must be smaller than End number.\nPlease type again!')
    Num_Start=int(input('Type start number: '))
    Num_End=int(input('Type end number: '))
else:
    for i in range (Num_Start-1, Num_End+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else: print(i)
