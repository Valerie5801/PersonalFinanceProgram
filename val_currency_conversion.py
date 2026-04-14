#VY 2nd Currency Conversion
from budgetkeeper import validate_input
import tkinter as tk
from tkinter import messagebox

def currency_conversion(root):
    exist_currencies = ["dollar", "euro", "yen"]
    
    #switch to one single conversion and do formulas instead?
    conversions ={
        "dollar to euro": 0.86,
        "euro to dollar": 1.16,
        "dollar to yen": 159.87,
        "yen to dollar": 0.0063,
        "euro to yen": 185.03,
        "yen to euro": 0.0054
    }

    """create a popup window with a close button. Taken from Zane's class"""
    popup = tk.Toplevel(root)
    popup.title("Currency Conversion")
    popup.geometry("600x500")
    popup.configure(background="pale goldenrod")
    content_frame = tk.Frame(popup, bg="pale goldenrod")
    content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    # Close button at the bottom
    close_button = tk.Button(popup, text="Close", command=popup.destroy, bg="lightcoral", font=("Arial", 12))
    close_button.pack(pady=10)

    #get the start and end currencies
    first_currency = tk.StringVar(value=exist_currencies[0])
    second_currency = tk.StringVar(value=exist_currencies[1])

    tk.Label(content_frame, text="Select Starting Currency:", bg="pale goldenrod", font=(12)).pack()
    tk.OptionMenu(content_frame, first_currency, *exist_currencies).pack(pady=(0, 25))

    tk.Label(content_frame, text="Select End Currency:", bg="pale goldenrod", font=(12)).pack()
    tk.OptionMenu(content_frame, second_currency, *exist_currencies).pack()

    #get money input
    tk.Label(content_frame, text="Amount to convert:", bg="pale goldenrod", font=(15)).pack(pady=(50, 0))

    start_money = tk.Entry(content_frame)
    start_money.pack()
    
    #inner function for the conversion itself as well as grammar checking
    def conversion():
        get_first_currency = first_currency.get()
        get_second_currency = second_currency.get()
        get_start_money = start_money.get()

        if get_first_currency == get_second_currency:
            messagebox.showerror("Error", "Please choose different currencies for the start and ending currencies.")
            return

        if not validate_input(get_start_money, "float"):
            messagebox.showerror("Error", "Please type in a number.")
            return

        get_start_money = float(get_start_money)

        chosen_conversion = get_first_currency + " to " + get_second_currency
        end_money = conversions[chosen_conversion] * get_start_money

        #for grammar's sake, put an "s" at the end of the currency name if it isn't yen.
        if get_first_currency == "yen":
            print_first = "yen"
        else:
            print_first = get_first_currency + "s"

        if get_second_currency == "yen":
            print_second = "yen"
        else:
            print_second = get_second_currency + "s"

        result_label.config(
            text=f"{get_start_money} {print_first} is {end_money:.2f} {print_second}"
        )


    result_label = tk.Label(content_frame, text="", bg="pale goldenrod", font=(15))
    result_label.pack(pady=(25, 25))
    #make a button to actually convert
    convert_btn = tk.Button(content_frame, text="Convert Currencies", command=conversion, font=(15))
    convert_btn.pack(pady=(25, 10))