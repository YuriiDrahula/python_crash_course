# Person
person = {
    'first name': 'Johny',
    'last name': 'Depp',
    'age': 51,
    'city': 'Hollywood'
}

print(f"{person['first name']} {person['last name']}, {person['age']}, {person['city']}.")

# Favorite numbers
favorite_numbers = {
    'Dave': 7,
    'Liza': 14,
    'Bart': 99,
    'Homer': 8,
    'Tilda': 54
}

for key, value in favorite_numbers.items():
    print(f"{key}'s favorite number is {value}")

