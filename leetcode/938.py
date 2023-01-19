def range_sum_bst(root, low, high):
    def get_sum(node):
        if node is None:
            return 0

        if node.val < low:
            return range_sum_bst(node.right)
        elif node.val > high:
            return range_sum_bst(node.left)

        return node.val + range_sum_bst(node.left) + range_sum_bst(node.right)

    return get_sum(root)