# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr. ", "Spongebob", "Squarepants")                       # Here order matters cause we r using positional arguments.
# hello("Hello", title="Mr.", last="Squarepants", first="Spongebob")     # Here order doesn't matter as we are using keyword arguments.
                                                                         # But positional arguments should be followed by keyword arguments. Else it will show error.
                                                                         
print()

for x in range(1, 11):
    print(x, end=" ")                                                    # end is a keyword argument found within builtin print statements.

print("1", "2","3", "4", "55", sep="-")


print()
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)