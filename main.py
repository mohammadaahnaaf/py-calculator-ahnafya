import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def root(x, y):
    return x**(1/y)
    # return math.sqrt(x)

def squire(x, y):
    return x ** y


print("Ahnafya Calculator: Python")
print("|")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Root")
print("6.Squire")

while True:
    # take input from the user
    choice = input("Enter choice (1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num2, "√", num1, "=", root(num1, num2))
        
        elif choice == '6':
            print(num1, "^", num2, "=", squire(num1, num2))
        
        
        next_calculation = input("Let's do more calculation? (y/n): ")
        if next_calculation == "n":
          break
    else:
        print("Invalid Input")