# Example 8

def main():
    try:
        with open("products.vcs", "rt") as products_file:
            for row in products_file:
                print(row)

    except Exception as excep:
        print(excep)

if __name__ == "__main__":
    main()