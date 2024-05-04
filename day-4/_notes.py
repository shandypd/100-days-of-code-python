# Generate a random integer
import random
print(random.randint(1, 10))

# Generate a random float
print(random.random() * 5) # 0 to 5

# Create a module (module_example.py)
import module_example
print(module_example.name)

# Create a list
fruits = ["Apple", "Orange", "Lemon"]
print(fruits)

# Get an item from a list
print(fruits[0])

# Get the last item from a list
print(fruits[-1])

# Modify an item in a list
fruits[1] = "Banana"
print(fruits)

# Add a new item to a list
fruits.append("Watermelon")
print(fruits)

# Concatenate two lists
fruits.extend(["Melon", "Snakefruit"])
print(fruits)

# Get the length of a list
print(len(fruits))

# Split a string into a list
print("1,2,3,4,5".split(","))

# Nested list
vegetables = ["Spinach", "Kale", "Celery"]
food = [fruits, vegetables]
print(food)
