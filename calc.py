def add(num1, num2):
    result = num1 + num2
    print_result(result, "added")


def subtract(num1, num2):
    result = num1 - num2
    print_result(result, "subtracted")


def multiply(num1, num2):
    result = num1 * num2
    print_result(result, "multiplied")


def divide(num1, num2):
    result = num1 / num2
    print_result(result, "divided")


def power(num1, num2):
    result = num1 ** num2
    print_result(result, "raised to the power")


def print_result(result, operation):
    print("Successfully", operation, "the numbers. Result:", result)


def get_operator(num1, num2):
    print("Enter a number matching the desired operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    operator = input()
    if operator == '1':
        add(num1, num2)
    elif operator == '2':
        subtract(num1, num2)
    elif operator == '3':
        multiply(num1, num2)
    elif operator == '4':
        divide(num1, num2)
    elif operator == '5':
        power(num1, num2)
    else:
        print("Error - invalid input. Please try again:")
        get_operator(num1, num2)


def main():
    num1 = input("Enter the first number: ")
    while not num1.isnumeric():
        num1 = input("Invalid input. Please enter a number: ")
    num2 = input("Enter the second number: ")
    while not num2.isnumeric():
        num2 = input("Invalid input. Please enter a number: ")
    get_operator(int(num1), int(num2))


if __name__ == '__main__':
    main()
