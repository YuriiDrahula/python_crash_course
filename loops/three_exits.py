message = ''
while message != 'quit':
    message = input(f"Enter any text"
                    f"\nIf you enter 'quit', the program will stop. ")
    if message != 'quit':
        print(f"I'll print entered word upercase, look: "
              f"{message.upper()}!!!")

active = True
while active:
    message = input(f"Enter any text: ")

    if message == 'quit':
        active = False
    else:
        print(f"Your text is: '{message}'")

while True:
    message = input(f"Enter any text: ")

    if message == 'quit':
        break
    else:
        print(f"drdrdr here is your word back - {message}")