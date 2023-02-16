# Example 4

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Define a lambda function that converts
    # a Fahrenheit temperature to Celsius and
    # returns the Celsius temperature.
    cels_from_fahr = lambda fahr: round((fahr - 32) * 5 / 9, 1)
    integer_yet = 3

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))
    celd_temps = list(map(integer_yet, fahr_temps)) #MAP WILL IDENTIFY IF ITS FUNCTION OR LAMBA WHICH IS STORE AT A VAR

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


# Call main to start this program.
if __name__ == "__main__":
    main()