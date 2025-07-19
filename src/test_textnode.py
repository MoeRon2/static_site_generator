import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()

    