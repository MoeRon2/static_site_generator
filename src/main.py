from block_markdown import markdown_to_blocks
from textnode import TextNode, TextType


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
#     blocks_test_string = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """

#     print(blocks_test_string)
#     blocks = markdown_to_blocks(blocks_test_string)

#     print(blocks)
    

main()
