from tkinter import *
from matplotlib import *   
import csv 

def vis_main():
    running = True
    while running:
        root = Tk()
        root.configure(background="#010136")
        root.minsize(1920, 1080)
        root.maxsize(1920 * 2, 1080 * 2)
        root.geometry("1920x1080+0+0")

        frame = Frame(root, bg="#010136")
        frame.place(relx=0.5, rely=0.6, anchor="s")

        def do_BOT(root):
            def saving_over_time():
                def show_over_time(category):
                    root.destroy()
                    with open("documents/Users.csv") as file:
                        pass

                for widget in root.winfo_children():
                    widget.destroy()

                frame = Frame(root, bg="#010136")
                frame.place(relx=0.5, rely=0.9, anchor="s")

                lbl = Label(frame, text="Saving Over Time", font=("Times New Roman", 67, "bold"))
                lbl.config(fg="white", bg="#010136")
                lbl.grid(row=0, column=0, columnspan=2)

                btn = Button(frame, text="Vehicle", command=lambda: show_over_time("New Car"), width=40, height=5, font=("Times New Roman", 20, "bold"))
                btn.config(fg="white", bg="gray")
                btn.grid(row=1, column=0, padx=50, pady=50)

                btn2 = Button(frame, text="Vacation", command=lambda: show_over_time("Vacation"), width=40, height=5, font=("Times New Roman", 20, "bold"))
                btn2.config(fg="white", bg="gray")
                btn2.grid(row=1, column=1, padx=50, pady=50)

                btn2 = Button(frame, text="Emergency Fund", command=lambda: show_over_time("Emergency Fund"), width=40, height=5, font=("Times New Roman", 20, "bold"))
                btn2.config(fg="white", bg="gray")
                btn2.grid(row=2, column=0, padx=50, pady=50)

                btn2 = Button(frame, text="Budget", width=40, command=lambda: show_over_time("Budget"), height=5, font=("Times New Roman", 20, "bold"))
                btn2.config(fg="white", bg="gray")
                btn2.grid(row=2, column=1, padx=50, pady=50)

                btn2 = Button(frame, text="Entertainment", command=lambda: show_over_time("Entertainment"), width=40, height=5, font=("Times New Roman", 20, "bold"))
                btn2.config(fg="white", bg="gray")
                btn2.grid(row=3, column=0, padx=50, pady=50)

                btn2 = Button(frame, text="Bills", width=40, command=lambda: show_over_time("Bills"), height=5, font=("Times New Roman", 20, "bold"))
                btn2.config(fg="white", bg="gray")
                btn2.grid(row=3, column=1, padx=50, pady=50)

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

        def do_BP(root):
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

        btn2 = Button(frame, text="Budgeting Over Time", command=lambda: do_BOT(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
        btn2.config(fg="white", bg="gray")
        btn2.grid(row=1, column=1, padx=50, pady=50)

        lbl2 = Label(frame, text="Click a button to visualize an aspect of your budget", font=("Times New Roman", 30, "bold"))
        lbl2.config(fg="white", bg="#010136")
        lbl2.grid(row=2, column=0, columnspan=2)

        mainloop()

vis_main()