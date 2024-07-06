# shopping_list_manager.py

# Initialize an empty shopping list
shopping_list = []

# Function to display the menu and handle user choices
def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

# Function to add an item to the shopping list
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"Added '{item}' to the shopping list.")

# Function to remove an item from the shopping list
def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the shopping list.")
    else:
        print(f"'{item}' is not found in the shopping list.")

# Function to view the current shopping list
def view_list():
    print("\nCurrent Shopping List:")
    if shopping_list:
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

# Main function to run the shopping list manager
def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Entry point of the script
if __name__ == "__main__":
    main()
