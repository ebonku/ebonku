print('Welcome to the Shopping program.')
print()
print('Please select one of the following:')
print('1. Add item')
print('2. View cart')
print('3. Remove item')
print('4. Compute total')
print('5. Quit ')

print()
ask_item = ''
items = []
option = ''
option = int(input('Enter an option: '))
contents = ['bed', 'chair', 'blanket']
print()
while option != 5:
    if option == 1:
        ask_item = input('What item will you want to add? ')
        if ask_item != 5:
            items.append(ask_item)
        ask_price = float(input(f'What is the price {ask_item}? '))
        
        print(f'{ask_item.capitalize()} has been added to the cart.')
    

        print()
    elif option == 2:
        print(f'The contents of the shopping cart are:')
        for content in contents:
            print(content)
           
    
    elif option == 3:
        print('item has been removed')
    
    elif option == 4:
        print('computing total...')
    
    else:
         print('Invalid option')

    print()
    option = int(input('Enter an option: '))

if option == 5:
    print('Thank you for using our shopping program. Goodbye')
