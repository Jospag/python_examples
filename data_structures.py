numbers = (1, 2, 3, 4, 5)
squares = [num**2 for num in numbers]
print(squares)

squares = []
for num in numbers:
    squares.append(num**2)
print(squares)

str_numbers = ["1.5", "2.3", "5.25"]
float_numbers = [float(value) for value in str_numbers]
print(float_numbers)