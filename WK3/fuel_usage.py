def main():
    first_odometer_var = int(input("Enter the first odometer reading (miles): "))
    second_odometer_var = int(input("Enter the second odometer reading (miles): "))
    amount_fuel_var = float(input("Enter the amount of fuel used (gallons): "))
    mpg = miles_per_gallon(first_odometer_var,second_odometer_var,amount_fuel_var)
    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg:.2f} miles per gallon") #In example result is rounded up
    print(f"{lp100k:.2f} liters per 100 kilometers")

    pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg_res = (end_miles - start_miles) / amount_gallons
    return mpg_res

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k_res = 235.215 / mpg
    return lp100k_res

# Call the main function so that
# this program will start executing.
main()