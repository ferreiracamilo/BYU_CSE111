# Example 3

def main():
    try:
        number = float(input("Please enter a number: "))
        print(number)

    except ValueError as val_err:
        print(val_err)

if __name__ == "__main__":
    main()