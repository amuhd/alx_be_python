class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Returns the sum of two numbers.
        
        :param a: The first number.
        :param b: The second number.
        :return: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers.
        
        This method also prints the class attribute 'calculation_type'.
        
        :param a: The first number.
        :param b: The second number.
        :return: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage
if __name__ == "__main__":
    # Using the static method to add numbers
    sum_result = Calculator.add(5, 3)
    print(f"Sum: {sum_result}")

    # Using the class method to multiply numbers
    product_result = Calculator.multiply(5, 3)
    print(f"Product: {product_result}")
