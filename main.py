#this is the main file

from helpers.sethlog import *
from budgetkeeper import *



def menu():
    username=False
    while True:
        if username:
            while True:
                dict = puldict(username)
                inp=input("What would you like to do\n(1)Budgeting and saving goals\n(2) Convert Currency\n(3)finances over time \n(4) Logout")
                match inp:
                    case '1':
                        root = tk.Tk()
                        run = guipage(root, dict)
                        root.mainloop()
                    case '2':
                        #convert currency
                        break
                    case '3':
                        #finances over time
                        break
                    case '4':
                        username=logout(username)
                        break
                    case _:
                        continue
        else: 
            while True:
                """inp=input("What would you like to do\n(1) Login\n(2) Register")"""
                inp = simpledialog.askstring(" ", "What would you like to do\n(1) Login\n(2) Register")
                match inp:
                    case '1':
                        username=login()
                        dictionary= puldict(username)
                        break
                    case '2':
                        username=register()
                        
                        break
                    case _:
                        continue

menu()
