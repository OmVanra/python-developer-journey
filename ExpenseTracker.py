from datetime import datetime

FILENAME = 'expenses.txt'

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    expenses.append({'date':parts[0],'category':parts[1],'amount':float(parts[2])})
    except FileNotFoundError:
        pass
    return expenses

def add_expense(category, amount):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        amount_float = float(amount)
        if amount_float <= 0:
            raise ValueError("Amount must be greater than Zero.")
        with open(FILENAME, 'a') as file:
            file.write(f"{date_str},{category.strip().title()},{amount_float}\n")
        print("✓ Expense added successfully!")
    except ValueError as e:
        print(f"❌ Error: Invalid amount. {e}")     

def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    print("\n--- EXPENSE SUMMARY ---")
    total = 0.0
    for exp in expenses:
        print(f"[{exp['date']}] {exp['category']}:${exp['amount']:.2f}")
        total += exp['amount']

    print("-" * 23)
    print(f"TOTAL SPENT: ${total:.2f}\n")

def main():
    while True:
        print("=== FAST EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            category = input("Enter category (e.g., Food, Transport): ")
            amount = input("Enter amount spent ($): ")
            add_expense(category, amount)
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Please pick 1, 2, or 3.\n")        

if __name__ == "__main__":
    main()