
edibles = {
    "food": "Rice",
    "drink": "Water",
    "vegetable": "Spinach",
    "fruits": "Apple",
    "snack": "Meat Pie",

}

print(edibles)
print(edibles.get("food"))  # Get the value of a key
print(edibles.keys())  # Return the keys in the dictionary
print(edibles.values())  # Return the values in the dictionary
edibles.pop("fruits")  # To remove a key from a dictionary
print(edibles)
edibles.update({"fruits": "Banana", "drink": "Fresh Juice"})
print(edibles)
