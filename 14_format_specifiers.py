# Format Specifiers = {value:flags} format a value based on what flags are inserted.

# flags = 0 : Left Justify (default).

price1 = 3.1456852
price2 = -3.1456852
price3 = 30000.215
print(f"Price 1 is ${price1:.1f}") 
print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price1:.3f}")
print(f"Price 1 is ${price1:20}")
print(f"Price 1 is ${price1:020}")
print(f"Price 1 is ${price1:<20}")
print(f"Price 1 is ${price1:>20}")
print(f"Price 1 is ${price1:^20}")
print(f"Price 1 is ${price1:+20}")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3:,}")
print(f"Price 3 is ${price3:+,.2f}")