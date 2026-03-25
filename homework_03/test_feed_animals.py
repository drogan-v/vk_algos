from homework_03.solutions import feed_animals


def test_feed_animals_empty_inputs():
    assert feed_animals([], [1, 2, 3]) == 0
    assert feed_animals([1, 2, 3], []) == 0


def test_feed_animals_all_fed_unsorted():
    animals = [3, 2, 1]
    food = [1, 2, 3]
    assert feed_animals(animals, food) == 3


def test_feed_animals_partial_feed():
    animals = [2, 3, 4]
    food = [1, 2, 2]
    assert feed_animals(animals, food) == 1
