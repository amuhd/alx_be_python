# multiplication_table.py

def main():
    # Prompt users to enter number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generation and output of the multiplication table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()
