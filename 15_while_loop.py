# WHile Loop = Execute some code while some conditons remain true.

# food = input("Enter a food you like: (q to quit):")
# while not food == "q":
#    food = input("Enter another food u like: (q to quit):")
    
# print("bye")


name = input("Enter your name:")

while name == "":
    print("You did not enter your name")
    name = input("Please enter your name:")
    
print(f"Hello, {name}")