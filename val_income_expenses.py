#VY 2nd Income and Expenses
from budgetkeeper import validate_input #temporary, get from helper functions once it's there
from val_currency_conversion import currency_conversion

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
        return f"Category {self.expense_info["source"]} is ${self.expense_info["amount"]} per {self.expense_info["time"]}.\n"



def set_income():
    while True:
        income_interval = input("What time interval do you recieve your income/like to track it?(day/month/year): ").lower().strip()
        if income_interval != "day" and income_interval != "month" != "year":
            print('Please type in either "daily", "month", or "year"')
        else:
            break
    
    while True:
        income_amount = input("What's your income amount (in the time interval you typed in)?: ")
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
    all_expenses = Expenses()
    while True:
        total_expense_groups = input("How may expense groups do you have?(type as a whole number): ")
        check_num = validate_input(total_expense_groups, "int")
        if check_num:
            check_num = int(check_num)
            break
        else:
            print("Please type it as a whole number.")

    for i in range(int(total_expense_groups)-1):
        expense_name = input(f"What is the name of expense group {i+1}?: ")

        while True:
            expense_interval = input("What time interval would you like to track this expense group?(day/month/year): ").lower().strip()
            if expense_interval != "day" and expense_interval != "month" != "year":
                print('Please type in either "daily", "month", or "year"')
            else:
                break
        
        while True:
            expense_amount = input("What's your expense value (in the time interval you typed in)?: ")
            check_expense = validate_input(expense_amount, "float")
            if check_expense:
                expense_amount = float(expense_amount)
                break
            else:
                print("That isn't a number.")

        new_expense_group = Expense(expense_interval, expense_amount, expense_name)
        all_expenses.add_expense(new_expense_group)
    
    print("Here's all your expenses:")
    all_expenses.show_expenses()
    return all_expenses