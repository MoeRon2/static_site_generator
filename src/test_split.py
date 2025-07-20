import unittest

from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplit(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print("🔥🔥🔥")
        print(new_nodes)
        new_nodes_expected = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
        ]
        print(new_nodes_expected)
        print("🔥🔥🔥")
        self.assertEqual(new_nodes, new_nodes_expected)
    
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes_expected = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, new_nodes_expected)
        print("🔥🔥🔥")
        print(new_nodes)
        print(new_nodes_expected)
        print("🔥🔥🔥")
    
    def test_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        new_nodes_expected = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, new_nodes_expected)
        print("🔥🔥🔥")
        print(new_nodes)
        print(new_nodes_expected)
        print("🔥🔥🔥")
        
    def test_unmatched_delimiter(self):
        node = TextNode("This is text with a italic* word", TextType.TEXT)
        
        new_nodes_expected = [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word", TextType.TEXT),
        ]
        print("HMMM")
        with self.assertRaises(Exception) as cm:
            new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        self.assertIn("Invalid Markdown Syntax Unmatched delimiter", str(cm.exception))
        print("HMMM")

    def test_just_text(self):
        node = TextNode("This is just text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        new_nodes_expected = [
        TextNode("This is just text", TextType.TEXT),

        ]
        self.assertEqual(new_nodes, new_nodes_expected)
        print("🔥🔥🔥")
        print(new_nodes)
        print(new_nodes_expected)
        print("🔥🔥🔥")


if __name__ == "__main__":
    unittest.main()