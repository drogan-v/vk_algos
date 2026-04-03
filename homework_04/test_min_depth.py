from homework_04.solutions import TreeNode, minDepth


def test_min_depth_for_empty_tree():
    assert minDepth(None) == 0


def test_min_depth_for_single_node_tree():
    root = TreeNode(1)
    assert minDepth(root) == 1


def test_min_depth_for_tree_with_shallow_leaf():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)

    assert minDepth(root) == 2