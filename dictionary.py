# Dictionary in python

capitals = {'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin', 'Colorado': 'Denver'}

# Iterate through the dict to get the key and value
for state in capitals:
    print(f"The Capital of {state} is {capitals[state]}")
# OR

for state, capital in capitals.items():
    print(f"The capital of {state} is {capital}")

# Checking if a key exists in a dict
if 'Arizona' in capitals:
    print("Found")
else:
    print("Not Found")

print(capitals.items())


# Review Challenge
captains = {}
captains ['Enterprise'] = 'Picard'
captains ['Voyage'] = 'Janeway'
captains ['Defiant'] = 'Sisko'

if 'Enterprise' in captains:
    print("Found")

if 'Discovery' in captains:
    print("Found")
else:
    print("Not Found")

for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")
