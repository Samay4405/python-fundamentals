def sum(a,b):
    return a + b
    
def sub(a,b):
    return a - b
    
def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "EEERRORR"
        
while True:
    
    print("Calculator")
    print("1.Addition")
    print("2. Subtaction")
    print("3. Multiplication")
    print("4. Division")
    print("5. EXIT")
    
    choice = int(input("Enter your choice (1-5):"))
    
   
    
    
    if choice == 1:
        
        n1 = float(input("Enter first no.:"))
        n2 = float(input("Enter second no.:"))
    
        print("Addition:", sum(n1,n2))
    elif choice == 2:
        
        n1 = float(input("Enter first no.:"))
        n2 = float(input("Enter second no.:"))
    
        print("Subtraction:", sub(n1,n2))
    elif choice == 3:
        
        n1 = float(input("Enter first no.:"))
        n2 = float(input("Enter second no.:"))
    
        print("Multiplication:", multiply(n1,n2))
    elif choice == 4 :
        
        n1 = float(input("Enter first no.:"))
        n2 = float(input("Enter second no.:"))
    
        print("Division:", divide(n1,n2))
    elif choice == 5:
        
        print("The End.")
        break
    else :
        print("HATT")
    
    