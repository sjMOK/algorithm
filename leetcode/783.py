import sys

class Solution:
    min_diff = sys.maxsize

    def min_diff_in_bst(self, root):
        def get_min_diff(node):
            if node.left is not None:
                left_max = self.get_max_of_bst(node.left, node.left.val)
                self.min_diff = min(self.min_diff, abs(left_max - node.val))
                self.min_diff_in_bst(node.left)

            if node.right is not None:
                right_min = self.get_min_of_bst(node.right, node.right.val)
                self.min_diff = min(self.min_diff, abs(right_min - node.val))
                self.min_diff_in_bst(node.right)

        get_min_diff(root)
        return self.min_diff

    def get_max_of_bst(self, node, max_val):
        if node is None:
            return max_val

        max_val = self.get_max_of_bst(node.right, max_val)
        max_val = max(max_val, node.val)

        return max_val

    def get_min_of_bst(self, node, min_val):
        if node is None:
            return min_val

        min_val = self.get_min_of_bst(node.left, min_val)
        min_val = min(min_val, node.val)

        return min_val

