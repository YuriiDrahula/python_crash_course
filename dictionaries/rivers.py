rivers = {
    'Dnipro': 'Ukraine',
    'Nile': 'Egypt',
    'Misisipi': 'USA',
    'Dunay': 'Hungary'
}

for key, value in rivers.items():
    print(f'The {key} runs through {value}.')

for country in rivers.values():
    print(f'\t{country}')

for river in rivers.keys():
    print(f'\t\t{river}')
