# Create a dictionary
dict = {"a": 1, "b": 2}

# Get a value from a dictionary
print(dict["a"])

# Add a new item to a dictionary
dict["c"] = 3
print(dict["c"])

# Loop through a dictionary
for key in dict:
    print(f"key={key}, value={dict[key]}")

# Nesting
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
print(travel_log[0]["country"])
