from homework_06.solutions import longest_palindrome


def test_longest_palindrome_empty_string():
    assert longest_palindrome("") == ""


def test_longest_palindrome_single_character():
    assert longest_palindrome("a") == "a"


def test_longest_palindrome_odd_length_center():
    assert longest_palindrome("babad") in {"bab", "aba"}


def test_longest_palindrome_even_length_center():
    assert longest_palindrome("cbbd") == "bb"


def test_longest_palindrome_whole_string_is_palindrome():
    assert longest_palindrome("racecar") == "racecar"
