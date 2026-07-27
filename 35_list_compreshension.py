# List comprehension = A concise way to create lists in Python
#                      Compact and easiert to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x*2)                                      # This can be easily written using list comprehension.

# print(doubles)

doubles = [x * 2 for x in range(1, 11)]

print(doubles)                                                 # List comprehension = A concise way to create lists in Python.

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]           # Same shit with some condition.

print(positive_nums)