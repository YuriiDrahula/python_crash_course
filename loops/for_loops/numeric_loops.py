# Counting to Twenty:
for i in range(1, 21):
    print(i)

# One Million
one_million = []
for num in range(1, 1_000_001):
    one_million.append(num)

print(min(one_million))
print(max(one_million))

print(sum(one_million))

# Odd numbers
for i in range(1, 21, 2):
    print(i)

# Threes
for i in range(3, 31, 3):
    print(i)

# Cubes
for i in range(1, 11):
    print(i**3)

# Cube comprehension
cube = [i**3 for i in range(1, 11)]
print(cube)
