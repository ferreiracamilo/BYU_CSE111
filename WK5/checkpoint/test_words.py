"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    # pre = 3
    assert isinstance(pre, str), "prefix function must return a string"
    # assert not(isinstance(pre, int)), "prefix function must not return a number"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"
    assert prefix("upstream", "upgrade") == "up"
    assert prefix("juanito", "juancho") == "juan"
    assert prefix("Circus", "circos") == "circ", "prefix obtained does not match with value expected"

def test_suffix():
    """Verify that the suffix function works correctly.
    Parameters: none
    Return: nothing
    """
    assert suffix("", "") == ""
    assert suffix("", "correct") == ""
    assert suffix("clear", "") == ""
    assert suffix("angelic", "awesome") == ""
    assert suffix("found", "profound") == "found"
    assert suffix("ditch", "itch") == "itch"
    assert suffix("happy", "funny") == "y"
    assert suffix("tired", "fatigued") == "ed"
    assert suffix("swimming", "FLYING") == "ing"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
