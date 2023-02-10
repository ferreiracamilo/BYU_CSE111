import random


def append_random_numbers(numbers_list,quantity=1):
    """Appends a quantity of numbers to a list generated randomly

    Args:
        numbers_list (list of numbers): _description_
        quantity (int, optional): _description_. Defaults to 1.
    """
    for i in range(quantity):
        newNumber = round(random.uniform(1,100),1)
        numbers_list.append(newNumber)


def append_random_words(words_list,quantity=1):
    """Appends a quantity of words to a list randomly

    Args:
        words_list (_type_): _description_
        quantity (int, optional): _description_. Defaults to 1.
    """
    words = ["dog","cat","house","building","city","country","apartment","flat","shopping mall"
            ,"disco","cinema","tv show","soap opera","elephant","vacations","sports","gaming"
            ,"tv","cooler","computer","video console","furniture","kitchen","bedroom"]
    for i in range(quantity):
        words_list.append(random.choice(words))


def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers,3)
    print(numbers)
    print()

    words = []
    print(words)
    append_random_words(words)
    print(words)
    append_random_words(words,3)
    print(words)


# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()