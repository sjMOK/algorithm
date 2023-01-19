def bst_to_gst(root):
    def r_convert(node, sum=0):
        if node is None:
            return sum

        sum = r_convert(node.right, sum)
        sum += node.val
        node.val = sum
        sum = r_convert(node.left, sum)

        return sum

    r_convert(root)

    return root
