import datetime,uuid
import json


class expense:
    def __init__(self,amount,category,description,date = datetime.date.today()):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    
    def to_db(self):
        return {
            "id": self.id, 
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
                 }
#     def __str__(self):
#         return f"expense(id={self.id}, amount={self.amount}, category={self.category}, date={self.date})"

# first = expense(100,"food")
# print(first)

class expense_manager:
    def __init__(self,filepath = "expenses.json"):
        self.filepath = filepath
        self.expenses = []
        self.load()

    def save(self, expenses):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=2)

    def get_valid_date(self):
        while True:
            date_input = input("Enter date (YYYY-MM-DD): ").strip()
            
            try:
                valid_date = datetime.strptime(date_input, "%Y-%m-%d")            
                return valid_date.strftime("%Y-%m-%d")
                
            except ValueError:
                print("❌ Invalid format or date. Please use YYYY-MM-DD (e.g., 2026-05-21).")

    def create_expense(self):
        print("Enter the amount:")
        amount = float(input())
        print("Enter the category:")
        category = input()
        print("Enter the description:")
        description = input()
        date_input = self.get_valid_date()

        new_expense = expense(amount, category, description, date_input)
        with open(self.filepath, "r", encoding="utf-8") as f:
            expenses = json.load(f)
        expenses.append(new_expense.to_db())
        self.save(expenses)

    def display_expenses(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            a = json.load(f)
            for i in a:
                print(f"id: {i['id']},\n   Amount: {i['amount']}, Date: {i['date']}, Category: {i['category']}, Description: {i['description']}")


    def delete_expense(self):
        print("Enter the id of the expense to delete:")
        expense_id = input()
        with open(self.filepath, "r", encoding="utf-8") as f:
            expenses = json.load(f)
        expenses = [expense for expense in expenses if expense["id"] != expense_id]
        self.save(expenses)

    def view_expenses(self):
        return list(self.expenses)
    

    def calculate_total(self):
        return sum(e.amount for e in self.expenses)
    
    def get_float(prompt, min_val=0.01):
        while True:
            raw = input(prompt).strip()
            try:
                value = float(raw)
                if value < min_val:
                    print(f"Amount must be at least {min_val}.")
                    continue
                return value
            except ValueError:
                print("Please enter a number (e.g. 12.50).")

    def get_date(prompt):
        """Keep asking until user enters a valid YYYY-MM-DD date."""
        import datetime
        while True:
            raw = input(prompt).strip()
            if not raw:
                # Empty → use today
                return datetime.date.today().isoformat()
            try:
                datetime.date.fromisoformat(raw)    # validates format
                return raw
            except ValueError:
                print("Use YYYY-MM-DD format (e.g. 2024-03-15).")

    def get_category(prompt, valid):
        """Only accept categories from a known list."""
        while True:
            raw = input(prompt).strip().lower()
            if raw in valid:
                return raw
            print(f"Choose from: {', '.join(valid)}")

    # Usage in add_expense()
    amount   = get_float("Amount: £")
    date     = get_date("Date (YYYY-MM-DD or Enter for today): ")
    category = get_category("Category (food/transport/bills/other): ",
                            {"food","transport","bills","other"})      
# display_expenses()
# delete_expense()
# create_expense()