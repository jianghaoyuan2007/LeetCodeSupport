import unittest
from ..support import create_binary_tree


class BinaryTreeCreationTests(unittest.TestCase):

    def test_create_binary_tree(self):
        nodes = [3, 9, 20, None, None, 15, 7]
        root = create_binary_tree(nodes)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
