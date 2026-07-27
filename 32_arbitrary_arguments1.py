# *args     = allows you to pass multiple non-key arguments
# ** kwargs = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY

#  ** kwargs

def print_address( ** kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
                apt="100",
                city="Detroit",
                state="MI",
                zip="54321")

print()

#Example

def shipping_label(*args, ** kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")  # Here apt will display none as their is no input.              # for value in kwargs.values():
    print(f"{kwargs.get('city')} {kwargs.get('state')},{kwargs.get('zip')}")                                              #     print(value, end=" ")
                                                                              
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
                street="123 Fake St.",
                apt="100",
                city="Detroit",
                state="MI",
                zip="54321")