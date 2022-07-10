# Message
def display_message():
    print("I'm learning functions in this chapter")

display_message()

# Favorite book
def favourite_book(title):
    print(f"One of my favorite books is {title}")

favourite_book("Harry Potter")

# T-shirt
def make_shirt(size, text):
    print(f"The size of this shirt is {size}. "
          f"There is the '{text}' printed on it.")

make_shirt("XL", "I'm Ukrainian!")
make_shirt(size='M', text="Fuck Russian warship")

# Large shirts
def make_large_shirts(size='XL', text='I love Python'):
    print(f"These shirts are {size} size. "
          f"There is the '{text}' printed on it.")

make_large_shirts()

def make_medium_shirts(size='M', text='Programming is funny!'):
    print(f"These shirts are {size} size. "
          f"There is the '{text}' printed on it.")

make_medium_shirts()

def make_any_shirt(any_size, any_text):
    print(f"These shirts can be {any_size}. "
          f"You can print '{any_text}' on it.")

make_any_shirt('any size', 'any_text')

# Cities
def describe_city(city, country='Ukrainian'):
    print(f"{city} is {country} city.")

describe_city("Khrarkiv")
describe_city("Kherson")
describe_city("Donetsk")



