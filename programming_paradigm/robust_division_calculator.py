def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        result = num / denom
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."

# Example:
# print(safe_divide(10, 2))  "The result of the division is 5.0"
# print(safe_divide(10, 0))  "Cannot divide by zero."
# print(safe_divide(10, "a"))  "Please enter numeric values only."
