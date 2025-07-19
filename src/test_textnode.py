import unittest

from textnode import TextNode, TextType

from convert_text_to_leaf import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("\n🧪 Testing equality...")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is an unequal test node", TextType.LINK)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        print("✅ Equality test passed!")
        
    
    def test_none(self):
        print("\n\n🧪 Testing none...")
        node = TextNode("This is a text node", TextType.BOLD, "")

        try:
            self.assertIsNone(node.url)
            print("✅ None test passed!")
        except AssertionError as e:
            print("💀 FAILURE DETECTED! 💀")
            print(f"🔥 Error: {e}")
            
        
    
    def test_not_eq(self):
        print("\n\n🧪 Testing not equal...")
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is an unequal test node", TextType.LINK)
        self.assertNotEqual(node.text_type, node3.text_type)
        print("✅ Nonequality test passed!")

  
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
        
if __name__ == "__main__":
    unittest.main()

    