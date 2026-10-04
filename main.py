def verify_pin(correct_pin, max_attempts=3):
    """Handles user authentication with a limited number of attempts."""
    attempts = 0
    while attempts < max_attempts:
        entered_pin = input("Enter your 4-digit PIN: ").strip()
        if entered_pin == correct_pin:
            print("\n Login successful!")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect PIN. Attempts left: {remaining}\n")
            else:
                print("Too many incorrect attempts. Account locked for security.")
    return False


def check_balance(balance):
    """Displays current account balance."""
    print(f"\n Current Balance: ₹{balance:,.2f}")


def deposit(balance):
    """Handles cash deposits and updates the balance."""
    try:
        amount = float(input("\nEnter amount to deposit: ₹"))
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return balance
        balance += amount
        print(f"Successfully deposited ₹{amount:,.2f}")
        print(f"New Balance: ₹{balance:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance


def withdraw(balance):
    """Handles cash withdrawals with balance checks."""
    try:
        amount = float(input("\nEnter amount to withdraw: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return balance
        if amount > balance:
            print(f"Insufficient funds! Your current balance is ₹{balance:,.2f}")
            return balance
        balance -= amount
        print(f"Please collect your cash: ₹{amount:,.2f}")
        print(f"Remaining Balance: ₹{balance:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance


def show_menu():
    """Prints the operation menu."""
    print("\n" + "=" * 25)
    print("      ATM MAIN MENU      ")
    print("=" * 25)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 25)


def run_atm():
    """Main driver function managing account state and the main loop."""
    account_pin = "1234"
    balance = 10000.00  # Initial account balance

    print("=" * 35)
    print("   WELCOME TO APEX BANK ATM   ")
    print("=" * 35)

    if not verify_pin(account_pin):
        return

    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("\nThank you for banking with us. Have a great day!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    run_atm()
