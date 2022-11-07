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