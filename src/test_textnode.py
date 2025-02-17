import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from htmlnode import HTMLNode
"""
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # test Class attribute
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

    def test_text_node_to_html_node(self):
        # Test text_to_html
        # Test normal text
        text_node = TextNode("Hello World", TextType.TEXT)
        leaf_node = text_node.text_node_to_html_node()
        self.assertEqual(leaf_node, LeafNode(None, "Hello World"))
        
        # Test bold text
        text_node = TextNode("Bold Text", TextType.BOLD)
        leaf_node = text_node.text_node_to_html_node()
        self.assertEqual(leaf_node, LeafNode("b", "Bold Text"))
        
        # Test italic text
        text_node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node, HTMLNode("i", "Italic Text"))
        
        # Test code text
        text_node = TextNode("Code Text", TextType.CODE)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node, HTMLNode("code", "Code Text"))
        
        # Test link
        text_node = TextNode("Link Text", TextType.LINK, url="https://example.com")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node, HTMLNode("a", "Link Text", None, {"href": "https://example.com"}))
        
        # Test image
        text_node = TextNode("Image Alt", TextType.IMAGE, url="https://example.com/image.png")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node, HTMLNode("img", "", None, {"src": "https://example.com/image.png", "alt": "Image Alt"}))
        
        # Test invalid type
        with self.assertRaises(Exception):
            text_node = TextNode("Invalid Text", "InvalidType")
            text_node.text_node_to_html_node()
        


if __name__ == "__main__":
    unittest.main() 
"""