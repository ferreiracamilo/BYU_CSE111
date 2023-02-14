    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students:

        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students[id]

        # Print the student's name.
        print(name)

    else:
        print("No such student")