from homework_04.solutions import TreeNode, isSameTree


def test_is_same_tree_for_two_empty_trees():
    assert isSameTree(None, None) is True


def test_is_same_tree_for_identical_trees():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    assert isSameTree(p, q) is True


def test_is_same_tree_for_different_values():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(4))

    assert isSameTree(p, q) is False


def test_is_same_tree_for_different_structure():
    p = TreeNode(1, TreeNode(2), None)
    q = TreeNode(1, None, TreeNode(2))

    assert isSameTree(p, q) is False