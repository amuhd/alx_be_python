import math

class Shape:
    def area(self):
        """
        Calculate the area of the shape.
        
        This method should be overridden in derived classes.
        """
        raise NotImplementedError("Subclasses must override area() method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance with the given length and width.
        
        :param length: The length of the rectangle.
        :param width: The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        
        :return: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes a Circle instance with the given radius.
        
        :param radius: The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        
        :return: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

# Example usage:
if __name__ == "__main__":
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(length=5, width=3)
    circle = Circle(radius=4)

    # Print the areas of the shapes
    print(f"Area of the rectangle: {rectangle.area()}")
    print(f"Area of the circle: {circle.area()}")
