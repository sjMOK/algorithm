class Solution:
    def __init__(self):
        self.diameter = 0

    def diameter_of_binary_tree(self, root):
        def post_order(node):
            if node is None:
                return -1

            left_child_height = post_order(node.left)
            right_child_height=  post_order(node.right)

            self.diameter = max(self.diameter, left_child_height + right_child_height + 2)
            height = max(left_child_height, right_child_height) + 1

            return height
        
        post_order(root)
        return self.diameter
