class SimpleCalculator:
    def add(self, a, b):
        return a + b # for addition

    def subtract(self, a, b):
        return a - b # for subtraction

    def multiply(self, a, b):
        return a * b # for multiplication

    def divide(self, a, b):
        if b == 0: # for division
            return None
        return a / b
