import unittest
from markdowntoblock import markdown_to_blocks

class MarkdownToBlockTest(unittest.TestCase):
    def test_eq(self):
        text = "this is some text" # single block
        text2 = "this is some text \n\n# and a header " # 2 blocks and leading + trailing 
        text3 = "this is some text \n\n# and a header \n\n *and a list\n *and a list " # this includes a list seperated by a single newline
        text4 = "" # this is an empty string
        self.assertEqual(markdown_to_blocks(text), ["this is some text"])
        self.assertEqual(markdown_to_blocks(text2), ["this is some text", "# and a header"])
        self.assertEqual(markdown_to_blocks(text3), ["this is some text", "# and a header", "*and a list\n*and a list"])
        self.assertEqual(markdown_to_blocks(text4), [''])

if __name__ == "__main__":
    unittest.main()