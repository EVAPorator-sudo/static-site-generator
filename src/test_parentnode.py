import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_parent_with_nested_parents(self):
        # Create LeafNodes and ParentNodes
        leaf1 = LeafNode("h1", "Leaf 1 content", {"href": "https://www.google.com"})
        leaf2 = LeafNode("h1", "Leaf 2 content", {"href": "https://www.bing.com"})
        
        # Create a ParentNode with LeafNodes and nested ParentNodes
        nested_parent = ParentNode(
            "h1",
            [
                leaf1,  # This is a LeafNode
                ParentNode(
                    "h1",  # This is a nested ParentNode with the same tag
                    [
                        leaf2  # A LeafNode inside the nested ParentNode
                    ]
                ),
                LeafNode("h1", "Leaf 3 content")  # Another LeafNode
            ]
        )

        # Expected output with nested <h1> tags and proper handling
        expected_html = (
            "<h1>"
            "<h1 href='https://www.google.com'>Leaf 1 content</h1>"
            "<h1>"
            "<h1 href='https://www.bing.com'>Leaf 2 content</h1>"
            "</h1>"
            "<h1>Leaf 3 content</h1>"
            "</h1>"
        )

        # Assert that the generated HTML matches the expected output
        self.assertEqual(nested_parent.to_html(), expected_html)

    def test_parent_with_different_children_types(self):
        # Test a ParentNode with a mix of ParentNode and LeafNode children

        leaf1 = LeafNode("p", "This is a paragraph.")
        nested_parent = ParentNode(
            "div",
            [
                leaf1,  # A LeafNode child
                ParentNode(
                    "section",  # A nested ParentNode
                    [
                        LeafNode("span", "Span content in section")
                    ]
                )
            ]
        )

        # Expected HTML structure with mixed children types (ParentNode and LeafNode)
        expected_html = (
            "<div>"
            "<p>This is a paragraph.</p>"
            "<section>"
            "<span>Span content in section</span>"
            "</section>"
            "</div>"
        )

        # Assert that the generated HTML matches the expected output
        self.assertEqual(nested_parent.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()