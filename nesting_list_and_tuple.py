animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cat = animals
large_cat.append("Tiger")
print(animals)

# To return different object after copying in python

animals = ['lion', 'tiger', 'frumious Bardersnatcch']
large_cat = animals[:]
large_cat.append("Monkey")
print(large_cat)
print(animals)

# Sorting list

colours = ['red', 'yellow', 'green', 'blue']
colours.sort()
print(colours)

numbers = [1, 10, 5, 8, 15, 20, 11]
numbers.sort()
print(numbers)


# Sorting string by string length
colours = ['red', 'yellow', 'green', 'blue']
colours.sort(key=len)
print(colours)