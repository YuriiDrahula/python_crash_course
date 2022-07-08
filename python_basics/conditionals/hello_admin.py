users_list = ['admin', 'Lorem', 'Ipsum']

# Hello admin
for user in users_list:
    if user == 'admin':
        print(f'Hello {user},would you like to see a status report!')
    else:
        print(f'Hello {user}, thank you for logging in again1')

# No users
if users_list:
    for user in users_list:
        print(f'Greeting {user}')
else:
    print('We need some users!')

# Checking Usernames
current_users = ['Calvin', 'Tommy', 'Johny', 'Dave', 'Mike']
new_users = ['Johny', 'Dave', 'Peter']

for user in new_users:
    if user in current_users:
        print(f'{user} has been already exited, please enter another name!')
    else:
        print(f'{user} is available username')

# Ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
