# return = statement used to end a function
#          and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return (first + " " + last)
    # print(f"Hello {first} {last}")

first = input("Enter your first name: ")
last = input("Enter your last name: ")
print(create_name(first, last))
# full_name = create_name("krish", "lODHA")

# print(create_name)

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1, 2))
print(multiply(1,2))
print(divide(1, 2))