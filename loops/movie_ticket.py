while True:
    question = input("How old are you? ")
    if question == 'quit':
        break

    age = int(question)
    if age < 3:
        print("Ticket is free for you")
    elif 3 <= age < 12:
        print("Ticket costs 10$")
    elif age >= 12:
        print("Ticket costs 15$")