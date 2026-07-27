# Functions = A block of reusable code.
#             place () after the function name to invoke it.

# def nnn():
#     print("lorem.......................................................................")
#     print("lorem.......................................................................")
#     print("lorem.......................................................................")
    
# nnn() 
# nnn()                             # Write the function name to call it.

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount :.2f} is due: {due_date}")

username = input("Enter your name: ")
amount = input("Enter the amount: ")
due_date = input("Enter the due date: ")
display_invoice(username, float(amount), due_date)  # We can also use the input() function to get the values from the user.

# display_invoice("Arnav", 90.50, "02/10")
# display_invoice("Karwa", 10.70, "04/11")