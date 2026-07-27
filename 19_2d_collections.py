data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Designer"],
    ["Charlie", 22, "Student"]
]

# Accessing nested data
print(data[1][2])  # Output: Designer

# Creating a 2D keypad
mobile_keypad = [
    ["1", "2", "3"],  # Row 1
    ["4", "5", "6"],  # Row 2
    ["7", "8", "9"],  # Row 3
    ["*", "0", "#"]   # Row 4
]

# Displaying the keypad
for row in mobile_keypad:
     for num in row:                                                   # print(" ".join(row))
        print(num, end=" ")
     print()
                                                     
