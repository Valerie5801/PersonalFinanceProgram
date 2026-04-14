import tkinter as tk

def show_text():
    x=entry.get()

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Submit", command=show_text)
btn.pack()

root.mainloop()