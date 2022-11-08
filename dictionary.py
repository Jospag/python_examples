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