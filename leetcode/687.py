class Solution:
    longest_length = 0

    def longest_univalue_path(self, root):
        def post_order(node):
            if node is None:
                return 0

            left  = post_order(node.left)
            right = post_order(node.right)

            if node.left is not None and node.val == node.left.val:
                left += 1
            else:
                left = 0
                
            if node.right is not None and node.val == node.right.val:
                right += 1
            else:
                right = 0

            self.longest_length = max(self.longest_length, left + right)
            length = max(left, right)

            return length

        post_order(root)
        return self.longest_length
