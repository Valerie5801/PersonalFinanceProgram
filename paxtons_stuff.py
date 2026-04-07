from tkinter import *

root = Tk()
root.title("Button Clicker")
root.configure(background="#010136")
root.minsize(300, 300)
root.maxsize(1920, 1080)
root.geometry("1920x1080+0+0")

frame = Frame(root, bg="#010136")
frame.place(relx=0.5, rely=0.5, anchor="s")

lbl = Label(frame, text="Visualization", font=("Times New Roman", 67, "bold"))
lbl.config(fg="white", bg="#010136")
lbl.grid(row=0, column=0, columnspan=2)

btn = Button(frame, text="CLICK ME", width=40, height=20, font=("Times New Roman", 10, "bold"))
btn.config(fg="white", bg="gray")
btn.grid(row=1, column=0, padx=20)

btn = Button(frame, text="CLICK ME", width=40, height=20, font=("Times New Roman", 10, "bold"))
btn.config(fg="white", bg="gray")
btn.grid(row=1, column=1, padx=20)


root.mainloop()