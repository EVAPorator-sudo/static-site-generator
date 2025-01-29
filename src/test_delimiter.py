import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestDelimiter(unittest.TestCase):
    def test_delimiter(self):
        # Setup test nodes
        node1 = TextNode("hello this is a `test` node", TextType.TEXT)
        node2 = TextNode("This *is* a test", TextType.TEXT)  # Simplified this case
        node3 = TextNode("this is just plain text", TextType.TEXT)
        node4 = TextNode("this should not be split", TextType.CODE)
        node5 = TextNode("**this* should not work", TextType.TEXT)
        node6 = TextNode("*this should not work either`", TextType.TEXT)

        # Test cases
        self.assertEqual(split_nodes_delimiter([node1], "`", TextType.CODE), [TextNode("hello this is a ", TextType.TEXT), TextNode("test", TextType.CODE), TextNode(" node", TextType.TEXT)])
        self.assertEqual(split_nodes_delimiter([node2], "*", TextType.ITALIC), [TextNode("This ", TextType.TEXT), TextNode("is", TextType.ITALIC), TextNode(" a test", TextType.TEXT)])
        self.assertEqual(split_nodes_delimiter([node3], "`", TextType.CODE), [node3])
        self.assertEqual(split_nodes_delimiter([node4], "`", TextType.CODE), [node4])
        with self.assertRaises(Exception): split_nodes_delimiter([node5], "**", TextType.BOLD)
        with self.assertRaises(Exception): split_nodes_delimiter([node6], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()




    
