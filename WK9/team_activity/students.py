import os
import csv
from os import path

def buildPath(file_name):
    """Given a file you want to reach located at same folder as this .py file retrieve the absolute path to concatenate to file name

    Args:
        file_name (String): You'll specify the file name you want to interact with (myinfo.txt,myinfo.csv,etc)

    Returns:
        string: Absolute path concatenated to file name argument
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    final_path = ""

    contains_slash = True if dir_path.find("/") != -1 else False
    contains_double_slash = True if dir_path.find("//") != -1 else False
    contains_backslash = True if dir_path.find("\\") != -1 else False
    contains_double_backslash = True if dir_path.find("\\\\") != -1 else False

    dictionary_final_path = {
        contains_slash: dir_path + "/" + file_name,
        contains_double_slash: dir_path + "//" + file_name,
        contains_backslash: dir_path + "\\" + file_name,
        contains_double_backslash: dir_path + "\\\\" + file_name
    }

    return dictionary_final_path[True]

def buildPath_v2(file_name):
    """Given a file you want to reach located at same folder as this .py file retrieve the absolute path to concatenate to file name

    Args:
        file_name (String): You'll specify the file name you want to interact with (myinfo.txt,myinfo.csv,etc)

    Returns:
        string: Absolute path concatenated to file name argument
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    final_path = ""

    contains_slash = True if dir_path.find("/") != -1 else False
    contains_double_slash = True if dir_path.find("//") != -1 else False
    contains_backslash = True if dir_path.find("\\") != -1 else False
    contains_double_backslash = True if dir_path.find("\\\\") != -1 else False
    
    if contains_slash:
        final_path = dir_path + "/" + file_name
    elif contains_double_slash:
        final_path = dir_path + "//" + file_name
    elif contains_backslash:
        final_path = dir_path + "\\" + file_name
    elif contains_double_backslash:
        final_path = dir_path + "\\\\" + file_name
    
    return final_path

def buildPath_v3(file_name):
    file_name_path = path.join(path.dirname(__file__), "students.csv")
    return file_name_path

def read_dictionary(filename, key_column_index=None):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    file_name_path = buildPath_v3(filename)
    dict_students = {}
    index_id = 0
    index_name = 1
    with open(file_name_path, "rt") as csv_file:
        reader = csv.reader(csv_file)
        index_row = 0
        for row_list in reader:
            if index_row != 0:
                dict_students[row_list[index_id]] = row_list[index_name]
            index_row += 1
    return dict_students

def check_student(student_id, students_dict):
    message = ""
    if student_id in students_dict:
        message = students_dict[student_id]
    else:
        message = "No such student"
    return message

def main():
    students_dict = read_dictionary("students.csv")
    student1 = input("Please enter an I-Number (xxxxxxxxx): ")
    print(f"{check_student(student1,students_dict)}")
    student2 = input("Please enter an I-Number (xxxxxxxxx): ")
    print(f"{check_student(student2,students_dict)}")

# Call main to start this program.
if __name__ == "__main__":
    main()