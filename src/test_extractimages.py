import unittest

from extract_markdown_links_images import extract_markdown_images

class TestExtractImage(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)




if __name__ == "__main__":
    unittest.main()