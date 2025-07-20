import unittest
from split_nodes_delimiter import split_nodes_link  
from textnode import TextNode, TextType
# You'll need to import your split_nodes_link function from wherever it lives
# from your_module_name import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_split_single_link(self):
        node = TextNode("This is text with a [link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_multiple_links(self):
        node = TextNode(
            "Visit [Boot.dev](https://www.boot.dev) and [Google](https://www.google.com) for more.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" for more.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_at_start_and_end(self):
        node = TextNode(
            "[Start](https://start.com) of text with a link and [end](https://end.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start", TextType.LINK, "https://start.com"),
                TextNode(" of text with a link and ", TextType.TEXT),
                TextNode("end", TextType.LINK, "https://end.com"),
            ],
            new_nodes,
        )

    def test_split_no_links(self):
        node = TextNode("This text has no links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text has no links.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_node_not_text_type(self):
        node = TextNode("This is an image node", TextType.IMAGE, "image_url.png")
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is an image node", TextType.IMAGE, "image_url.png"),
            ],
            new_nodes,
        )
