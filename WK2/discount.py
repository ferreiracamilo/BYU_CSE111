from datetime import datetime

def switch_day(argument):
    #By definition itselft SWICH is not available for python, so I had to work on this way
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return switcher.get(argument, "Invalid month")

subtotal = 0 #Initial value assigned to enforce while execution

dt = datetime.now()
wkday_num = dt.weekday()


while subtotal == 0:
    subtotal = float(input("Please enter the subtotal: "))
    wkday_num = 4 #Friday
    #wkday_num = 2 #Tuesday
    if (switch_day(wkday_num) == 'Tuesday' or switch_day(wkday_num) == 'Wednesday'):
        if subtotal >= 50:
            subtotal = subtotal * 0.9
        else:
            print(f"You are {50-subtotal} dollars away from getting your discount")
    tax = subtotal * 0.06
    final = subtotal+tax
    
    print(switch_day(wkday_num))
    print(f"Sales tax amount is {tax}")
    print(f"Total: {final:.2f}")

# On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
# Please enter the subtotal: 42.75
# Sales tax amount: 2.56
# Total: 45.31