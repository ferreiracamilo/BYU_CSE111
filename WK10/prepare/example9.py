# Example 8

def main():
    try:
        with open("products.vcs", "rt") as products_file:
            for row in products_file:
                print(row)

    except FileNotFoundError as not_found_err:
        print(not_found_err)

if __name__ == "__main__":
    main()