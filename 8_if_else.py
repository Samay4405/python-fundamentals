age = int(input("Enter ur age:"))

if age >= 18:
    print("You are eligible to vote!")
elif age <= 0:                                      # You can add as many elif statements as you wish
    print("You are not born yet.")
elif age >= 100:
    print("You are too old to vote.")
else:
    print("You are not eligible to vote.")