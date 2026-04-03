from homework_04.solutions import min_max_product_bst


def test_min_max_product_bst_for_empty_input():
    assert min_max_product_bst([]) is None


def test_min_max_product_bst_for_balanced_bst():
    data = [4, 2, 6, 1, 3, 5, 7]
    assert min_max_product_bst(data) == 7