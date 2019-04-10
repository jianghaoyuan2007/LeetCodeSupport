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


def string_to_tree_node(string):
    string = string.strip()
    string = string[1:-1]
    if not string:
        return None

    input_values = [s.strip() for s in string.split(',')]
    root = TreeNode(int(input_values[0]))
    node_queue = [root]
    front = 0
    index = 1
    while index < len(input_values):
        node = node_queue[front]
        front = front + 1

        item = input_values[index]
        index = index + 1
        if item != "null":
            left_number = int(item)
            node.left = TreeNode(left_number)
            node_queue.append(node.left)

        if index >= len(input_values):
            break

        item = input_values[index]
        index = index + 1
        if item != "null":
            right_number = int(item)
            node.right = TreeNode(right_number)
            node_queue.append(node.right)
    return root

