# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    

    Please enter your gender (M or F): F
    Enter your birthdate (YYYY-MM-DD): 2001-03-21
    Enter your weight in U.S. pounds: 125
    Enter your height in U.S. inches: 54
    Age (years): 19
    Weight (kg): 56.70
    Height (cm): 137.2
    Body mass index: 30.1
    Basal metabolic rate (kcal/day): 1315
    # Get the user's gender, birthdate, height, and weight.

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    mass_kg = 0.453592 * pounds
    return mass_kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    length_cm = 2.54 * inches
    return length_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000 * kg_from_lb(weight) / cm_from_in(height)**2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    bmr = 0
    if gender.upper == "F":
        #mujer
        # bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
        bmr = 447.593 + 9.247 * kg_from_lb(weight) + 3.098 * cm_from_in(height) - 4.330 * age
    else:
        #hombre
        # bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age
        bmr = 88.362 + 13.397 * kg_from_lb(weight) + 4.799 * cm_from_in(height) - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.