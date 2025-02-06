from linksplitter import split_nodes_link, split_nodes_image
from textnode import TextType, TextNode
import unittest

class LinkSplitterTest(unittest.TestCase):
    def test_eq(self):
        # image link node
        node = TextNode("here is a link ![this is an url](https://google.com/image.png) and some more text", TextType.TEXT)
        # link node
        node2 = TextNode("here is a link [this is an url](google.com) and some text", TextType.TEXT)
        # plain text node
        node3 = TextNode("this should not return any links", TextType.TEXT)
        # non text node
        node4 = TextNode("this is an invalid text type", TextType.BOLD)
        # both link and image link node
        node5 = TextNode("this should just return the image ![this is an image link](https://image.com/images/image.png) [this should not be returned](https://google.com)]", TextType.TEXT)

        # simple tests
        self.assertEqual(split_nodes_image([node]), [TextNode("here is a link ", TextType.TEXT), TextNode("this is an url", TextType.IMAGE, "https://google.com/image.png"), TextNode(" and some more text", TextType.TEXT)])
        self.assertEqual(split_nodes_link([node]), [node])
        self.assertEqual(split_nodes_link([node2]), [TextNode("here is a link ", TextType.TEXT), TextNode("this is an url", TextType.LINK, "google.com"), TextNode(" and some text", TextType.TEXT)])
        self.assertEqual(split_nodes_image([node2]), [node2])
        self.assertEqual(split_nodes_image([node3]), [node3])
        self.assertEqual(split_nodes_link([node3]), [node3])
        self.assertEqual(split_nodes_image([node4]), [node4])
        self.assertEqual(split_nodes_link([node4]), [node4])
        self.assertEqual(split_nodes_image([node5]), [TextNode("this should just return the image ", TextType.TEXT), TextNode("this is an image link", TextType.IMAGE, "https://image.com/images/image.png"), TextNode(" [this should not be returned](https://google.com)]", TextType.TEXT)])
        # multiple node test
        self.assertEqual(split_nodes_link([node3, node4]), [node3, node4])
        # image and link test
        self.assertEqual(split_nodes_image(node, node2), [TextNode("here is a link ", TextType.TEXT), TextNode("this is an url", TextType.IMAGE, "https://google.com/image.png"), TextNode(" and some more text", TextType.TEXT), node2])
        self.assertEqual(split_nodes_link(node, node2), [node, TextNode("here is a link ", TextType.TEXT), TextNode("this is an url", TextType.LINK, "google.com"), TextNode(" and some text", TextType.TEXT)])
        # nested functions test
        self.assertEqual(split_nodes_image(split_nodes_link(node, node2)), [TextNode("here is a link ", TextType.TEXT), TextNode("this is an url", TextType.IMAGE, "https://google.com/image.png"), TextNode(" and some more text", TextType.TEXT), TextNode("here is a link ", TextType.TEXT), TextNode("this is an url", TextType.LINK, "google.com"), TextNode(" and some text", TextType.TEXT)])
        self.assertEqual(split_nodes_link(split_nodes_image(node, node2)), split_nodes_image(split_nodes_link(node, node2)))

if __name__ == "__main__":
    unittest.main()