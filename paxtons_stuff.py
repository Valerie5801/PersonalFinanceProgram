from tkinter import *
import matplotlib.pyplot as plt
import csv 
from helpers import sethlog
import numpy as n

def vis_main(username):
    root = Tk()
    root.configure(background="#010136")
    root.minsize(1920, 1080)
    root.maxsize(1920 * 2, 1080 * 2)
    root.geometry("1920x1080+0+0")

    frame = Frame(root, bg="#010136")
    frame.place(relx=0.5, rely=0.8, anchor="s")

    def do_BOT(root, username):
        def show_over_time(category, userdict):
            root.destroy()             
            progress = userdict["goals"][category]["progress"]
            goal = userdict["goals"][category]["amount"]
            print(f"{goal}, {progress}")

            goal_line_x = []
            goal_line_y = []
            savings_labels = []
            for i in range(len(progress)): 
                savings_labels.append(i)

            for i in range(len(progress) - 2, len(progress) + 2):
                goal_line_x.append(i) 
                goal_line_y.append(goal)    

            plt.bar(savings_labels, progress, label="Savings", color="green")
            plt.plot(goal_line_x, goal_line_y, label="Goal", color="red", linestyle="--")                   

            plt.xlabel("Time")
            plt.ylabel("Amount")
            plt.title(f"{category} Progress Over Time")
            plt.legend()

            plt.show()

        def quit(root):
            root.destroy()

        with open("documents/Users.csv") as file:
            userdict = sethlog.get_dict(username)

            for widget in root.winfo_children():
                widget.destroy()

            frame = Frame(root, bg="#010136")
            frame.place(relx=0.5, rely = (len(userdict["goals"].keys()) * 0.15) + 0.3, anchor="s")

            lbl = Label(frame, text="Saving Over Time", font=("Times New Roman", 67, "bold"))
            lbl.config(fg="white", bg="#010136")
            lbl.grid(row=0, column=0, columnspan=2)

            x = 0
            y = 1

            for i in userdict["goals"].keys():
                btn = Button(frame, text=i, command=lambda i=i: show_over_time(i, userdict), width=40, height=5, font=("Times New Roman", 20, "bold"))
                btn.config(fg="white", bg="gray")
                btn.grid(row=y, column=x, padx=50, pady=50)
                if x == 1: y += 1
                if x == 0: x = 1
                elif x == 1: x = 0    

            btn = Button(frame, text="Quit", command=lambda : quit(root), width=40, height=5, font=("Times New Roman", 20, "bold"))
            btn.config(fg="white", bg="gray")
            btn.grid(row=y, column=x, padx=50, pady=50)

        mainloop()

    def do_BP(username):
        userdict = sethlog.get_dict(username)
        labels = []
        amounts = []

        for i in userdict["budget"].keys(): labels.append(i)
        for i in userdict["budget"].values(): amounts.append(i)

        plt.pie(amounts, labels=labels)
        plt.show()

    def quit(root):
        root.destroy()

    lbl = Label(frame, text="Visualization", font=("Times New Roman", 67, "bold"))
    lbl.config(fg="white", bg="#010136")
    lbl.grid(row=0, column=0, columnspan=2)

    btn = Button(frame, text="Budgeting Percentages", command=lambda: do_BP(username), width=40, height=5, font=("Times New Roman", 20, "bold"))
    btn.config(fg="white", bg="gray")
    btn.grid(row=1, column=0, padx=50, pady=50)

    btn2 = Button(frame, text="Budgeting Over Time", command=lambda: do_BOT(root, username), width=40, height=5, font=("Times New Roman", 20, "bold"))
    btn2.config(fg="white", bg="gray")
    btn2.grid(row=1, column=1, padx=50, pady=50)

    btn2 = Button(frame, text="Quit", command=lambda: quit(root), width=40, height=5, font=("Times New Roman", 20, "bold"))
    btn2.config(fg="white", bg="gray")
    btn2.grid(row=2, column=0, padx=50, pady=50)

    lbl2 = Label(frame, text="Click a button to visualize an aspect of your budget", font=("Times New Roman", 30, "bold"))
    lbl2.config(fg="white", bg="#010136")
    lbl2.grid(row=3, column=0, columnspan=2)

    mainloop()