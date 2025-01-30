from linkextraction import extract_markdown_images, extract_markdown_links
import unittest

class LinkExtractionTest(unittest.TestCase):
    def test_eq(self):
        # test for link/imagelink extraction
        # test cases
        imagetext1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        imagetext2 = "This is text with a ![rick roll](https://i.imgur.com/images/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/images/obiwan/fJRm4Vk.jpeg)"
        imagetext3 = "This is text with a ![https://i.imgur.com/images/aKaOqIh.gif](https://i.imgur.com/images/aKaOqIh.gif) and ![https://i.imgur.com/images/obiwan/fJRm4Vk.jpeg](https://i.imgur.com/images/obiwan/fJRm4Vk.jpeg)"
        linktext1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        linktext2 = "This is text with a link [to boot dev](https://www.boot.dev/home) and [to youtube](https://www.youtube.com/dev/@bootdotdev)"
        linktext3 = "This is text with a link [https://www.boot.dev](https://www.boot.dev/home) and [https://www.youtube.com/@bootdotdev](https://www.youtube.com/dev/@bootdotdev)"
        
        # basic extraction
        self.assertEqual(extract_markdown_images(imagetext1), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        self.assertEqual(extract_markdown_links(linktext1), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        # nested directory
        self.assertEqual(extract_markdown_images(imagetext2), [("rick roll", "https://i.imgur.com/images/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/images/obiwan/fJRm4Vk.jpeg")])
        self.assertEqual(extract_markdown_links(linktext2), [("to boot dev", "https://www.boot.dev/home"), ("to youtube", "https://www.youtube.com/dev/@bootdotdev")])
        # link also in alt text
        self.assertEqual(extract_markdown_images(imagetext3), [("https://i.imgur.com/images/aKaOqIh.gif", "https://i.imgur.com/images/aKaOqIh.gif"), ("https://i.imgur.com/images/obiwan/fJRm4Vk.jpeg", "https://i.imgur.com/images/obiwan/fJRm4Vk.jpeg")])
        self.assertEqual(extract_markdown_links(linktext3), [("https://www.boot.dev", "https://www.boot.dev/home"), ("https://www.youtube.com/@bootdotdev", "https://www.youtube.com/dev/@bootdotdev")])
        
        
if __name__ == "__main__":
    unittest.main()