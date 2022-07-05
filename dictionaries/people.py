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