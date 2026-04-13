from tkinter import *
import matplotlib.pyplot as plt
import csv 
from helpers import sethlog
import numpy as n

def vis_main(username):
    running = True
    while running:
        root = Tk()
        root.configure(background="#010136")
        root.minsize(1920, 1080)
        root.maxsize(1920 * 2, 1080 * 2)
        root.geometry("1920x1080+0+0")

        frame = Frame(root, bg="#010136")
        frame.place(relx=0.5, rely=0.6, anchor="s")

        def do_BOT(root, username):
            def saving_over_time():
                userdict = {"goals": {"New Car": {"amount": 10000, "progress":[7000.0]},
        "Vacation": {"amount": 5000, "progress": [2000]},
        "Emergency Fund": {"amount": 2000, "progress": [1500, 1600, 1700, 1800]}}, 
"budget": {"Food": {"amount": 500, "remaining": 200}, 
        "Entertainment": {"amount": 300, "remaining": 150}, 
        "Bills": {"amount": 1000, "remaining": 800}}, 
"expenses": [2000.0],
"income":[]}    
                def show_over_time(category, userdict):
                    root.destroy()
                    with open("documents/Users.csv") as file:                   
                        progress = userdict["goals"][category]["progress"]
                        goal = userdict["goals"][category]["amount"]
                        print(f"{goal}, {progress}")

                        goal_line = [goal] * len(progress)

                        plt.bar(progress, progress, label="Progress")
                        plt.plot(goal_line, goal_line, label="Goal", color="red", linestyle="--")

                        plt.xlabel("Time")
                        plt.ylabel("Amount")
                        plt.title(f"{category} Progress Over Time")
                        plt.legend()

                        plt.show()

                for widget in root.winfo_children():
                    widget.destroy()

                frame = Frame(root, bg="#010136")
                frame.place(relx=0.5, rely = len(userdict) * 0.15, anchor="s")

                lbl = Label(frame, text="Saving Over Time", font=("Times New Roman", 67, "bold"))
                lbl.config(fg="white", bg="#010136")
                lbl.grid(row=0, column=0, columnspan=2)

                x = 0
                y = 1

                for i in userdict["goals"].keys():
                    btn = Button(frame, text=i, command=lambda: show_over_time(i, userdict), width=40, height=5, font=("Times New Roman", 20, "bold"))
                    btn.config(fg="white", bg="gray")
                    btn.grid(row=y, column=x, padx=50, pady=50)
                    if x == 1: y += 1
                    if x == 0: x = 1
                    elif x == 1: x = 0
                    

            root.title("Budgeting Over Time")

            for widget in root.winfo_children():
                widget.destroy()

            frame = Frame(root, bg="#010136")
            frame.place(relx=0.5, rely=0.9, anchor="s")

            lbl = Label(frame, text="Budgeting Over Time", font=("Times New Roman", 67, "bold"))
            lbl.config(fg="white", bg="#010136")
            lbl.grid(row=0, column=0, columnspan=2)

            btn = Button(frame, text="Income", width=40, height=10, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=1, column=0, padx=50, pady=50)

            btn2 = Button(frame, text="Spending", width=40, height=10, font=("Times New Roman", 20, "bold"))
            btn2.config(fg="white", bg="gray")
            btn2.grid(row=1, column=1, padx=50, pady=50)

            btn2 = Button(frame, text="Savings", command=saving_over_time, width=40, height=10, font=("Times New Roman", 20, "bold"))
            btn2.config(fg="white", bg="gray")
            btn2.grid(row=2, column=0, padx=50, pady=50)

            mainloop()

        def do_BP(root, username):
            root.title("Budgeting Percentages")

            for widget in root.winfo_children():
                widget.destroy()

            frame = Frame(root, bg="#010136")
            frame.place(relx=0.5, rely=0.9, anchor="s")

            lbl = Label(frame, text="Budgeting Percentages", font=("Times New Roman", 67, "bold"))
            lbl.config(fg="white", bg="#010136")
            lbl.grid(row=0, column=0, columnspan=2)

            btn = Button(frame, text="Income", width=40, height=10, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=1, column=0, padx=50, pady=50)

            btn2 = Button(frame, text="Spending", width=40, height=10, font=("Times New Roman", 20, "bold"))
            btn2.config(fg="white", bg="gray")
            btn2.grid(row=1, column=1, padx=50, pady=50)

            btn2 = Button(frame, text="Savings", width=40, height=10, font=("Times New Roman", 20, "bold"))
            btn2.config(fg="white", bg="gray")
            btn2.grid(row=2, column=0, padx=50, pady=50)

            mainloop()


        lbl = Label(frame, text="Visualization", font=("Times New Roman", 67, "bold"))
        lbl.config(fg="white", bg="#010136")
        lbl.grid(row=0, column=0, columnspan=2)

        btn = Button(frame, text="Budgeting Percentages", width=40, height=10, font=("Times New Roman", 20, "bold"))
        btn.config(fg="white", bg="gray")
        btn.grid(row=1, column=0, padx=50, pady=50)

        btn2 = Button(frame, text="Budgeting Over Time", command=lambda: do_BOT(root, username), width=40, height=10, font=("Times New Roman", 20, "bold"))
        btn2.config(fg="white", bg="gray")
        btn2.grid(row=1, column=1, padx=50, pady=50)

        lbl2 = Label(frame, text="Click a button to visualize an aspect of your budget", font=("Times New Roman", 30, "bold"))
        lbl2.config(fg="white", bg="#010136")
        lbl2.grid(row=2, column=0, columnspan=2)

        mainloop()

vis_main("john")