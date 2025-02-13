import unittest
from blocktotype import block_to_block_type

class block_to_type_test(unittest.TestCase):
    def test_eq(self):
        block = "this is some text"
        block2 = "# this is a header"
        block3 = "###### this is a header with more hashes"
        block4 = "####### this is an invalid header"
        block5 = "```this is some code```"
        block6 = "``` this is invalid code"
        block7 = "* this is an\n* unordered list"
        block8 = "* this is an\n - unordered list\n* with different characters"
        block9 = "* this is an invalid\n list"
        block10 = "1. this is an ordered\n2. list"
        block11 = "0. this is an invalid\n1. list"
        self.assertEqual(block_to_block_type(block), "paragraph")
        self.assertEqual(block_to_block_type(block2), "heading")
        self.assertEqual(block_to_block_type(block3), "heading")
        self.assertEqual(block_to_block_type(block4), "paragraph")
        self.assertEqual(block_to_block_type(block5), "code")
        self.assertEqual(block_to_block_type(block6), "paragraph")
        self.assertEqual(block_to_block_type(block7), "unordered_list")
        self.assertEqual(block_to_block_type(block8), "unordered_list")
        self.assertEqual(block_to_block_type(block9), "paragraph")
        self.assertEqual(block_to_block_type(block10), "ordered_list")
        self.assertEqual(block_to_block_type(block11), "paragraph")

if __name__ == "__main__":
    unittest.main()