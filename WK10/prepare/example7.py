# Example 7

def main():
    try:
        # Create a dictionary with student IDs as
        # the keys and student names as the values.
        students = {
            "42-039-4736": "Clint Huish",
            "61-315-0160": "Amelia Davis",
            "10-450-1203": "Ana Soares",
            "75-421-2310": "Abdul Ali",
            "07-103-5621": "Amelia Davis"
        }

        # Attempt to find the key "50-420-1021",
        # which is not in the dictionary. This will
        # cause the computer to raise a KeyError.
        name = students["50-420-1021"]

        print(name)

    except KeyError as key_err:
        print(key_err)
        print(type(key_err))
        print(type(key_err).__name__)
        print(type(key_err).__name__, key_err)

if __name__ == "__main__":
    main()