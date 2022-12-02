grocery_list:dict = {}
while True:
    item_name = str(input("Type item name or leave empty to exit: "))
    if item_name == '':
        break
    price = float(input('Type a price: '))
    grocery_list[item_name] = price

print(grocery_list)