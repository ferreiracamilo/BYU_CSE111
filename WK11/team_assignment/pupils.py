import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(list_students):
    """prints each element of the list on a separate line.

    Args:
        list_students (_type_): Compound list containing students information
    """
    for student in list_students:
        print(student)


def main():
    list_students = read_compound_list("WK11/team_assignment/pupils.csv")
    print_list(list_students)
    
    # Sort the list of students by birthdate
    birthdate_func = lambda student: student[BIRTHDATE_INDEX]
    sorted_list_by_birthdate = sorted(list_students, key=birthdate_func)
    print()
    print_list(sorted_list_by_birthdate)

    # Sort the list of students by birthdate
    givenName_func = lambda student: student[GIVEN_NAME_INDEX]
    sorted_list_by_givenName = sorted(list_students, key=givenName_func)
    print()
    print_list(sorted_list_by_givenName)



# Call main to start this program.
if __name__ == "__main__":
    main()