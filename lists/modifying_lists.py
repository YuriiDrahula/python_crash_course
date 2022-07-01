friends = ['Vasya', 'Vanya', 'Petrik']
print(f'I would like to invite {len(friends)} friends for the dinner')
print(f"I would like to invite you, {friends[0]}, to the dinner.")
print(f"I would like to invite you, {friends[1]}, to the dinner.")
print(f"I would like to invite you, {friends[2]}, to the dinner.")

print(f'{friends[0]} and {friends[2]}, can\'t come for the dinner')
del friends[0]
friends.append('Igor')
friends[1] = 'Sasha'

print(f"I would like to invite you, {friends[0]}, to the dinner.")
print(f"I would like to invite you, {friends[1]}, to the dinner.")
print(f"I would like to invite you, {friends[2]}, to the dinner.")

print('I just fond a bigger table for our dinner and would invite 3 more friends')
friends.insert(0, 'Misha')
friends.insert(2, 'Yura')
friends.append('Mikey')
print(f'{len(friends)} friends are invited for the dinner')
print(f'So, at our dinner will be {friends[0]}, {friends[1]}, {friends[2]}, '
      f'{friends[3]}, {friends[-2]}, {friends[-1]}.')

print("My new dinner table won't arrive in the time, so I have space only for 2 guests!")

name_1 = friends.pop(0)
name_2 = friends.pop(1)
name_3 = friends.pop(2)
name_4 = friends.pop(1)
unlucky_friends = [name_1, name_2, name_3, name_4]
print(unlucky_friends)

print(f'{friends[0]} and {friends[1]}, you are still invited to the dinner!')

del friends[0]
del friends[0]

print(friends)
