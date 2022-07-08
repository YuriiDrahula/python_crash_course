# Deli
sandwich_orders = ['filadelfia', 'california', 'taxes', 'deli']
finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I finished your {made_sandwich} sandwich.")
    finished_sandwiches.append(made_sandwich)

print(f"Today I made such sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")

# No pastrami
sandwich_orders = ['filadelfia', 'pastrami', 'california', 'pastrami', 'taxes', 'deli', 'pastrami']
print("The deli is coming out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

