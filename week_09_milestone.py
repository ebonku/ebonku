print('Welcome to the Shopping program.')
print()
print('Please select one of the following:')
print('1. Add item')
print('2. View cart')
print('3. Remove item')
print('4. Compute total')
print('5. Quit ')
items = []
option = ''
option = int(input('Enter an option: '))
while option != 5:
    if option == 1:
        ask_item = input('What item will you want to add? ')
        items.append(ask_item)
        ask_price = float(input(f'What is the price {ask_item}? '))
        print(f'{ask_item.capitalize()} has been added to the cart.')
    elif option == 2:
        print(*items, sep='\n')
    elif option == 3:
        print('item has been removed')
    elif option == 4:
        print('computing total...')
    else:
         print('Invalid option')
    option = int(input('Enter an option: '))
if option == 5:
    print('Thank you for using our shopping program. Goodbye')
