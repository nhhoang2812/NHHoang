def add_item(Expenditure, item):
    '''Thêm mục chi tiêu mới vào danh sách'''  
    Expenditure.append(item)

def find_item(Expenditure, item_name):
    '''Tìm mục chi tiêu trong danh sách'''
    result = -1
    length = len(Expenditure)
    for i in range(length):
        if Expenditure[i]['name'] == item_name:
            result = i
    return result

def remove_item(Expenditure, item_name):
    '''Xóa mục chi tiêu trong dánh sách'''
    if find_item(Expenditure, item_name) > -1:
        del Expenditure[find_item(Expenditure, item_name)]
    else:
        print(item_name + " not in list")

if __name__=='__main__':
    Expenditure=[]
    while True:
        print("What do you want to do? -\n"\
            "1. Add\n" \
            "2. Remove")
        option = int(input("Select option 1 or 2: "))
        name_input = input("Item name: ")
        if option == 1:
            cost_input = int(input("Item cost: "))
            date_input = input("Date: ")
            item = {'name': name_input, 'cost':str(cost_input)+'USD', 'date':date_input}
            add_item(Expenditure, item)
            print("Your expenses: ", Expenditure)
        elif option == 2:
            find_item(Expenditure, name_input)
            remove_item(Expenditure, name_input)
            print("Your expenses: ", Expenditure)
        else:
            print("Invalid input")