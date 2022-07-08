glossary = {
    'while loop': 'is used to execute a block of statements repeatedly until a given condition is satisfied.',
    'for loops': 'are used for sequential traversal.',
    'conditional': 'is used for decision-making operations.',
    'sets': 'are used to store multiple items in a single variable',
    'tuples': 'are collections which are ordered and unchangeable.',
    'dictionaries': 'are used to store data values in key:value pairs.'
}


glossary.update({
    'lists': 'are used to store multiple items in a single variable.',
    'strings': 'strings in Python are arrays of bytes representing unicode characters.'
})

for key, value in glossary.items():
    print(f"{key.title()} - {value}")

