# Example 9

def main():
    try:
        with open("contacts.csv", "rt") as contacts_file:
            for row in contacts_file:
                print(row)

    except PermissionError as perm_err:
        print(perm_err)

if __name__ == "__main__":
    main()