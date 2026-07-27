# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy (q to quit): ")
    if food.lower() == "q":                                      # If only (if food = "q") is used then if user writes Q won't work.
        break
    
    else: 
        price = float(input(f"Enter the price of the {food} : $"))
        
        foods.append(food)
        prices.append(price)
        
print("------Your Cart--------")
for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price
    
print()
print(f"Your total is = {total}")
        