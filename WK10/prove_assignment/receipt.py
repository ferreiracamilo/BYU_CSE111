import csv
from datetime import datetime
from os import path

def buildPath(file_name):
    file_name_path = path.join(path.dirname(__file__), file_name)
    return file_name_path

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    outcome_dictionary = {}
    with open(buildPath(filename), "rt") as input_file:
        reader = csv.reader(input_file)
        next(reader)
        for row_list in reader:
            key_dict = row_list[key_column_index]
            qty_columns = len(row_list)
            value_dict = []
            for i in range(qty_columns):
                if i != key_column_index:
                    column_data = row_list[i]
                    if column_data.isnumeric():
                        value_dict.append(float(column_data))    
                    else:
                        value_dict.append(column_data)
            if key_dict not in outcome_dictionary:
                outcome_dictionary[key_dict] = value_dict
            else:
                value_dict_check = value_dict
                number_check = outcome_dictionary[key_dict]
                new_number = 0
                if value_dict_check != number_check:
                    new_number = value_dict_check[0] + number_check[0]
                new_list = [new_number]
                outcome_dictionary[key_dict] = new_list
    return outcome_dictionary


def main():
    products_dict = read_dictionary("products.csv",0)
    print(products_dict)
    request_dict = read_dictionary("request.csv",0)
    print(products_dict)
    print("\nRequested Items")
    for product_id in request_dict:
        quantity = request_dict[product_id]
        # Print the product name, requested quantity, and product price.
        product_name_index = 0
        product_price_index = 1
        product_name = products_dict[product_id][product_name_index]
        product_price = products_dict[product_id][product_price_index]
        print(f"{product_name}: {quantity} @ {product_price}")
        # wheat bread: 2 @ 2.55


# Call main to start this program.
if __name__ == "__main__":
    main()