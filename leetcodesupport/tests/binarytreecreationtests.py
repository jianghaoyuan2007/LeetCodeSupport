import unittest
from ..support import create_binary_tree
from ..support import string_to_tree_node


class BinaryTreeCreationTests(unittest.TestCase):

    def test_create_binary_tree(self):
        nodes = [3, 9, 20, None, None, 15, 7]
        root = create_binary_tree(nodes)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)

    def test_string_to_tree_node(self):
        string = "[3,9,20,null,null,15,7]"
        root = string_to_tree_node(string)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
