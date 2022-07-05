pets = []

pet_1 = {
    'nickname': 'blacky',
    'type': 'dog',
    'age': 2,
    'favorite food': 'meat and bones'
}
pets.append(pet_1)

pet_2 = {
    'nickname': 'musya',
    'type': 'cat',
    'age': 3,
    'favorite food': 'fish and rats'
}
pets.append(pet_2)

pet_3 = {
    'nickname': 'yovji',
    'type': 'hengehog',
    'age': 1.5,
    'favorite food': 'bugs'
}
pets.append(pet_3)

for pet in pets:
    print(f"{pet['nickname'].title()} is a {pet['type']}. "
          f"It is {pet['age']} years old. {pet['nickname'].title()} likes {pet['favorite food']}.")

for pet in pets:
    print(f"I have such information about this pet:")
    for key, value in pet.items():
        if key == 'nickname':
            print(f"{key.title()} - {value.title()}")
        else:
            print(f"{key.title()} - {value}")