expenseData = []
nextId = 1


def show_menu():
    print("\n EXPENSE TRACKER")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. View total amount spent")
    print("4. View total spent by category")
    print("5. Delete an expense")
    print("0. Exit")


def add_new_expense():
    global nextId

    print("\n Add a New Expense")

    d = input("Enter date (DD-MM-YYYY): ").strip()
    catg = input("Enter category: ").strip()
    desc = input("Enter description: ").strip()

    amt_raw = input("Enter amount: ").strip()
    try:
        amt = float(amt_raw)
    except ValueError:
        print("Oops—couldn't read that as a number.")
        return

    entry = {}
    entry["id"] = nextId
    entry["date"] = d
    entry["category"] = catg
    entry["description"] = desc
    entry["amount"] = amt

    expenseData.append(entry)

    print(f"Saved! (id={nextId})")
    nextId = nextId + 1


def view_all():
    print("\n All Expenses")
    print("ID | Date       | Category     | Description           | Amount")

    for e in expenseData:
        d = e["description"]
        if len(d) > 18:
            d = d[:15] + "..."

        print(f'{e["id"]:2} | {e["date"]:<10} | {e["category"]:<12} | {d:<20} | {e["amount"]:>8.2f}')


def total_spent():
    t = 0
    for e in expenseData:
        t = t + e["amount"]

    print("\n Total spent:", t)


def total_by_cat():
    totals = {}

    for e in expenseData:
        cat = e["category"]
        if cat not in totals:
            totals[cat] = 0
        totals[cat] += e["amount"]

    print("\n Total spent by category:")
    for cat, amt in totals.items():
        print(f"{cat}: {amt}")


def find_expense(theId):
    for e in expenseData:
        if e["id"] == theId:
            return e
    return None


def delete_expense():
    raw = input("Enter the ID to delete: ").strip()
    try:
        num = int(raw)
    except ValueError:
        print("That's not a number...")
        return

    e = find_expense(num)
    if e is None:
        print("Could not find that ID.")
        return

    print("Found:", e)
    confirm = input("Are you SURE? (y/n): ").lower().strip()

    if confirm == "y":
        try:
            expenseData.remove(e)
            print("Deleted.")
        except ValueError:
            print("Something weird happened—couldn't delete.")
    else:
        print("Okay, leaving it alone.")


while True:
    show_menu()
    choice = input("Your choice: ").strip()

    if choice == "1":
        add_new_expense()
    elif choice == "2":
        view_all()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        total_by_cat()
    elif choice == "5":
        delete_expense()
    elif choice == "0":
        print("Bye!")
        break
    else:
        print("No idea what that means. Try again.")



           