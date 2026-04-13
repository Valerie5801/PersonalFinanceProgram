import json
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
def validate_input(text, kind='int'):
    test_to_check = str(text).strip()
    if kind == 'int':
        try:
            int(test_to_check)
            return True
        except ValueError:
            return False
    elif kind == 'float':
        try:
            float(test_to_check)
            return True
        except ValueError:
            return False
    elif kind == 'alpha':
        return test_to_check.replace(" ", "").isalpha()
    else:
        return False
def get_from_csv(file):
    with open(file, "r") as r:
        reader = csv.DictReader(r)
        data_dict = {"goals": {}, "budget": {}, "expenses": [], "expenses_history": []}
        for row in reader:
            if row["type"].lower() == "goal":
                progress = float(row["progress"]) if "progress" in row else 0
                data_dict["goals"][row["name"]] = {"amount": float(row["amount"]),"progress": progress, "progress_history": []}
            elif row["type"].lower() == "budget":
                remaining = float(row["remaining"]) if "remaining" in row else float(row["amount"])
                data_dict["budget"][row["name"]] = {"amount": float(row["amount"]),"remaining": remaining, "spent_history": []}
            elif row["type"].lower() == "expenses":
                pass
        return data_dict
class budgetkeeperGUI:
    def __init__(self, root, data_dict):
        self.root = root
        self.data = data_dict
        self.root.title("Budget Keeper")
        self.root.geometry("700x600+100+100")
        self.root.configure(background="pale goldenrod")
        self.setup_main_menu()
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
    def setup_main_menu(self):
        self.clear_window()
        title = tk.Label(self.root, text="Budget Keeper", font=("Arial", 20, "bold"), bg="pale goldenrod")
        title.pack(pady=20)
        intro_label = tk.Label(
            self.root, 
            text="Welcome to the budget keeper! Here you can track your saving goals and your budget categories. Please select an option from the menu below to get started.",
            bg="pale goldenrod",
            wraplength=400,
            font=("Arial", 10))
        intro_label.pack(pady=10)
        button_frame = tk.Frame(self.root, bg="pale goldenrod")
        button_frame.pack(pady=20)
        goals_button = tk.Button(button_frame, text="Goals", command=self.open_goals_window, width=20, font=("Arial", 12))
        goals_button.pack(pady=10)
        budget_button = tk.Button(button_frame, text="Budget Categories", command=self.open_budget_window, width=20, font=("Arial", 12))
        budget_button.pack(pady=10)
        income_button = tk.Button(button_frame, text="Edit Income", command=self.open_income_window, width=20, font=("Arial", 12))
        income_button.pack(pady=10)
        quit_button = tk.Button(button_frame, text="Quit", command=self.root.quit, width=20, font=("Arial", 12), bg="lightcoral")
        quit_button.pack(pady=10)
    def clear_window(self):
        """Clear all widgets from the main window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def open_goals_window(self):
        self.create_popup_window("Goals Management", self.goals_content)
    def goals_content(self, popup, frame):
        if not self.data["goals"]:
            intro = tk.Label(frame, text="Welcome to the goals section! Here you can create saving goals and track your progress towards them.",
                           bg="pale goldenrod", wraplength=500, font=("Arial", 10))
            intro.pack(pady=10)
        goals_label = tk.Label(frame, text="Current Goals:", font=("Arial", 12, "bold"), bg="pale goldenrod")
        goals_label.pack()
        if self.data["goals"]:
            goals_text = scrolledtext.ScrolledText(frame, height=10, width=60, bg="white")
            goals_text.pack(pady=10)
            for goal, info in self.data["goals"].items():
                if info["amount"] > 0:
                    percent_complete = (info["progress"] / info["amount"]) * 100
                else:
                    percent_complete = 0
                goals_text.insert(tk.END, f"{goal}: ${info['progress']:.2f}/${info['amount']:.2f} ({percent_complete:.2f}%)\n")
            goals_text.config(state=tk.DISABLED)
        else:
            no_goals = tk.Label(frame, text="No goals yet.", bg="pale goldenrod", font=("Arial", 10))
            no_goals.pack(pady=10)
        # Buttons for the user to interact with golas
        button_frame = tk.Frame(frame, bg="pale goldenrod")
        button_frame.pack(pady=10)
        add_button = tk.Button(button_frame, text="Add to Goal", command=self.add_to_goal)
        add_button.pack(side=tk.LEFT, padx=5)
        edit_button = tk.Button(button_frame, text="Edit Goal", command=self.edit_goal)
        edit_button.pack(side=tk.LEFT, padx=5)
        create_button = tk.Button(button_frame, text="Create Goal", command=self.create_goal)
        create_button.pack(side=tk.LEFT, padx=5)
    def add_to_goal(self):
        """Add money to an existing goal"""
        if not self.data["goals"]:
            messagebox.showwarning("No Goals", "You don't have any goals yet. Create one first!")
            return
        goals_list = list(self.data["goals"].keys())
        goal_choice = self.show_selection_dialog("Select a Goal", "Choose a goal to add to:", goals_list)
        if goal_choice is None:
            return
        amount_str = simpledialog.askstring("Add to Goal", f"How much would you like to add to {goal_choice}?")
        if amount_str is None:
            return
        if not validate_input(amount_str, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        amount_to_add = float(amount_str)

        self.data["goals"][goal_choice]["progress"] += amount_to_add
        self.data["goals"][goal_choice]["progress_history"].append(amount_to_add)
        self.data["expenses"].append(amount_to_add)
        self.data["expenses_history"].append(amount_to_add)
        new_percent = (self.data["goals"][goal_choice]["progress"] / self.data["goals"][goal_choice]["amount"]) * 100
        messagebox.showinfo("Success", f"Added ${amount_to_add:.2f} to {goal_choice}.\nNew progress: {new_percent:.2f}%")

    def edit_goal(self):
        if not self.data["goals"]:
            messagebox.showwarning("No Goals", "You don't have any goals yet.")
            return
        goals_list = list(self.data["goals"].keys())
        goal_choice = self.show_selection_dialog("Select a Goal", "Choose a goal to edit:", goals_list)
        if goal_choice is None:
            return
        current_amount = self.data["goals"][goal_choice]["amount"]
        current_progress = self.data["goals"][goal_choice]["progress"]
        new_amount = simpledialog.askstring("Edit Goal", f"Enter new goal total (current: ${current_amount:.2f}):")
        if new_amount is None:
            return
        if not new_amount.strip():
            new_amount = str(current_amount)
        if not validate_input(new_amount, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        new_amount = float(new_amount)
        new_progress = simpledialog.askstring("Edit Goal", f"Enter new progress (current: ${current_progress:.2f}):")
        if new_progress is None:
            return
        if not new_progress.strip():
            new_progress = str(current_progress)
        if not validate_input(new_progress, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        new_progress = float(new_progress)
        if new_progress > new_amount:
            messagebox.showerror("Invalid", "Progress cannot be greater than the total amount.")
            return
        change = new_progress - current_progress
        self.data["goals"][goal_choice]["amount"] = new_amount
        self.data["goals"][goal_choice]["progress"] = new_progress
        if change > 0:
            self.data["goals"][goal_choice]["progress_history"].append(change)
            self.data["expenses"].append(change)
            self.data["expenses_history"].append(change)
        messagebox.showinfo("Success", f"Goal {goal_choice} updated successfully!")
    def create_goal(self):
        goal_name = simpledialog.askstring("Create Goal", "Enter the name of the new goal:")
        if goal_name is None:
            return
        if not goal_name.strip():
            messagebox.showerror("Invalid", "Goal name cannot be empty.")
            return
        goal_amount = simpledialog.askstring("Create Goal", "Enter the total amount for the new goal:")
        if goal_amount is None:
            return
        if not validate_input(goal_amount, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        goal_amount = float(goal_amount)
        self.data["goals"][goal_name] = {"amount": goal_amount, "progress": 0, "progress_history": []}
        messagebox.showinfo("Success", f"New goal '{goal_name}' created with amount ${goal_amount:.2f}!")
    def open_budget_window(self):
        self.create_popup_window("Budget Categories", self.budget_content)
    def budget_content(self, popup, frame):
        if not self.data["budget"]:
            intro = tk.Label(frame, text="Welcome to the budget categories section! Here you can create budget categories and track your spending.",
                           bg="pale goldenrod", wraplength=500, font=("Arial", 10))
            intro.pack(pady=10)
        budget_label = tk.Label(frame, text="Current Budget Categories:", font=("Arial", 12, "bold"), bg="pale goldenrod")
        budget_label.pack()
        if self.data["budget"]:
            budget_text = scrolledtext.ScrolledText(frame, height=10, width=60, bg="white")
            budget_text.pack(pady=10)
            for category, info in self.data["budget"].items():
                spent = info["amount"] - info["remaining"]
                budget_text.insert(tk.END, f"{category}: ${info['remaining']:.2f}/${info['amount']:.2f} remaining (${spent:.2f} spent)\n")
            budget_text.config(state=tk.DISABLED)
        else:
            no_budget = tk.Label(frame, text="No budget categories yet.", bg="pale goldenrod", font=("Arial", 10))
            no_budget.pack(pady=10)
        button_frame = tk.Frame(frame, bg="pale goldenrod")
        button_frame.pack(pady=10)
        add_button = tk.Button(button_frame, text="Add to Category", command=self.add_to_budget)
        add_button.pack(side=tk.LEFT, padx=5)
        edit_button = tk.Button(button_frame, text="Edit Category", command=self.edit_budget)
        edit_button.pack(side=tk.LEFT, padx=5)
        create_button = tk.Button(button_frame, text="Create Category", command=self.create_budget)
        create_button.pack(side=tk.LEFT, padx=5)

    def add_to_budget(self):
        if not self.data["budget"]:
            messagebox.showwarning("No Categories", "You don't have any budget categories yet. Create one first!")
            return
        categories_list = list(self.data["budget"].keys())
        category_choice = self.show_selection_dialog("Select a Category", "Choose a category to add to:", categories_list)
        if category_choice is None:
            return
        amount_str = simpledialog.askstring("Add to Category", f"How much would you like to add to {category_choice}?")
        if amount_str is None:
            return
        if not validate_input(amount_str, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        amount_to_add = float(amount_str)
        self.data["budget"][category_choice]["remaining"] += amount_to_add
        self.data["expenses"].append(amount_to_add)
        messagebox.showinfo("Success", f"Added ${amount_to_add:.2f} to {category_choice}.\nNew remaining: ${self.data['budget'][category_choice]['remaining']:.2f}")
    def edit_budget(self):
    # Edit a budget category
        if not self.data["budget"]:
            messagebox.showwarning("No Categories", "You don't have any budget categories yet.")
            return
        categories_list = list(self.data["budget"].keys())
        category_choice = self.show_selection_dialog("Select a Category", "Choose a category to edit:", categories_list)
        if category_choice is None:
            return
        current_amount = self.data["budget"][category_choice]["amount"]
        current_remaining = self.data["budget"][category_choice]["remaining"]
        new_amount = simpledialog.askstring("Edit Category", f"Enter new category total (current: ${current_amount:.2f}):")
        if new_amount is None:
            return
        if not new_amount.strip():
            new_amount = str(current_amount)
        if not validate_input(new_amount, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        new_amount = float(new_amount)
        new_remaining = simpledialog.askstring("Edit Category", f"Enter new remaining amount (current: ${current_remaining:.2f}):")
        if new_remaining is None:
            return
        if not new_remaining.strip():
            new_remaining = str(current_remaining)
        if not validate_input(new_remaining, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        new_remaining = float(new_remaining)
        if new_remaining > new_amount:
            messagebox.showerror("Invalid", "Remaining amount cannot be greater than the total amount.")
            return
        spent = current_remaining - new_remaining
        self.data["budget"][category_choice]["amount"] = new_amount
        self.data["budget"][category_choice]["remaining"] = new_remaining
        if spent > 0:
            self.data["budget"][category_choice]["spent_history"].append(spent)
            self.data["expenses"].append(spent)
            self.data["expenses_history"].append(spent)
        messagebox.showinfo("Success", f"Category {category_choice} updated successfully!")
    def create_budget(self):
        #allows you to crete a new budget catagory
        category_name = simpledialog.askstring("Create Category", "Enter the name of the new budget category:")
        if category_name is None:
            return
        if not category_name.strip():
            messagebox.showerror("Invalid", "Category name cannot be empty.")
            return
        category_amount = simpledialog.askstring("Create Category", "Enter the total amount for the new category:")
        if category_amount is None:
            return
        if not validate_input(category_amount, 'float'):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        category_amount = float(category_amount)
        self.data["budget"][category_name] = {"amount": category_amount, "remaining": category_amount, "spent_history": []}
        messagebox.showinfo("Success", f"New category '{category_name}' created with amount ${category_amount:.2f}!")
    def open_income_window(self):
        """Open the income editing window"""
        self.create_popup_window("Edit Income", self.income_content)
    def income_content(self, popup, frame):
        """Content for the income window"""
        current_income = self.data.get("income", 0)
        income_label = tk.Label(frame, text=f"Your current income is: ${current_income:.2f}", 
                               font=("Arial", 12), bg="pale goldenrod")
        income_label.pack(pady=20)
        # Create input tab
        input_frame = tk.Frame(frame, bg="pale goldenrod")
        input_frame.pack(pady=10)
        label = tk.Label(input_frame, text="Enter new income:", font=("Arial", 11), bg="pale goldenrod")
        label.pack()
        entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        entry.pack(pady=10)
        entry.insert(0, str(current_income))
        def save_income():
            income_text = entry.get()
            if not income_text.strip():
                messagebox.showerror("Invalid", "Income cannot be empty.")
                return
            if not validate_input(income_text, 'float'):
                messagebox.showerror("Invalid Input", "Please enter a valid number.")
                return
            self.data["income"] = float(income_text)
            messagebox.showinfo("Success", f"Income updated to ${float(income_text):.2f}")
            popup.destroy()
        save_button = tk.Button(input_frame, text="Save Income", command=save_income, font=("Arial", 11))
        save_button.pack(pady=10)
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
test_dict = {"goals": {}, 
            "budget": {},
            "expenses": [],
            "expenses_history": []}
    
root = tk.Tk()
run = budgetkeeperGUI(root, test_dict)
root.mainloop()

"""Def budget():
While True:
	Introduce user to budgets and goals if first time
	Get all information from json and save it in dictionary
	Display menu as “1. Goals
			     2. Budget Categories
			     4. Quit”
	User picks option
	If goals:
		If goals section of dictionary is empty:
		Introduce user to saving goals and how to create them
		Have user create saving goal
		Else:
			Display goals and percent complete
			Give user options to add to goal, edit goal, and quit
			If add to goal:
				Select goal
				Ask user how much is being added
				Add that much
				Display new goal percentage. If >100, remove goal
			If edit:
				Select goal
				Display all goal information
				User can edit all information
			If quit
				Continue to start of loop
	If budget
		If budget section is empty
		Introduce users to budgets and how to create them
		User creates budget category
			Else:
				Display all budgets and money remaining
				Give user options to add to category,remove from category,  edit category, and quit
				If add:
					Select category
					Ask user how much is being added
					Add to category
				If edit:
					Select category
					Display all stats
					User can edit all information
				If quit:
					Continue to start of loop
		If quit:
			Return from function	
"""