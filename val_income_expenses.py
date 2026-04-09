#VY 2nd Income and Expenses
from budgetkeeper import validate_input
from val_currency_conversion import currency_conversion
from datetime import datetime

class Incomes:
    def __init__(self, hist_income=None):
        if hist_income:
            self.hist_income = hist_income
        else:
            self.hist_income = []

    def add_income(self, new_income):
        self.hist_income.append(new_income)

    def remove_income(self, selected_income):
        if selected_income in self.hist_income:
            self.hist_income.remove(selected_income)
            print(f"Income set at {selected_income['time']} has been removed from your income history.")
        else:
            print(f"That doesn't exist.")

    def show_income(self):
        for income in self.hist_income:
            print(f"{income}")


class Income:
    def __init__(self, given_time, given_amount):
        self.income_info = {
            "time": given_time,
            "amount": given_amount
        }

    def edit_time(self, new_time):
        self.income_info["time"] = new_time

    def edit_amount(self, new_amount):
        self.income_info["amount"] = new_amount
    
    def __str__(self):
        return f"You got ${self.income_info['amount']} at {self.income_info['time']}."


class Expenses:
    def __init__(self, all_expenses=None):
        if all_expenses:
            self.all_expenses = all_expenses
        else:
            self.all_expenses = []
        
    def add_expense(self, new_expense):
        self.all_expenses.append(new_expense)

    def remove_expense(self, selected_expense):
        if selected_expense in self.all_expenses:
            self.all_expenses.remove(selected_expense)
            print(f"Category {selected_expense['source']} has been removed from expenses.")
        else:
            print(f"That expense doesn't exist.")

    def show_expenses(self):
        for expense in self.all_expenses:
            print(expense)


class Expense:
    def __init__(self, given_time, given_amount, given_source):
        self.expense_info = {
            "time": given_time,
            "amount": given_amount,
            "source": given_source
        }

    def edit_time(self, new_time):
        self.expense_info["time"] = new_time

    def edit_amount(self, new_amount):
        self.expense_info["amount"] = new_amount

    def edit_source(self, new_source):
        self.expense_info["source"] = new_source
    
    def __str__(self):
        return f"Category {self.expense_info['source']} is ${self.expense_info['amount']} at {self.expense_info['time']}."



def set_income():
    income_hist = Incomes()
    while True:
        total_income_hist = input("How many records do you want to keep in your income history?(as a whole number): ")
        check_num = validate_input(total_income_hist, "int")
        if check_num and int(total_income_hist) > 0:
            total_income_hist = int(total_income_hist)
            break
        else:
            print("Please type it as a whole number. Don't type in 0.")

    for i in range(total_income_hist):
        income_interval = datetime.now()
        
        while True:
            print(f"Input at {income_interval}...")
            income_amount = input("What's the income amount?: ")
            check_income = validate_input(income_amount, "float")
            if check_income:
                income_amount = float(income_amount)
                break
            else:
                print("That isn't a number.")

        add_user_income = Income(income_interval, income_amount)
        income_hist.add_income(add_user_income)

    print("\nHere is your income history:")
    income_hist.show_income()
    return income_hist


def set_expenses():
    all_expenses = Expenses()
    while True:
        total_expense_groups = input("How many expense groups do you have?(type as a whole number): ")
        check_num = validate_input(total_expense_groups, "int")
        if check_num:
            total_expense_groups = int(total_expense_groups)
            break
        else:
            print("Please type it as a whole number.")

    for i in range(int(total_expense_groups)):
        expense_name = input(f"What is the name of expense group {i+1}?: ")

        expense_interval = datetime.now()
        
        while True:
            expense_amount = input("What's your expense value for this category?: ")
            check_expense = validate_input(expense_amount, "float")
            if check_expense:
                expense_amount = float(expense_amount)
                break
            else:
                print("That isn't a number.")

        new_expense_group = Expense(expense_interval, expense_amount, expense_name)
        all_expenses.add_expense(new_expense_group)
    
    print("\nHere's all your expenses:")
    all_expenses.show_expenses()
    return all_expenses