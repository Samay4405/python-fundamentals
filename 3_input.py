#input() = A function that promotes the user to enter data 
#           and returns the entered data as a string

name = input("What is your name?:")
age = input("How old r u?:")

age = int(age)           # cause it returs the data as a string
                         # or you can do age = int(input("How old r u?:")) instead!!
age += 1                
 
print(f"Hello {name}")
print("Happy Birthday.")
print(f"You are now {age} years old!")