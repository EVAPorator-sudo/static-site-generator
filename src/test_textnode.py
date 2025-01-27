import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "https://www.this-is-a-dummy-url.com")
        node4 = TextNode("This is another text node", TextType.ITALIC, "https://www.this-is-a-new-dummy-url.com")
        self.assertEqual(node, node2)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, bold text, None)")
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node.__repr__(), node3.__repr__())
        self.assertNotEqual(node4.__repr__(), node3.__repr__())
        self.assertEqual(node4.__repr__(), "TextNode(This is another text node, italic text, https://www.this-is-a-new-dummy-url.com)")
        


if __name__ == "__main__":
    unittest.main()