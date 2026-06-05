# Calculator
def addition():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    return value1 + value2

def subtraction():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    return value1 - value2

def multiplication():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    return value1 * value2

def division():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))

    if value2 == 0:
        return "Error: Division by zero is not allowed."

    return value1 / value2


def calculator():
    print("********* Welcome to Calculator *********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Enter 'q' to quit.")

    while True:
        choice = input("\nChoose an operation (1/2/3/4) or 'q' to quit: ").strip()

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        elif choice == '1':
            print(f"The result of addition is: {addition()}")

        elif choice == '2':
            print(f"The result of subtraction is: {subtraction()}")

        elif choice == '3':
            print(f"The result of multiplication is: {multiplication()}")

        elif choice == '4':
            print(f"The result of division is: {division()}")

        else:
            print("Invalid choice. Please try again.")

calculator()

