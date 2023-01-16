class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    def pre_order(root, cnt=0, depth=0):
        if root is None:
            return max(depth, cnt)

        cnt += 1
        depth = pre_order(root.left, cnt, depth)
        depth = pre_order(root.right, cnt, depth)

        return depth

    return pre_order(root)
