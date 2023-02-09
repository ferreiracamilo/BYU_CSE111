import random

def get_determiner(quantity):
    """Return a randomly chosen determiner.

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of the single nouns, otherwise will return one of the plural nouns

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb based on quantity and tense.

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    # tense = tense.lower()
    if quantity > 1 and tense == "present":
        tense = "plural_present"

    #it is easier to maintain a dictionary instead of nested ifs
    verb_dictionary = {
                "past": ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
                "future": ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
                "present": ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
                "plural_present": ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
                }
    
    # Randomly choose and return a determiner.
    word = random.choice(verb_dictionary[tense])
    return word


def get_preposition():
    """Return a randomly chosen preposition

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    ret_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}"
    return ret_phrase


def get_adjective():
    words = ["small","big","talented","young","ancient","black","red","swedish"]
    word = random.choice(words)
    return word


def main():
    #Even though it was indicated in the prove assignment to follow certain data criteria for printing 6 sentences, I believe an iteration could be better
    print("single past")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1,'past')} {get_prepositional_phrase(1)}")

    print("\nsingle present")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1,'present')} {get_prepositional_phrase(1)}")

    print("\nsingle future")
    print(f"{get_determiner(1).capitalize()} {get_noun(1)} {get_verb(1,'future')} {get_prepositional_phrase(1)}")

    print("\nplural past")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2,'past')} {get_prepositional_phrase(2)}")

    print("\nplural present")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2,'present')} {get_prepositional_phrase(2)}")

    print("\nplural future")
    print(f"{get_determiner(2).capitalize()} {get_noun(2)} {get_verb(2,'future')} {get_prepositional_phrase(2)}")


# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()