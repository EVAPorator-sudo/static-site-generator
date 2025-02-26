import unittest
from extract_title import extract_title

class TitleExtractionTest(unittest.TestCase):
    def test_eq(self):
        if __name__ == "__main__":
            test = "# valid header" # test for basic input
            test2 = "# #another valid header" # test for possible second '#'
            test3 = "# valid header with whitespace " # test for stripping whitespace

            self.assertEqual(extract_title(test), "valid header")
            self.assertEqual(extract_title(test2), "#another valid header")
            self.assertEqual(extract_title(test3), "valid header with whitespace")

if __name__ == "__main__":
    unittest.main()