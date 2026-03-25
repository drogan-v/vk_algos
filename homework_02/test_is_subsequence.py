from homework_02.solutions import is_subsequence


def test_empty_strings():
    """Пустая строка является подпоследовательностью любой строки"""
    assert is_subsequence("", "") is True
    assert is_subsequence("", "abc") is True


def test_single_character_match():
    """Одиночный символ совпадает"""
    assert is_subsequence("a", "a") is True


def test_single_character_no_match():
    """Одиночный символ не совпадает"""
    assert is_subsequence("a", "b") is False


def test_exact_match():
    """Строки полностью совпадают"""
    assert is_subsequence("abc", "abc") is True


def test_subsequence_true():
    """Строка a является подпоследовательностью строки b"""
    assert is_subsequence("abc", "ahbgdc") is True


def test_subsequence_false():
    """Строка a НЕ является подпоследовательностью строки b"""
    assert is_subsequence("axc", "ahbgdc") is False


def test_characters_in_wrong_order():
    """Символы присутствуют, но в неправильном порядке"""
    assert is_subsequence("cba", "abc") is False


def test_all_chars_present_wrong_order():
    """Все символы есть, но порядок нарушен"""
    assert is_subsequence("bac", "abc") is False


def test_longer_a_than_b():
    """Строка a длиннее строки b"""
    assert is_subsequence("abcd", "abc") is False


def test_consecutive_characters():
    """Проверка последовательных символов"""
    assert is_subsequence("ace", "abcde") is True
    assert is_subsequence("aec", "abcde") is False


def test_repeated_characters():
    """Повторяющиеся символы в строке"""
    assert is_subsequence("aa", "aaa") is True
    assert is_subsequence("aaa", "aa") is False
    assert is_subsequence("aab", "aaab") is True


def test_first_character_match():
    """Совпадение начинается с первого символа"""
    assert is_subsequence("abc", "abcdef") is True


def test_last_character_match():
    """Совпадение заканчивается последним символом"""
    assert is_subsequence("def", "abcdef") is True


def test_middle_characters_match():
    """Совпадают только средние символы"""
    assert is_subsequence("bcd", "abcdef") is True


def test_alternating_characters():
    """Символы чередуются с другими"""
    assert is_subsequence("abc", "aXbYcZ") is True
    assert is_subsequence("abc", "aXcYbZ") is False


def test_case_sensitive():
    """Проверка чувствительности к регистру"""
    assert is_subsequence("abc", "ABC") is False
    assert is_subsequence("ABC", "ABC") is True
    assert is_subsequence("AbC", "AaBbCc") is True


def test_special_characters():
    """Специальные символы и пробелы"""
    assert is_subsequence("a b", "a x b") is True
    assert is_subsequence("@#$", "@x#y$") is True
    assert is_subsequence("@#$", "@$#") is False


def test_numbers_in_string():
    """Цифры в строке"""
    assert is_subsequence("123", "1a2b3") is True
    assert is_subsequence("321", "1a2b3") is False


def test_large_strings():
    """Тест на больших строках"""
    a = "abc" * 100  # 300 символов
    b = "aXbYcZ" * 100  # 600 символов
    assert is_subsequence(a, b) is True


def test_almost_subsequence():
    """Почти подпоследовательность (не хватает одного символа)"""
    assert is_subsequence("abcd", "abc") is False
    assert is_subsequence("abc", "ab") is False


def test_single_char_in_long_string():
    """Одиночный символ в длинной строке"""
    assert is_subsequence("z", "abcdefghijklmnopqrstuvwxyz") is True
    assert is_subsequence("z", "abcdefghijklmnopqrstuvwxy") is False


def test_unicode_characters():
    """Юникод символы"""
    assert is_subsequence("абв", "ааббвв") is True
    assert is_subsequence("абв", "авб") is False


def test_empty_a_non_empty_b():
    """Пустая строка a и непустая строка b"""
    assert is_subsequence("", "anything") is True


def test_non_empty_a_empty_b():
    """Непустая строка a и пустая строка b"""
    assert is_subsequence("a", "") is False


def test_many_insertions():
    """Много вставленных символов между символами a"""
    a = "abc"
    b = "aXXXXXXbYYYYYYcZZZZZZ"
    assert is_subsequence(a, b) is True


def test_no_common_characters():
    """Нет общих символов между строками"""
    assert is_subsequence("abc", "xyz") is False


def test_first_char_missing():
    """Первый символ строки a отсутствует в b"""
    assert is_subsequence("abc", "xbc") is False


def test_last_char_missing():
    """Последний символ строки a отсутствует в b"""
    assert is_subsequence("abc", "abx") is False


def test_middle_char_missing():
    """Средний символ строки a отсутствует в b"""
    assert is_subsequence("abc", "axc") is False