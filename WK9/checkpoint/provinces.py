def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    #filename_update = 'C:\\Users\\CamiloF\\Documents\\GitHub\\CSE111\\WK9\\prepare\\'
    #text_list = read_list(filename_update+"plants.txt")
    text_list = read_list("WK9\\checkpoint\\provinces.txt")
    text_list = list(map(lambda x: x.replace('AB', 'Alberta'), text_list)) #replace AB for Alberta
    print(f"{text_list}\n")
    text_list.pop(0)
    text_list.pop(len(text_list)-1)
    count_states_list = count_states(text_list)
    alberta_occurences = count_states_list["Alberta"]
    print(f"\nAlberta has been found {alberta_occurences} times")
    # Print the entire list.


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


def count_states(state_list):
    country_dictionary = {}
    for state in state_list:
        if state in country_dictionary:
            country_dictionary[state] += 1
        else:
            country_dictionary[state] = 1
    return country_dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()