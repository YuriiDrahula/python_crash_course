car = input("What car do yo want to rent? ")
print(f"Let me see if I can find you a {car}")

people = int(input("How many people are in your dinner group? "))
if people > 8:
    print("You have to wait for a table")
else:
    print("Your table is ready!")

number = int(input("Tell me any number "))
if number % 10 == 0:
    print(f"The {number} is multiply of 10")
else:
    print(f"The {number} isn't multiply on 10")