import unittest
from split_nodes_delimiter import split_nodes_image
from textnode import TextNode, TextType
# You'll need to import your split_nodes_image function from wherever it lives
# from your_module_name import split_nodes_image 

class TestSplitNodesImage(unittest.TestCase):
    def test_split_single_image(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_multiple_images(self):
        node = TextNode(
            "Here's ![first image](https://example.com/1.png) and ![second image](https://example.com/2.png) in text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here's ", TextType.TEXT),
                TextNode("first image", TextType.IMAGE, "https://example.com/1.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://example.com/2.png"),
                TextNode(" in text.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_at_start_and_end(self):
        node = TextNode(
            "![Start](https://start.com/img.png) text with an image and ![end](https://end.com/img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Start", TextType.IMAGE, "https://start.com/img.png"),
                TextNode(" text with an image and ", TextType.TEXT),
                TextNode("end", TextType.IMAGE, "https://end.com/img.png"),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode("This text has no images.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This text has no images.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_node_not_text_type(self):
        node = TextNode("This is a code block", TextType.CODE)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a code block", TextType.CODE),
            ],
            new_nodes,
        )