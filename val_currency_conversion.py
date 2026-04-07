#VY 2nd Currency Conversion

#only put here for early testing, later take from helper functions
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


def currency_conversion():
    exist_currencies = ["dollar", "euro", "yen"]
    avail_currencies = exist_currencies #duplicate this since avail_currencies will be messed with
    #switch to one single conversion and do formulas instead?
    conversions ={
        "dollar to euro": 0.86,
        "euro to dollar": 1.16,
        "dollar to yen": 159.87,
        "yen to dollar": 0.0063,
        "euro to yen": 185.03,
        "yen to euro": 0.0054
    }

    def check_currency():
        while True:
            chosen_currency = input("Type your chosen currency: ").strip().lower()
            if chosen_currency in avail_currencies:
                return chosen_currency
            else:
                print('That is not an available currency. Please type it out fully (for example, instead of "USD" type out "dollar")')
        
    print("Here are the available currencies:")
    for currency in avail_currencies:
        print(f"-{currency.capitalize()}")
    print("\nPlease select the currency you want to start with.")
    first_currency = check_currency()

    avail_currencies.remove(first_currency)
    print("\nPlease select the currency you want to convert to.")
    print("Here are the available currencies:")
    for currency in avail_currencies:
        print(f"-{currency.capitalize()}")
    second_currency = check_currency()

    chosen_conversion = first_currency + " to " + second_currency

    while True:
        #for grammar's sake...put an s on dollar and euro but not when it's yen
        print_first = ""
        print_second = ""
        if first_currency == "yen":
            print_first = "yen"
        else:
            print_first = first_currency + "s"

        if second_currency == "yen":
            print_second = "yen"
        else:
            print_second = second_currency + "s"


        start_money = input(f"\nType the starting money (in {print_first}): ")
        check_money = validate_input(start_money, "float")
        if check_money:
            start_money = float(start_money)
            break
        else:
            print("That isn't a numerical value.")

    end_money = conversions[chosen_conversion] * start_money

    print(f"{start_money} {print_first} is {end_money} {print_second}.")

currency_conversion()