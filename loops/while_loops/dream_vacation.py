active_poll = True
dream_vacation = {}

while active_poll:
    name = input("What's your name? ")
    vacation_place = input("Where would you like to spend your vacation? ")
    dream_vacation[name] = vacation_place

    repeat = input("Would you like to let another person respond. (yes/no) ")
    if repeat == 'no':
        active_poll = False

for name, vacation in dream_vacation.items():
    print(f"{name} would like to spend his vacation in {vacation}.")
