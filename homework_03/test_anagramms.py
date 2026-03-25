from homework_03.solutions import anagramms


def _normalize(groups):
    return sorted(sorted(group) for group in groups)


def test_anagramms_grouping():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = anagramms(words)
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert _normalize(result) == _normalize(expected)


def test_anagramms_empty_input():
    assert anagramms([]) == []


def test_anagramms_single_word():
    assert anagramms(["solo"]) == [["solo"]]
