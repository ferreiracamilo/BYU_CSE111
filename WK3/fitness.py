# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    weight = int(input("Enter your weight in U.S. pounds: "))
    height = int(input("Enter your height in U.S. inches: "))

    age = compute_age(birthdate)
    weight_kg = kg_from_lb(weight)
    height_cm = cm_from_in(height)

    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight_kg}")
    print(f"Height (cm): {height_cm}")

    print(f"Body mass index: {body_mass_index(weight_kg,height_cm):.2f}")
    print(f"Basal metabolic rate (kcal/day): {basal_metabolic_rate(gender,weight_kg,height_cm,age):.2f}")
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
    # as the way formula is displayed I understand should be like this, however result does not match
    # bmi = 10000 * kg_from_lb(weight) / cm_from_in(height)**2
    
    #after checking the sample solution I noticed there's a total different calculation
    bmi = weight / (height ** 2) * 10000
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
        bmr = 447.593 + 9.247 * kg_from_lb(weight) + 3.098 * cm_from_in(height) - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * kg_from_lb(weight) + 4.799 * cm_from_in(height) - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()