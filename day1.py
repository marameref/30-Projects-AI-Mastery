# Basic Calculator
#Fxn to add 2 numbers
def add(x, y):
    return x + y

#Fxn to subtract 2 numbers
def subtract(x, y):
    return x - y

#Fxn to multiply 2 numbers
def multiply(x, y):
    if y == 0:
        return 0
    else:
        return x * y

#Fxn to divide 2 numbers
def divide(x, y):
    if y == 0:
        return "Error, Division by zero is not possible"
    else:
        return x / y

#function to square to numbers
def square(x, y):
    if y == 0:
        return 1
    else:
        return x ** y
    
def calculator():
    print("Welcome to the Basic Calculator (Range: 1-100)")

    while True:
        try:
            x = int(input("Enter value of x (1-100): "))
            y = int(input("Enter value of y (1-100): "))
            #Validate input
            if not (1 <= x <= 100 and 1 <= y <= 100):
                print("Both numbers must be between 1-100. Try Again\n")
                continue
            #Perform Operations
            print(f"\nResults for x = {x}, y = {y}:")
            print(f"Addition: {x} + {y} = {add(x, y)}")
            print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
            print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
            print(f"Division: {x} / {y} = {divide(x, y)}")
            print(f"Square: {x} ^ {y} = {square(x, y)}\n")

            #Ask to repeat or exit loop
            repeat = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if repeat != 'yes':
                print("Thanks for using Basic Calculator!. Good Bye\n")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")

#Run app
calculator()

