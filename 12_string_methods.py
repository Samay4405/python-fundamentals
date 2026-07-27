name = input("Enter your name: ")
print(name)
trim = name.strip()                     # remove leading and trailing spaces
print(trim)
result = len(name)                           #lenght
print(result)
result1= name.find("a")
result2= name.rfind("a")
result3= name.find("A")
name = name.capitalize()                     # capitalize first letter.
#name = name.upper/lower()                   # to capitalize or lower case all letters
result4 = name.isdigit()                     # check if it is a digit.  ( It only returns true if all are digits)
result5 = name.isalpha()                     # check if it has letters. (Return false even if it has space)

print("First occurrence of 'a' :", result1)  # starts from 0 (ex. S is at o)
                                             # if the letter is not found, result is -1.
print(f"Last occurrence of 'a' : {result2}")

print("First occurrence of 'A' :", result3)

print(result4)
print(result5)