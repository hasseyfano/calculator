# calculator.py

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    def get_user_input(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_user_input()

    def perform_calculation(self, choice, num1, num2):
        if choice == '1':
            return f"{num1} + {num2} = {self.add(num1, num2)}"
        elif choice == '2':
            return f"{num1} - {num2} = {self.subtract(num1, num2)}"
        elif choice == '3':
            return f"{num1} * {num2} = {self.multiply(num1, num2)}"
        elif choice == '4':
            result = self.divide(num1, num2)
            return f"{num1} / {num2} = {result}"
