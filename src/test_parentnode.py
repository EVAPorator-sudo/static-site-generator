import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        # tests parentnode constructiton and HTML conversions including nested parents 
        leaf1 = LeafNode("h1", "Leaf 1 content", {"href": "https://www.google.com"})
        leaf2 = LeafNode("h1", "Leaf 2 content", {"href": "https://www.bing.com"})
        nested_parent = ParentNode("h1", [leaf1, ParentNode("h1", [leaf2]), LeafNode("h1", "Leaf 3 content")])
        expected_html = "<h1><h1 href='https://www.google.com'>Leaf 1 content</h1><h1><h1 href='https://www.bing.com'>Leaf 2 content</h1></h1><h1>Leaf 3 content</h1></h1>"
        self.assertEqual(nested_parent.to_html(), expected_html)

        leaf3 = LeafNode("p", "This is a paragraph.")
        mixed_parent = ParentNode("div", [leaf3, ParentNode("section", [LeafNode("span", "Span content in section")])])
        expected_mixed_html = "<div><p>This is a paragraph.</p><section><span>Span content in section</span></section></div>"
        self.assertEqual(mixed_parent.to_html(), expected_mixed_html)

if __name__ == "__main__":
    unittest.main()
