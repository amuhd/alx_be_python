def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        result = num / denom
        return f"The result is: {result}"
    except ValueError:
        return "Error: Non-numeric input detected. Please provide numeric values."

# Example usage (for testing purposes):
# print(safe_divide(10, 2))  # Should print "The result is: 5.0"
# print(safe_divide(10, 0))  # Should print "Error: Division by zero is not allowed."
# print(safe_divide(10, "a"))  # Should print "Error: Non-numeric input detected. Please provide numeric values."
