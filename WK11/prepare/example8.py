# Example 8

def main():
    # Create a list that contains data about young students.
    students = [
        # [given_name, surname, reading_level]
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8]
    ]

    GIVEN_INDEX = 0
    SURNAME_INDEX = 1

    # Define a lambda function that combines
    # a student's surname and given name.
    combine_names = lambda student_list: \
        f"{student_list[SURNAME_INDEX]}, {student_list[GIVEN_INDEX]}"

    # Sort the list by the combined key of surname, given_name.
    sorted_list = sorted(students, key=combine_names)

    # Print the list.
    for student in sorted_list:
        print(student)


# Call main to start this program.
if __name__ == "__main__":
    main()