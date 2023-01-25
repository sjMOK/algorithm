import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    preorder = collections.deque(preorder)

    def r_build_tree(inorder):
        if inorder:
            index = inorder.index(preorder.popleft())

            node = TreeNode(inorder[index])
            node.left = r_build_tree(inorder[:index])
            node.right = r_build_tree(inorder[index + 1:])

            return node

    return r_build_tree(inorder)
