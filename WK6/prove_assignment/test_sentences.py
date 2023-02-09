from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for i in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for i in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single determiners.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for i in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural determiners.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for i in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns


def test_get_verb():
    # 1. Test the single determiners.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for i in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(i, "past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in past_verbs

    # 2. Test the plural determiners.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for i in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(i, "future")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in future_verbs
    
    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for i in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(1, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in present_single_verbs
    
    present_multi_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for i in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2, "present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in present_multi_verbs


def test_get_preposition():
    words = ["about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]
    word = random.choice(words)
    assert word in words


def test_get_adjective():
    words = ["small","big","talented","young","ancient","black","red","swedish"]
    word = random.choice(words)
    assert word in words


def test_get_prepositional_phrase():
    single_prepositional_phrase = get_prepositional_phrase(1)
    single_prepositional_phrase_list_words = single_prepositional_phrase.split(" ")
    single_prepositional_phrase_list_length = len(single_prepositional_phrase_list_words)
    assert single_prepositional_phrase_list_length is 4

    plural_prepositional_phrase = get_prepositional_phrase(2)
    plural_prepositional_phrase_list_words = plural_prepositional_phrase.split(" ")
    plural_prepositional_phrase_list_length = len(plural_prepositional_phrase_list_words)
    assert plural_prepositional_phrase_list_length is 4


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])