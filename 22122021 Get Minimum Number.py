numbers = [25, 29, 66, 22, 45, 33, 3]

def get_min_num(numbers):
    '''Tìm giá trị nhỏ nhất trong danh sách'''
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

if __name__=='__main__':
    min_num=get_min_num(numbers)
    print('Minimum number is:',min_num)