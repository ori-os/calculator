def add(num1, num2):
    pass


def subtract(num1, num2):
    pass


def multiply(num1, num2):
    pass


def divide(num1, num2):
    pass


def power(num1, num2):
    pass


def get_operator(num1, num2):
    print("Enter a number to choose the operation:")
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
        print("Error - invalid input. Please try again!")
        get_operator(num1, num2)


def main():
    num1 = 7
    num2 = 1
    get_operator(num1, num2)


if __name__ == '__main__':
    main()
