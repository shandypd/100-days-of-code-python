# Define a function with parameters
def greet(greeting, name):
    print(f"{greeting}, {name}!")


# Execute a function with positional arguments
greet("Hello", "Kai")
greet("Nice to see you", "Jack")

# Execute a function with keyword arguments
greet(name="Bob", greeting="Hi")
