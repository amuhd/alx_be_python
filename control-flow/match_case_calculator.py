# calculator
def main():
    #prompt for users
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
    # calculations with statements
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "undefined (Cannot divide by zero.)"
    else:
        result = "invalid operation"
            
    #output
    if isinstance(result, (int, float)):
        print(f"The result is {result}.")
    else:
        print(f"The result is {result}.")
if __name__ == "__main__":
    main()
           
        