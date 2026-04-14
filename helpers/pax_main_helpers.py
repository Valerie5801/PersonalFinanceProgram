import tkinter as tk
from helpers.sethlog import *
import budgetkeeper as BK
import val_currency_conversion as VCC
import paxtons_stuff as PS
import val_income_expenses as VIE

def login_register():
    root = tk.Tk()
    root.configure(background="#010136")
    root.minsize(1920, 1080)
    root.maxsize(1920 * 2, 1080 * 2)
    root.geometry("1920x1080+0+0")

    usertemp = tk.StringVar()

    def login_spec(root):
        name = login(root)
        usertemp.set(name)
        root.destroy()

    def register_spec(root):
        name = register(root)
        usertemp.set(name)
        root.destroy()

    frame = tk.Frame(root, bg="#010136")
    frame.place(relx=0.5, rely=0.6, anchor="s")

    lbl = tk.Label(frame, text="Personal Finances", font=("Times New Roman", 67, "bold"))
    lbl.config(fg="white", bg="#010136")
    lbl.grid(row=0, column=0, columnspan=2)

    lbl = tk.Label(frame, text="Login/Register to begin", font=("Times New Roman", 33, "bold"))
    lbl.config(fg="white", bg="#010136")
    lbl.grid(row=1, column=0, columnspan=2)

    btn = tk.Button(frame, text="Log In", command=lambda : login_spec(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
    btn.config(fg="white", bg="gray")
    btn.grid(row=2, column=0, padx=50, pady=50)

    btn = tk.Button(frame, text="Register", command=lambda : register_spec(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
    btn.config(fg="white", bg="gray")
    btn.grid(row=2, column=1, padx=50, pady=50)
    
    tk.mainloop()
    username = usertemp.get()
    return username

def main_menu():
    username=''
    while True:
        if bool(username):
            root = tk.Tk()
            root.configure(background="#010136")
            root.minsize(1920, 1080)
            root.maxsize(1920 * 2, 1080 * 2)
            root.geometry("1920x1080+0+0")

            frame = tk.Frame(root, bg="#010136")
            frame.place(relx=0.5, rely=0.95, anchor="s")

            lbl = tk.Label(frame, text=f"Welcome, {username}", font=("Times New Roman", 67, "bold"))
            lbl.config(fg="white", bg="#010136")
            lbl.grid(row=0, column=0, columnspan=2)

            lbl = tk.Label(frame, text="Select an option to get started", font=("Times New Roman", 33, "bold"))
            lbl.config(fg="white", bg="#010136")
            lbl.grid(row=1, column=0, columnspan=2)

            btn = tk.Button(frame, text="Budgetting/Savings Goals", command=lambda : budgetting(username), width=40, height=5, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=2, column=0, padx=50, pady=50)

            btn = tk.Button(frame, text="Currency Converter", command=lambda : VCC.currency_conversion(root), width=40, height=5, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=2, column=1, padx=50, pady=50)

            btn = tk.Button(frame, text="Visualization", command=lambda : PS.vis_main(username), width=40, height=5, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=3, column=0, padx=50, pady=50)

            btn = tk.Button(frame, text="Income/Expenses", command=lambda : income(username), width=40, height=5, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=3, column=1, padx=50, pady=50)

            btn = tk.Button(frame, text="Quit", command=lambda : logout_fr(root), width=40, height=5, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=4, column=0, padx=50, pady=50)

            root.mainloop()

        else: 
            username = login_register()

def budgetting(username):
    dataRaw = get_dict(username)
    dataRaw["username"] = username
    root = tk.Tk() 
    budgetGUI = BK.budgetkeeperGUI(root, dataRaw)    
    budgetGUI.setup_main_menu()

def income(username):
    dataRaw = get_dict(username)
    dataRaw["username"] = username
    root = tk.Tk() 
    budgetGUI = VIE.IncomeExpenseGUI(root, dataRaw)    

def logout_fr(root):
    root.destroy()