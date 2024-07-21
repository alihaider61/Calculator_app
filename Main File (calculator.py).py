# Import necessary functions from separate files
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


def calculator():
    while True:
        # Input numbers and operator from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        # Perform operations based on operator
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator")
            continue

        # Print the result
        print(f"Result: {result}")

        # Ask user if they want to quit
        choice = input("Do you want to quit? (Y/N): ").strip().upper()
        if choice == 'Y':
            break
        elif choice == 'N':
            continue
        else:
            print("Invalid choice. Continuing...")
            continue


if __name__ == "__main__":
    calculator()
