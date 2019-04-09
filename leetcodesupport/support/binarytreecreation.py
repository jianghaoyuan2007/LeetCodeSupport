# coding: utf-8
from ..datastructure import TreeNode


# 利用完全二叉树的性质，结点 i 的左右子结点分别为 2i 和 2i + 1。

def create_subtree_nodes(node, index, nodes):
    left_subtree_index = index * 2
    right_subtree_index = index * 2 + 1
    if left_subtree_index < len(nodes):
        value = nodes[left_subtree_index]
        if value is not None:
            node.left = TreeNode(value)
            create_subtree_nodes(node.left, left_subtree_index, nodes)
    if right_subtree_index < len(nodes):
        value = nodes[right_subtree_index]
        if value is not None:
            node.right = TreeNode(value)
            create_subtree_nodes(node.right, right_subtree_index, nodes)


def create_binary_tree(nodes):
    if len(nodes) == 0:
        return None
    else:
        nodes = [None] + nodes
        root = TreeNode(nodes[1])
        create_subtree_nodes(root, 1, nodes)
        return root
