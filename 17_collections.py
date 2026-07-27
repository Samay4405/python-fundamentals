# Collection = single 'variable' used to store multiple values.
# List = [] ordered and changeble. Duplicates OK.
# Set = {} unordered and immutable(unchangeble), but add/remove OK. No Duplicates.
# Tuples = {} ordered and unchangeble. Duplicates OK. FASTER.
# Dictionary = { : } 

fruits = ["apple", "orange", "Banana", "Grape"]
# print(fruits)
# print(fruits[0])
# print(fruits[3])
# print(fruits[0:3])
# print(fruits[::-1])
# print(len(fruits))

for x in fruits:
    print(x)
print()

    
print("apple" in fruits)
print("pineapple" in fruits)

print()

fruits.append("kiwi")                     # To add in the list.

print()

print(fruits)

print()

fruits.remove("Banana")                  # To remove from the list.
fruits[0] = "pineapple"                  # To change from the list.
fruits.insert(0, "PEru")                 # To insert
fruits.sort()                            # Sorts in ascending order
fruits.reverse()                         # Sorts in descending order
fruits.pop(0) 

print()

for fruits in fruits:
    print(fruits)
print()

# fruits.clear()                           # Clear the list     

# print(dir(fruits))                       # Using print(dir(fruits)) is a great way to inspect the methods and attributes available for an object in Python. If fruits is a string, the output will display all the methods and attributes of the str class.
