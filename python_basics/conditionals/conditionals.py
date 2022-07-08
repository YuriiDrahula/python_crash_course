car = 'audi'
if car == 'audi':
    print(f"{car.title()} is a good car.")

if car == 'lada':
    print(f'Omg, don\'t drive this car')

car = 'bmw'
if car == 'bmw':
    print(f'{car.upper()} is also a good one.')

cars = ['audi', 'bmw', 'lada', 'mercedes', 'dodge', 'ford']
for car in cars:
    if car == 'audi' or car == 'bmw' or car == 'mercedes':
        print(f'{car.title()} is a German car.')
    elif car == 'lada':
        print(f'{car.upper()} is a shit car, don\'t buy this!')
    else:
        print(f'{car.title()} is an American car.')

cars = ['audi', 'bmw', 'lada', 'mercedes', 'dodge', 'ford']
for car in cars:
    if car != 'chevrolett':
        print(f"This is not a Chevrolett, this is {car.title()}.")

age = 16
if age <= 18:
    print("He can't come in club.")

if age == 16:
    print("This guy is at 11th grade")

def reverse_seq(n):
    list = []
    for i in list(n, 0):
        return list.append(i)