# Slices
places_to_visit = ['Madrid', 'New York', 'Barcelona', 'Rome', 'London', 'Paris', 'Kyiv', 'Riga', 'Amsterdam']
print(f"The first three cities in the list are \n {places_to_visit[:3]}")
print(f"The cities from the middle of the list are \n {places_to_visit[3:7]}")
print(f"The last three cities from the list are \n {places_to_visit[-3:]}")

# My Pizzas, Your Pizzas
favorite_pizza = ['4 cheeses', 'meat pizza', 'margarita', 'pepperoni']
friends_pizza = favorite_pizza[:]
favorite_pizza.append('barbecue')
friends_pizza.append('napolitanna')
print(f"My favorite pizzas are: \n {favorite_pizza}")
print(f"My friends favorite pizzas are \n {friends_pizza}")

# More loops
for pizza in favorite_pizza:
    print(pizza)
for pizza in friends_pizza:
    print(pizza)
