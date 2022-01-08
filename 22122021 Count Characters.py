def count_chars(txt):
    '''Đếm ký tự trong chuỗi'''
    result = 0
    for char in txt:
        result += 1
    return result
if __name__=='__main__':
    input_text = input('Your text: ')
    print('Length: ', count_chars(input_text))
