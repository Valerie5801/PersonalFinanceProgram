#VY 2nd Income and Expenses
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from budgetkeeper import validate_input
from datetime import date

class Incomes:
    def __init__(self, hist_income=None):
        if hist_income:
            self.hist_income = hist_income
        else:
            self.hist_income = []

    def add_income(self, new_income):
        self.hist_income.append(new_income)

    def get_all_income(self):
        return self.hist_income


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

    def get_all_expenses(self):
        return self.all_expenses


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


test_info = {
    "income": Incomes(),
    "expense": Expenses()
}


class IncomeExpenseGUI:
    def __init__(self, root, data_dict):
        self.root = root
        self.data = data_dict
        self.root.title("Income/Expense Tracker")
        self.root.geometry("700x600+100+100")
        self.root.configure(background="pale goldenrod")
        self.setup_menu()

    def create_popup_window(self, title, content_func):
        """Creates a popup window with a close button"""
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("600x500")
        popup.configure(background="pale goldenrod")
        content_frame = tk.Frame(popup, bg="pale goldenrod")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        content_func(popup, content_frame)
        # Close button at the bottom
        close_button = tk.Button(popup, text="Close", command=popup.destroy, bg="lightcoral", font=("Arial", 12))
        close_button.pack(pady=10)
        return popup
    
    def setup_menu(self):
        self.clear_window()
        title = tk.Label(self.root, text="Income/Expense Tracker", font=("Arial", 20, "bold"), bg="pale goldenrod")
        title.pack(pady=20)
        intro_label = tk.Label(
            self.root, 
            text="Welcome to the income/expense menu! Here, you can keep track of your income and expense history. Please select an option from the menu below to get started.",
            bg="pale goldenrod",
            wraplength=400,
            font=("Arial", 10))
        intro_label.pack(pady=10)
        button_frame = tk.Frame(self.root, bg="pale goldenrod")
        button_frame.pack(pady=20)
        goals_button = tk.Button(button_frame, text="Income History", command=self.open_income_window, width=20, font=("Arial", 12))
        goals_button.pack(pady=10)
        budget_button = tk.Button(button_frame, text="Expense History", command=self.open_expense_window, width=20, font=("Arial", 12))
        budget_button.pack(pady=10)
        quit_button = tk.Button(button_frame, text="Quit", command=self.root.quit, width=20, font=("Arial", 12), bg="lightcoral")
        quit_button.pack(pady=10)
    def clear_window(self):
        """Clear all widgets from the main window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def open_income_window(self):
        self.create_popup_window("Income History", self.income_content)
    def income_content(self, frame):
        if not self.data["income"]:
            intro = tk.Label(frame, text="Welcome to your income history! Here you can track when you earned your income by date.",
                           bg="pale goldenrod", wraplength=500, font=("Arial", 10))
            intro.pack(pady=10)
        goals_label = tk.Label(frame, text="Current History:", font=("Arial", 12, "bold"), bg="pale goldenrod")
        goals_label.pack()
        if self.data["income"]:
            goals_text = scrolledtext.ScrolledText(frame, height=10, width=60, bg="white")
            goals_text.pack(pady=10)
            for income in self.data["income"].get_all_income():
                goals_text.insert(tk.END, str(income) + "\n")
            goals_text.config(state=tk.DISABLED)
        else:
            no_goals = tk.Label(frame, text="There is nothing in your income history yet.", bg="pale goldenrod", font=("Arial", 10))
            no_goals.pack(pady=10)
        # Buttons for the user to interact with golas
        button_frame = tk.Frame(frame, bg="pale goldenrod")
        button_frame.pack(pady=10)
        add_button = tk.Button(button_frame, text="Add item to History", command=self.add_to_income)
        add_button.pack(side=tk.LEFT, padx=5)
        edit_button = tk.Button(button_frame, text="Remove item from History", command=self.remove_from_income)
        edit_button.pack(side=tk.LEFT, padx=5)
        create_button = tk.Button(button_frame, text="Select an item", command=self.select_from_income)
        create_button.pack(side=tk.LEFT, padx=5)

    def add_to_income(self):
        income_amount = simpledialog.askfloat("Get Value", "What's the income amount for this entry?: ")
        if income_amount is None:
            return
        
        income_amount = float(income_amount)

        check_income = validate_input(income_amount, "float")
        if not check_income:
            messagebox.showerror("Invalid Input", "Please type a number.")
            return
        
        income_date = date.today()
        new_income = Income(income_date, income_amount)
        self.data["income"].add_income(new_income)
        messagebox.showinfo("Item Added", "Successfully added new item to your Income history.")
        

    def remove_from_income(self):
        if not self.data["income"]:
            messagebox.showwarning("Nothing in history", "Your history is empty. Start by adding an item to it!")
            return
        
        selection = self.show_selection_dialog("", "Select the entry you want to remove:", self.data['income'])
        
        

    def select_from_income(self):
        if not self.data["income"]:
            messagebox.showwarning("Nothing in history", "Your history is empty. Start by adding an item to it!")
            return
        

    def open_expense_window(self):
        self.create_popup_window("Income History", self.expense_content)
    def expense_content(self, frame):
        if not self.data["expense"]:
            intro = tk.Label(frame, text="Welcome to your expenses history! Here you can track your expenses by date.",
                           bg="pale goldenrod", wraplength=500, font=("Arial", 10))
            intro.pack(pady=10)
        goals_label = tk.Label(frame, text="Current History:", font=("Arial", 12, "bold"), bg="pale goldenrod")
        goals_label.pack()
        if self.data["expense"]:
            goals_text = scrolledtext.ScrolledText(frame, height=10, width=60, bg="white")
            goals_text.pack(pady=10)
            self.data['expense'].show_income()
            goals_text.config(state=tk.DISABLED)
        else:
            no_goals = tk.Label(frame, text="There is nothing in your expense history yet.", bg="pale goldenrod", font=("Arial", 10))
            no_goals.pack(pady=10)
        # Buttons for the user to interact with golas
        button_frame = tk.Frame(frame, bg="pale goldenrod")
        button_frame.pack(pady=10)
        add_button = tk.Button(button_frame, text="Add item to History", command=self.add_to_income)
        add_button.pack(side=tk.LEFT, padx=5)
        edit_button = tk.Button(button_frame, text="Remove item from History", command=self.remove_from_income)
        edit_button.pack(side=tk.LEFT, padx=5)
        create_button = tk.Button(button_frame, text="Select an item", command=self.select_from_income)
        create_button.pack(side=tk.LEFT, padx=5)

    def add_to_expense(self):
        pass
        
        

    def remove_from_expense(self):
        if not self.data["income"]:
            messagebox.showwarning("Nothing in history", "Your history is empty. Start by adding an item to it!")
            return
        

    def select_from_expense(self):
        if not self.data["income"]:
            messagebox.showwarning("Nothing in history", "Your history is empty. Start by adding an item to it!")
            return
    def show_selection_dialog(self, title, prompt, items):
        #shows dialouge
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("400x300")
        dialog.configure(background="pale goldenrod")
        label = tk.Label(dialog, text=prompt, bg="pale goldenrod", font=("Arial", 11))
        label.pack(pady=10)
        listbox = tk.Listbox(dialog, font=("Arial", 10))
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        for item in items:
            listbox.insert(tk.END, item)
        selected = None
        def on_select():
            nonlocal selected
            selection = listbox.curselection()
            if selection:
                selected = listbox.get(selection[0])
                dialog.destroy()
            else:
                messagebox.showwarning("No Selection", "Please select an item.")
        button = tk.Button(dialog, text="Select", command=on_select, font=("Arial", 10))
        button.pack(pady=10)
        dialog.wait_window()
        return selected



"""def set_expenses():
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

        expense_interval = date.today()
        
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
    return all_expenses"""