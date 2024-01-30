# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def get_user_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_input()

def calculator():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_user_input()

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            
            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != "yes":
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()
