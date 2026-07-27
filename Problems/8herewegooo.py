ggs = []

# Computation functions (no prints, only return values)
def calculate_sum(numbers):
    return sum(numbers)

def calculate_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def calculate_subtraction(numbers):
    if len(numbers) < 2:
        return None
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Phase B: Decision logic - returns (operation, result)
def get_operation_result(choice, numbers):
    if choice in ['A', 'a']:
        result = calculate_sum(numbers)
        return ('addition', result)
    elif choice in ['M', 'm']:
        result = calculate_product(numbers)
        return ('multiplication', result)
    elif choice in ['S', 's']:
        result = calculate_subtraction(numbers)
        return ('subtraction', result)
    else:
        return (None, None)
    
    
# Phase D: Output formatting
def display_result(operation, result):
    if operation == 'addition':
        print(f'Sum of numbers: {result}')
    elif operation == 'multiplication':
        print(f'Product of numbers: {result}')
    elif operation == 'subtraction':
        if result is None:
            print("Need at least two numbers to perform subtraction.")
        else:
            print(f'Result of sequential subtraction: {result}')

# Phase A: Input collection
ggs = []

while True:
    
    gg = input("Press Y to enter a number OR X to exit : ")
    
    if gg == 'Y' or gg == 'y':
        try:
            ggwp = int(input("Enter the number : "))
            print(f'you entered : {ggwp}')
            ggs.append(ggwp)
            print(f'List of numbers entered: {ggs}')
        except ValueError:
            print("Invalid input, enter an integer")
    elif gg == 'X' or gg == 'x':
        print("the END")
        break
    else:
        print("Invalid INPUT")

# Main operation loop
while True:
    ops = input("choose operation - A: Addition, M: Multiplication, S: Subtraction, X: Exit : ")
    
    if ops in ['X', 'x']:
        print("Exiting operations menu.")
        break
    
    operation, result = get_operation_result(ops, ggs)
    
    if operation is not None:
        display_result(operation, result)
    else:
        print("Invalid operation input.")