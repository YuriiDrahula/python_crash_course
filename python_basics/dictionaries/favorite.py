favorite_places = {
    'Liza': ['Marocco', 'Livan', 'Butan'],
    'Bart': ['London', 'Paris', 'Madrid'],
    'Homer': ['bar', "comfortable"],
}

for names, places in favorite_places.items():
    print(f"{names}'s favorite places are:")
    for place in places:
        print(place)

favorite_numbers = {
    'Mike': [18, 15, 13],
    'Taras': [456, 654],
    'Ivan': [11, 111],
    'Kate': [56, 96]
}

for names, numbers in favorite_numbers.items():
    print(f"{names}' favorite numbers are")
    for number in numbers:
        print(f"{number}")

cities = {
    'Kyiv': {
        'country': "Ukraine",
        'population': '3 millions',
        'fact': 'fonded in V century'
    },
    'London': {
        'country': "England",
        'population': '7 millions',
        'fact': 'fonded in VII century'
    }
}

for keys, values in cities.items():
    print(keys + ':')
    for key, value in values.items():
        print(f"{key} - {value}")

