def multitable():
    for i in range(1,10):
        for number in range(1,10):
            print(str(i)+' x '+str(number)+' = '+ str(i*number))
if __name__=='__main__':
    multitable()