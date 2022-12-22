# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
def shopping_cart():
    x = {}

    while True:
        cart=input('What do you want to do? Show/Add/Remove/Quit')
        if cart.lower() == "quit":
            print('Thanks for coming into the store! ')
            print(f'This is your cart! {x}')
            break
            
        elif cart.lower() == "add":
            item = input ('What is your item you want to add to your cart?')
            quanity = input (f'How many {item} do you want to add to your cart? ')
            x[item] = quanity
            
        elif cart.lower() == "show":
            print(f'These are the items in your cart {x}')
        
        elif cart.lower() == "remove":
            y = input(f'What item from your cart do you want to remove {x} hit enter to remove! ')
            x.pop(input("item: ")) 

        else:
            print('Invalid input!')  
        
    return
shopping_cart()

