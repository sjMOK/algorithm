class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = True

    def is_balanced(self, root):
        def get_height(root):
            if root is None:
                return -1

            l_height = get_height(root.left)
            r_height = get_height(root.right)

            if abs(l_height - r_height) > 1:
                self.result = False

            return max(l_height, r_height) + 1

        get_height(root)
        return self.result
