#VY 2nd Income and Expenses
from val_currency_conversion import validate_input #temporary, get from helper functions once it's there

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
        return f"You earn ${self.income_info["amount"]} per {self.income_info["time"]}."


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
            self.all_expenses.pop(selected_expense)
            print(f"Category {selected_expense.name} has been removed from expenses.")
        else:
            print(f"That expense doesn't exist.")


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



def set_income():
    while True:
        income_interval = input("What time interval do you recieve your income/like to track it?(day/month/year): ").lower().strip()
        if income_interval != "day" and income_interval != "month" != "year":
            print('Please type in either "daily", "month", or "year"')
        else:
            break
    
    while True:
        income_amount = input("What time interval do you recieve your income/like to track it?(daily/monthly/yearly): ")
        check_income = validate_input(income_amount, "float")
        if check_income:
            income_amount = float(income_amount)
            break
        else:
            print("That isn't a number.")

    user_income = Income(income_interval, income_amount)
    print(user_income)
    return user_income


def set_expenses():
    all_expenses = []
    while True:
        income_interval = input("What time interval do you recieve your income/like to track it?(day/month/year): ").lower().strip()
        if income_interval != "day" and income_interval != "month" != "year":
            print('Please type in either "daily", "month", or "year"')
        else:
            break
    
    while True:
        income_amount = input("What time interval do you recieve your income/like to track it?(daily/monthly/yearly): ")
        check_income = validate_input(income_amount, "float")
        if check_income:
            income_amount = float(income_amount)
            break
        else:
            print("That isn't a number.")