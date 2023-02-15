import csv
from datetime import datetime
from os import path
import copy

def is_float(a_string):
    """Check if a string is possible to be cast into float
        This method is built due to .isnumeric not identifying correclty all numbers

    Args:
        a_string (_type_): A string to be review

    Returns:
        boolean: It will state if a number is number or not
    """
    try:
        float(a_string)
        return True
    except ValueError:
        return False

def buildPath(file_name):
    """Generate dinamically the path for the file to reach

    Args:
        file_name (String): file name to reach within the same folder that contains the .py file

    Returns:
        Sting: full path to locate file to reach
    """
    file_name_path = path.join(path.dirname(__file__), file_name)
    return file_name_path

def current_datet_formatted():
    """Return the current date formatted to print on the receipt

    Returns:
        String: Current date time string formatted per prove assignment requirement
    """
    current_date_and_time = datetime.now()
    current_date_time_formatted = f"{current_date_and_time:%A %I:%M %p}"
    return current_date_time_formatted

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
                    if is_float(column_data):
                    #if column_data.isnumeric():
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

def combine_product_request(request_dict,products_dict):
    """Return a combination of the products dictionary and the request dictionary.
        This will make easier to print the receipt.

    Args:
        request_dict (dictionary): Dictionary containing the request information
        products_dict (dictionary): Dictionary containing the products information

    Returns:
        dictionary: Dictionary containing -> product_id, product_name, product_price, request_quantity
    """
    product_request_dict = copy.deepcopy(products_dict) #I tried with dictionary.copy() and dict() but original dictionary was still affected
    for product_id in product_request_dict:
        product_request_list = product_request_dict[product_id]
        product_request_list.append(0)
        if product_id in request_dict:
            request_qty = request_dict[product_id][0]
            product_request_list[2] = request_qty
    return product_request_dict

def accumulated_amounts(combine_product_request_dict,tax_percentage):
    """Return a dictionary containing subtotal and total

    Args:
        products_dict (Dictionary): Dictionary containing products and request information
        tax_percentage (float): Provide a tax rate as number

    Returns:
        Dictionary(String, Float): dictionary returning total; subtotal; no_items; sales_tax
    """
    accumulated_amounts_dict = {
        "no_items" : 0,
        "subtotal" : 0,
        "sales_tax" : 0,
        "total" : 0
    }
    index_price = 1
    index_quantity = 2
    for order_prod_id in combine_product_request_dict:
        accumulated_amounts_dict["subtotal"] += order_prod_id[index_price] * order_prod_id[index_quantity]
        accumulated_amounts_dict["no_items"] += order_prod_id[index_quantity]
    accumulated_amounts_dict["sales_tax"] = accumulated_amounts_dict["subtotal"] * tax_percentage / 100
    accumulated_amounts_dict["total"] = accumulated_amounts_dict["subtotal"] + accumulated_amounts_dict["sales_tax"]
    return accumulated_amounts_dict

def print_receipt(combine_product_request_dict,tax_percentage):
    accumulated_amounts_dict = accumulated_amounts(combine_product_request_dict,tax_percentage)
    index_name = 0
    index_price = 1
    index_quantity = 2
    print("Inkom Emporium\n")

    for order_prod_id in combine_product_request_dict:
        name = order_prod_id[index_name]
        price = order_prod_id[index_price]
        quantity = order_prod_id[index_quantity]
        print(f"{name}: {quantity} @ {price}")
    
    print(f"\nNumber of Items: {accumulated_amounts_dict['no_items']}")
    print(f"Subtotal: {accumulated_amounts_dict['subtotal']}")
    print(f"Sales Tax: {accumulated_amounts_dict['sales_tax']}")
    print(f"Total: {accumulated_amounts_dict['total']}")

    print("\nThank you for shopping at the Inkom Emporium.")
    print(f"{current_datet_formatted}")

def main():
    products_dict = read_dictionary("products.csv",0)
    request_dict = read_dictionary("request.csv",0)
    combined_dictionary = combine_product_request(request_dict,products_dict)
    # string_x = "a"
    print_receipt(combined_dictionary,6)
    


# Call main to start this program.
if __name__ == "__main__":
    main()