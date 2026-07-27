# Create a list of numbers from 1 to 20 and filter out even numbers using list comprehension.

numbers = [i for i in range(1, 21) if i % 2 != 0]
print(numbers)