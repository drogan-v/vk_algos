from homework_03.solutions import extra_letter


def test_extra_letter_extra_at_end():
    assert extra_letter("abcd", "abcde") == "e"


def test_extra_letter_extra_at_beginning():
    assert extra_letter("abcd", "zabcd") == "z"


def test_extra_letter_with_repeated_chars():
    assert extra_letter("aabbcc", "ababbcc") == "b"


def test_extra_letter_no_extra():
    assert extra_letter("abc", "abc") == ""
