# daily_reminder.py

def main():
    # Prompt the user to input a task description
    task = input("Enter your task: ")
    
    # Prompt for the task's priority (high, medium, low)
    priority = input("Priority (high/medium/low): ").lower()
    
    # Ask if the task is time-bound (yes or no)
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Reminder message
    reminder = f"Reminder: '{task}' is a"
    
    #task processing
    match priority:
        case "high":
            reminder += " high priority task"
        case "medium":
            reminder += " medium priority task"
        case "low":
            reminder += " low priority task"
        case _:
            print("Invalid priority entered.")
            return

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."
    
    
    # Print the customized reminder
    print("\nReminder:")
    print(reminder)

if __name__ == "__main__":
    main()
