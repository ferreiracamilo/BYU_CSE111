from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make full name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("Olivier", "Toussaint") == "Toussaint; Olivier"
    assert make_full_name("George","Washington") == "Washington; George"
    assert make_full_name("Martha","Washington") == "Washington; Martha"


def test_extract_family_name():
    """Verify that the extract family name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    assert extract_family_name("Toussaint; Olivier") == "Toussaint"
    assert extract_family_name("Washington; George") == "Washington"
    assert extract_family_name("Washington; Martha") == "Washington"

def test_extract_given_name():
    """Verify that the make extract given name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_given_name("Toussaint; Marie") == "Marie"
    assert extract_given_name("Toussaint; Olivier") == "Olivier"
    assert extract_given_name("Washington; George") == "George"
    assert extract_given_name("Washington; Martha") == "Martha"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])