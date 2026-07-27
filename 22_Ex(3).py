# Concession stand program.

menu = {
    "popcorn": 5.00,
    "soda": 3.00,
    "candy": 2.50,
    "nachos": 4.50,
    "hotdog": 3.50,
    "fries" : 3.50,
    "soft drinks": 2.00,
    "water": 1.50,
    "chips": 1.00,
    "coke": 1.25,
    "pepsi": 1.25,
}

cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("------------------------")

while True: 
    food = input("What would you like to order?(q to quit):")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print("------ YOUR ORDER ------")
print(f"Total is : ${total:.2f}")
    

    
        