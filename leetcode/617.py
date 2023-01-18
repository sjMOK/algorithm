class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(root1, root2):
    if root1 is None and root2 is None:
        return None

    if root1 is not None and root2 is None:
        root2 = TreeNode(0)
    elif root1 is None and root2 is not None:
        root1 = TreeNode(0)

    root1.left = merge_trees(root1.left, root2.left)
    root1.right = merge_trees(root1.right, root2.right)

    root1.val += root2.val
    return root1