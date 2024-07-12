import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <initial_balance> <operation> <amount>")
        print("Example: python main-0.py 100 deposit 50")
        return

    try:
        initial_balance = float(sys.argv[1])
    except ValueError:
        print("Initial balance must be a number.")
        return
    
    account = BankAccount(initial_balance)

    if len(sys.argv) >= 3:
        operation = sys.argv[2].lower()
        if operation in ["deposit", "withdraw"]:
            if len(sys.argv) >= 4:
                try:
                    amount = float(sys.argv[3])
                except ValueError:
                    print("Amount must be a number.")
                    return
                
                if operation == "deposit":
                    account.deposit(amount)
                elif operation == "withdraw":
                    account.withdraw(amount)
                account.display_balance()
            else:
                print("Please specify an amount for the operation.")
        else:
            print("Invalid operation. Please use 'deposit' or 'withdraw'.")
    else:
        account.display_balance()

if __name__ == "__main__":
    main()
