from expensetracker import create_expense, display_expenses, delete_expense


while True:
            print("what do you want to do?")
            print("1. add record")
            print("2. display records")
            print("3. delete record")
            print("4. exit")
            choice = int(input("enter your choice:"))
            match choice:
                case 1:
                    create_expense()
                case 2:
                    display_expenses()
                case 3:
                    delete_expense()
                case 4:
                    break



