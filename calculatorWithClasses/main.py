# main_calculator.py
from calculator import Calculator

def run_calculator():
    calculator = Calculator()

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
            num1, num2 = calculator.get_user_input()

            result = calculator.perform_calculation(choice, num1, num2)
            print(result)

            # check if user wants another calculation
            # break the while loop if the answer is no
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != "yes":
                break       
            #I could also have   if input("Do you want to perform another calculation? (yes/no): ").lower() != "yes":break to mmake the code cleaner
        else:
            print("Invalid Input")

if __name__ == "__main__":
    run_calculator()
