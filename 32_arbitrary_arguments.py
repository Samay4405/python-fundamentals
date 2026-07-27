# *args     = allows you to pass multiple non-key arguments
# ** kwargs = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY

#*args

# def add(a, b):
#     return a + b                                         # In these cases, we can't pass multiple arguments(more than defined)
#                                                          # So to avoid this we use **kwargs
# print(add(1, 2, 3))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 8))                                     # Here we can add as many arguments as we want.

# And with parameter *args we can change the name...
# FOR example
# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1))                                            This will work too...

print()

# example
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
