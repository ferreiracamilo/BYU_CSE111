import os
import csv
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
            qty_columns = len(row_list)
            data_value = []
            for i in range(qty_columns):
                if i != key_column_index:
                    data_value.append(row_list[i])
            outcome_dictionary[row_list[key_column_index]] = data_value
    return outcome_dictionary

print(read_dictionary("products.csv",1))