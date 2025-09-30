balance = 1000.0

def display_menu():
    print("\n===== ATM Menu =====")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")

def get_choice():
    choice = input("Enter your choice (1-4): ")
    return choice.strip()

def credit():
    global balance
    try:
        amount = float(input("Enter amount to credit: "))
        if amount <= 0:
            print("⚠ Please enter a positive amount.")
        else:
            balance += amount
            print(f"✅ ${amount:.2f} credited to your account.")
    except ValueError:
        print("⚠ Invalid input! Please enter a number.")

def debit():
    global balance
    try:
        amount = float(input("Enter amount to debit: "))
        if amount <= 0:
            print("⚠ Please enter a positive amount.")
        elif amount > balance:
            print("⚠ Insufficient balance.")
        else:
            balance -= amount
            print(f"✅ ${amount:.2f} debited from your account.")
    except ValueError:
        print("⚠ Invalid input! Please enter a number.")

def show_balance():
    print(f"💰 Your current balance is: ${balance:.2f}")

def main():
    while True:
        display_menu()
        choice = get_choice()
        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            show_balance()
        elif choice == '4':
            print("🙏 Thank you for using the ATM. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
