people = []

person_1 = {
    'first name': 'Johny',
    'last name': 'Depp',
    'age': 51,
    'city': 'Hollywood'
}
people.append(person_1)

person_2 = {
    'first name': 'Angelina',
    'last name': 'Jolie',
    'age': 46,
    'city': 'Hollywood'
}
people.append(person_2)

person_3 = {
    'first name': 'Brad',
    'last name': 'Pitt',
    'age': 53,
    'city': 'California'
}
people.append(person_3)

for person in people:
    name = f"{person['first name']} {person['last name']}"
    age = person['age']
    city = person['city']
    if name == 'Angelina Jolie':
        print(f"{name} is {age} years old. She lives in {city}")
    else:
        print(f"{name} is {age} years old. He is from {city}")




favorite_numbers_1 = {
    'Dave': 7,
    'Liza': 14,
    'Bart': 99,
    'Homer': 8,
    'Tilda': 54
}

favorite_numbers_2 = {
    'Mike': 22,
    'Taras': 34,
    'Ivan': 45,
    'Kate': 68
}

favorite_numbers_3 = {
    'Mike': 18,
    'Taras': 456,
    'Ivan': 11,
    'Kate': 56
}

list_of_people = [favorite_numbers_1, favorite_numbers_2, favorite_numbers_3]

for people in list_of_people:
    for name, favorite_number in people.items():
        print(f"{name}'s favorite number is {favorite_number}.")