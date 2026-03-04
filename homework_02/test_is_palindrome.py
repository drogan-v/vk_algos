from homework_02.solutions import is_palindrome


def test_empty_string():
    """Пустая строка считается палиндромом"""
    assert is_palindrome("") is True

def test_single_character():
    """Один символ — палиндром"""
    assert is_palindrome("a") is True
    assert is_palindrome("z") is True

def test_two_characters_same():
    """Два одинаковых символа — палиндром"""
    assert is_palindrome("aa") is True
    assert is_palindrome("zz") is True

def test_two_characters_different():
    """Два разных символа — не палиндром"""
    assert is_palindrome("ab") is False
    assert is_palindrome("xy") is False

def test_odd_length_palindrome():
    """Палиндром нечетной длины"""
    assert is_palindrome("aba") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("madam") is True

def test_even_length_palindrome():
    """Палиндром четной длины"""
    assert is_palindrome("abba") is True
    assert is_palindrome("noon") is True
    assert is_palindrome("deed") is True

def test_not_palindrome():
    """Не палиндром"""
    assert is_palindrome("abc") is False
    assert is_palindrome("hello") is False
    assert is_palindrome("world") is False

def test_case_sensitive():
    """Проверка чувствительности к регистру"""
    assert is_palindrome("Aba") is False
    assert is_palindrome("aba") is True
    assert is_palindrome("ABBA") is True

def test_with_spaces():
    """Строка с пробелами (пробелы учитываются)"""
    assert is_palindrome("a b a") is True
    assert is_palindrome("a b") is False

def test_with_special_characters():
    """Строка со специальными символами"""
    assert is_palindrome("a!a") is True
    assert is_palindrome("a!b") is False
    assert is_palindrome("!!!") is True

def test_numbers():
    """Числовые строки"""
    assert is_palindrome("121") is True
    assert is_palindrome("123") is False
    assert is_palindrome("12321") is True

def test_mixed_alphanumeric():
    """Смешанные буквы и цифры"""
    assert is_palindrome("a1a") is True
    assert is_palindrome("a1b") is False

def test_long_palindrome():
    """Длинный палиндром"""
    long_palindrome = "a" * 1000
    assert is_palindrome(long_palindrome) is True

def test_long_not_palindrome():
    """Длинная не палиндром строка"""
    long_string = "a" * 500 + "b" + "a" * 499
    assert is_palindrome(long_string) is False

def test_unicode_characters():
    """Юникод символы (кириллица)"""
    assert is_palindrome("шалаш") is True
    assert is_palindrome("топот") is True
    assert is_palindrome("привет") is False

def test_single_word_palindromes():
    """Известные слова-палиндромы"""
    assert is_palindrome("level") is True
    assert is_palindrome("radar") is True
    assert is_palindrome("rotor") is True
    assert is_palindrome("civic") is True
    assert is_palindrome("kayak") is True

