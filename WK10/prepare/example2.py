# Example 2

def main():
    try:
        text = input("Please enter a number: ")
        integer = round(text)
        print(integer)

    except TypeError as type_err:
        print(type_err)

if __name__ == "__main__":
    main()