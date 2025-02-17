import unittest
from htmlnode import HTMLNode
"""
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        # tests various htmlnode attributes
        node = HTMLNode("h1", "this is a test node", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "this is a test node", None, {"href": "https://www.google.com"})
        node3 = HTMLNode("h1", "this is another test node",["node1", "node2"] , {"href": "https://www.google.com"})
        node4 = HTMLNode("a", "this is a test node", None, {"targt": "https://www.bing.com"})
        self.assertEqual(node, node2)
        self.assertEqual(node.__repr__(), node2.__repr__())
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node.__repr__(), node3.__repr__())
        self.assertNotEqual(node4.__repr__(), node3.__repr__())
        self.assertNotEqual(node4.__repr__(), "")

if __name__ == "__main__":
    unittest.main()
"""