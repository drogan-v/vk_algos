from homework_04.solutions import build_tree


def test_build_tree_returns_none_for_out_of_range_index():
    assert build_tree([1, 2, 3], 10) is None


def test_build_tree_creates_expected_structure():
    root = build_tree([1, 2, 3, 4, 5, 6, 7], 0)

    assert root is not None
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left.val == 4
    assert root.left.right.val == 5
    assert root.right.left.val == 6
    assert root.right.right.val == 7