# pattern_drawing.py

def main():
    # Prompt users to enter patern size
    size = int(input("Enter the size of the pattern: "))
    
    # Validation of a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize the row counter
    row = 0
    
    # Using while loop to iterate through each row
    while row < size:
        # Using for loop to print asterisks side by side
        for _ in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment of row counter
        row += 1

if __name__ == "__main__":
    main()
