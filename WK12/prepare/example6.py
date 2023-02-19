# Example 6

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis",
        "81-298-9238": "Sama Patel"
    }

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Lookup the student ID in the dictionary and
    # retrieve the corresponding student name.
    name = students.get(id)

    if name:
        # Print the student name.
        print(name)

        # Remove the student that the user
        # specified from the dictionary.
        students.pop(id)
    else:
        print("No such student")
    print()

    # Use a for loop to print each key value pair
    # in the dictionary. Of course, the code in
    # the body of a loop can do much more with
    # each key value pair than simply print it.
    for key, value in students.items():
        print(key, value)


# Call main to start this program.
if __name__ == "__main__":
    main()