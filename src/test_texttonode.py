from texttonode import text_to_textnode
import unittest
from textnode import TextNode, TextType

class TextToTextNodeTest(unittest.TestCase):
    def test_eq(self):
        # basic types
        text = "This is a [link](https://example.com)"
        text2 = "This is **bold text**"
        text3 = "This is *italics*"
        text4 ="This is an ![image](https://example.com/image.png)"
        # multiple in one
        text5 = "This is **bold text** and a [link](https://example.com)"
        text6 = "this is *italics* and some **bold text**"
        #plain text
        text7 = "this is some plain text"
        

        self.assertEqual(text_to_textnode(text), [TextNode("This is a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://example.com")])
        self.assertEqual(text_to_textnode(text2), [TextNode("This is ", TextType.TEXT), TextNode("bold text", TextType.BOLD)])
        self.assertEqual(text_to_textnode(text3), [TextNode("This is ", TextType.TEXT), TextNode("italics", TextType.ITALIC)])
        self.assertEqual(text_to_textnode(text4), [TextNode("This is an ", TextType.TEXT), TextNode("image", TextType.IMAGE, "https://example.com/image.png")])
        self.assertEqual(text_to_textnode(text5), [TextNode("This is ", TextType.TEXT), TextNode("bold text", TextType.BOLD), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://example.com")])
        self.assertEqual(text_to_textnode(text6), [TextNode("this is ", TextType.TEXT), TextNode("italics", TextType.ITALIC), TextNode(" and some ", TextType.TEXT), TextNode("bold text", TextType.BOLD)])
        self.assertEqual(text_to_textnode(text7), [TextNode("this is some plain text", TextType.TEXT)])

if __name__ == "__main__":
    unittest.main()
