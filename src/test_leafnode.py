import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("h1", "this is a test node", {"href": "https://www.google.com"})
        node2 = LeafNode("h1", "this is a test node", {"href": "https://www.google.com"})
        node3 = LeafNode("h1", "this is another test node", {"href": "https://www.google.com"})
        node4 = LeafNode("h1", "this is a new test node")
        self.assertEqual(node.__repr__(), node2.__repr__())
        self.assertEqual(node.__repr__(), "HTMLNode(h1, this is a test node, None, {'href': 'https://www.google.com'})")
        self.assertNotEqual(node.to_html(), node3.to_html())
        self.assertNotEqual(node.__repr__(), node3.__repr__())
        self.assertNotEqual(node4.__repr__(), node3.__repr__())

if __name__ == "__main__":
    unittest.main()