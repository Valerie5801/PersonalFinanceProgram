import json
import csv
def validate_input(text, kind='int'):
    test_to_check = str(text).strip().capitalize()
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
        return test_to_check.isalpha()
    else:
        return False


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
test_dict = {"goals": {}, 
             "budget": {},
             "expenses" : 0}
def budget(dict):
    while True:
        print("Welcome to the budget keeper!")
        print("1. Goals")
        print("2. Budget Categories")
        print("3. edit income")
        choice = input("Please select an option: ")
        if choice == '1':
            if dict["goals"] == {}:
                print("Welcome to the goals section! Here you can create saving goals and track your progress towards them.")
                pass
            else:
                print("Here are your current goals and their progress:")
                for goal, info in dict["goals"].items():
                    percent_complete = (info["progress"] / info["amount"]) * 100
                    print(f"{goal}: {percent_complete:.2f}% complete")
                print("Options:")
                print("1. Add to goal")
                print("2. Edit goal")
                print("3. Create Goal")
                print("4. Quit")
                goal_choice = input("Please select an option: ")
                if goal_choice == '1':
                    pass
                    count = 1
                    for x in dict["goals"].keys():
                        print(f"{count}. {x}")
                        count += 1
                    print ("Select a goal to add to:")
                    goal_selection = int(input("Enter the number of the goal: "))
                    goal_to_edit = list(dict["goals"].keys())[goal_selection - 1]
                    print(f"How much would you like to add to {goal_to_edit}?")
                    amount_to_add = float(input("Enter the amount: "))
                    dict["goals"][goal_to_edit]["progress"] += amount_to_add
                    new_percent_complete = (dict["goals"][goal_to_edit]["progress"] / dict["goals"][goal_to_edit]["amount"]) * 100
                    print(f"New progress for {goal_to_edit}: {new_percent_complete:.2f}% complete")
                    dict["expenses"] = dict["expenses"] + amount_to_add
                elif goal_choice == '2':
                    count = 1
                    for x in dict["goals"].keys():
                        print(f"{count}. {x}")
                        count += 1
                    print ("Select a goal to edit:")
                    while True:
                        goal_selection = int(input("Enter the number of the goal: "))
                        if goal_selection not in range(1, count):
                            print ("please enter a valid selection value")
                            continue
                        break
                    goal_to_edit = list(dict["goals"].keys())[goal_selection - 1]
                    print(f"Current information for {goal_to_edit}:")
                    print(f"Amount: ${dict['goals'][goal_to_edit]['amount']}")
                    old_progress = dict['goals'][goal_to_edit]['progress']
                    print(f"Progress: ${dict['goals'][goal_to_edit]['progress']}")
                    while True:
                        while True:
                            new_amount = input("Enter new goal total (or press enter to keep current): ") or dict['goals'][goal_to_edit]['amount']
                            if not validate_input(new_amount, 'int'):
                                print ("please enter an integer value")
                                continue
                            break
                        new_amount = float(new_amount)
                        while True:
                            new_progress = input("Enter new progress (or press enter to keep current): ") or dict['goals'][goal_to_edit]['progress']
                            if not validate_input(new_progress, 'int'):
                                print ("please enter an integer value")
                                continue
                            break
                        new_progress = float(new_progress)
                        if new_progress > new_amount:
                            print ("Your new progress cannot be greater than the total. \n please reenter the information.")
                            continue
                        break
                    dict["goals"][goal_to_edit]["amount"] = new_amount
                    dict["goals"][goal_to_edit]["progress"] = new_progress
                    print(f"Updated information for {goal_to_edit}:")
                    print(f"Total: ${dict['goals'][goal_to_edit]['amount']}")
                    print(f"Progress: ${dict['goals'][goal_to_edit]['progress']}")
                    change = old_progress - dict['goals'][goal_to_edit]['progress']
                    dict["expenses"] += change
                elif goal_choice == '3':
                    goal_name = input("Enter the name of the new goal: ")
                    while True:
                        goal_amount = input("Enter the total amount for the new goal: ")
                        if not validate_input(goal_amount, 'int'):
                            print ("please enter an integer value")
                            continue
                        break
                    goal_amount = float(goal_amount)
                    dict["goals"][goal_name] = {"amount": goal_amount, "progress": [0]}
                    print(f"New goal {goal_name} created with total amount ${goal_amount}. this goal has no progress yet, but you can edit this goal to add progress or add to it using the add to goal option.")
                elif goal_choice == '4':
                    continue
                else:
                    print("Invalid option, please try again.")
        elif choice == '2':
            if dict["budget"] == {}:
                print("Welcome to the budget categories section! Here you can create budget categories and track your spending.")
            print("Here are your current budget categories and their remaining amounts:")
            for category, info in dict["budget"].items():
                print(f"{category}: ${info['remaining']} remaining")
            print("Options:")
            print("1. Add to category")
            print("2. Edit category")
            print("3. create category")
            print("4. Quit")
            budget_choice = input("Please select an option: ")
            if budget_choice == '1':
                count = 1
                for x in dict["budget"].keys():
                    print(f"{count}. {x}")
                    count += 1
                print ("Select a category to add to:")
                category_selection = int(input("Enter the number of the category: "))
                amount_to_add = float(input("Enter the amount to add: "))
                category_to_edit = list(dict["budget"].keys())[category_selection - 1]
                dict["budget"][category_to_edit]["remaining"] += amount_to_add
                print(f"New remaining amount for {category_to_edit}: ${dict['budget'][category_to_edit]['remaining']}")
                dict["expenses"] += amount_to_add
            elif budget_choice == '2':
                count = 1
                for x in dict["budget"].keys():
                    print(f"{count}. {x}")
                    count += 1
                print ("Select a category to edit:")
                while True:
                    category_selection = int(input("Enter the number of the category: "))
                    if category_selection not in range(1, count-1):
                        print ("please enter a valid selection value")
                        continue
                    break
                category_to_edit = list(dict["budget"].keys())[category_selection - 1]
                print(f"Current information for {category_to_edit}:")
                print(f"Amount: ${dict['budget'][category_to_edit]['amount']}")
                old_remainder = dict['budget'][category_to_edit]['remaining']
                print(f"Remaining: ${dict['budget'][category_to_edit]['remaining']}")

                while True:
                    while True:
                        new_amount = input("Enter new category total (or press enter to keep current): ") or dict['budget'][category_to_edit]['amount']
                        if not validate_input(new_amount, 'int'):
                            print ("please enter an integer value")
                            continue
                        break
                    new_amount = float(new_amount)
                    while True:
                        new_remaining = input("Enter new remaining amount (or press enter to keep current): ") or dict['budget'][category_to_edit]['remaining']
                        if not validate_input(new_remaining, 'int'):
                            print ("please enter an integer value")
                            continue
                        break
                    new_remaining = float(new_remaining)
                    if new_remaining > new_amount:
                        print ("Your new remaining amount cannot be greater than the total. \n please reenter the information.")
                        continue
                    break
                dict["budget"][category_to_edit]["amount"] = new_amount
                dict["budget"][category_to_edit]["remaining"] = new_remaining
                print(f"Updated information for {category_to_edit}:")
                print(f"Total: ${dict['budget'][category_to_edit]['amount']}")
                print(f"Remaining: ${dict['budget'][category_to_edit]['remaining']}")
                change = old_remainder - dict['budget'][category_to_edit]['remaining']
                dict["expenses"] += change
            elif budget_choice == '3':
                category_name = input("Enter the name of the new category: ")
                while True:
                    category_amount = input("Enter the total amount for the new category: ")
                    if not validate_input(category_amount, 'int'):
                        print ("please enter an integer value")
                        continue
                    break
                category_amount = float(category_amount)
                dict["budget"][category_name] = {"amount": category_amount, "remaining": category_amount}
                print(f"New category {category_name} created with total amount ${category_amount}. this category has no expenses yet, but you can edit this category to add expenses or add to it using the add to category option.")
            elif budget_choice == '4':
                continue
            else:
                print("Invalid option, please try again.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
    return dict
def get_from_csv(file):
    with open(file, "r") as r:
        reader = csv.DictReader(r)
        data_dict = {"goals": {}, "budget": {}, "expenses": 0}
        
        for row in reader:
            if row["type"].lower() == "goal":
                data_dict["goals"][row["name"]] = {"amount": float(row["amount"]),"progress": float(row["progress"])}
            elif row["type"].lower() == "budget":
                data_dict["budget"][row["name"]] = {"amount": float(row["amount"]),"remaining": float(row["remaining"])}
            elif row["type"].lower() == "expenses":
                data_dict["expenses"] = float(row["amount"])
        return data_dict