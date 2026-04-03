from homework_04.solutions import TreeNode, is_symmetric


def test_is_symmetric_for_empty_tree():
    assert is_symmetric(None) is True


def test_is_symmetric_for_symmetric_tree():
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    assert is_symmetric(root) is True


def test_is_symmetric_for_non_symmetric_tree():
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(3))
    root.right = TreeNode(2, None, TreeNode(3))

    assert is_symmetric(root) is False