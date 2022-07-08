pizza_topping = "\nWhat pizza topping would you like to add? "
pizza_topping += "\nEnter 'quit' if you don't want more toppings. "
message = ''
while message != 'quit':
    message = input(pizza_topping)
    if message == 'quit':
        print("Stop the program")
    else:
        print(f"{message} is added to your pizza.")
