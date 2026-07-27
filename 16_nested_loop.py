# Nested loop = A loop within another loop (outer, inner)

for x in range(1 ,10):
  #  print(x)
   print(x, end="")
  #  print(x, " ")
  #  print(x, end=" ")
  #  print(x, "\n")
  # print(x, ",")
  # print(x, end=",") 
  
# for x in range(3):
#    for y in range(1 ,10):
#     print(y, end="")
#     print()  

rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns: "))
symbols = (input("Enter a symbol to use: "))

for i in range(rows):
    for j in range(columns):
        print(symbols, end=" ")
    print()