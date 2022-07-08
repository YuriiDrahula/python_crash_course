countries = ['USA', 'Spain', 'England', 'Italy']
countries.insert(2, 'Ukraine')
countries.append('Norway')
countries.remove('Italy')
countries.pop(3)
countries.sort()
print(f'I want to visit {len(countries)}, they are {countries[0]},'
      f' {countries[1]}, {countries[2]} and {countries[3]}')

countries.reverse()
print(f'{countries[0]} is the best on whole world!')