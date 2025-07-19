from htmlnode import LeafNode
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    # search for invalid syntax
    count_delimiter = 0
    for node in old_nodes:
        count_delimiter += node.text.count(delimiter)
    if count_delimiter % 2 == 1:
        raise Exception("Invalid Markdown Syntax Unmatched delimiter")
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        node = old_node.text.split(delimiter)
        for index, node_parts in enumerate(node):
            if index % 2 == 1:
                new_nodes.append(TextNode(node_parts, text_type))
            else:
                new_nodes.append(TextNode(node_parts, TextType.TEXT))

    return new_nodes
        
