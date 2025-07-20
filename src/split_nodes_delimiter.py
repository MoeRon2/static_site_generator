from htmlnode import LeafNode
from textnode import TextNode, TextType
from extract_markdown_links_images import extract_markdown_images, extract_markdown_links

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
        



def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT: # Assuming TextType is accessible
            new_nodes.append(node)
            continue # Move to the next node in old_nodes
        
        node_text = node.text
        img_matches = extract_markdown_images(node_text)

        if not img_matches: # This is true if img_matches is empty
            new_nodes.append(node)
            continue

        while img_matches:
            image_alt, image_link = img_matches[0]
            delimiter = f"![{image_alt}]({image_link})"
            sections = node_text.split(delimiter, 1)
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            node_text = sections[1]   
            img_matches = extract_markdown_images(node_text)
       
        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
        
        

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT: # Assuming TextType is accessible
            new_nodes.append(node)
            continue # Move to the next node in old_nodes
        
        node_text = node.text
        link_matches = extract_markdown_links(node_text)

        if not link_matches: # This is true if link_matches is empty
            new_nodes.append(node)
            continue

        while link_matches:
            link_text, link_url = link_matches[0]
            delimiter = f"[{link_text}]({link_url})"
            sections = node_text.split(delimiter, 1)
            if len(sections[0]) > 0:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            node_text = sections[1]   
            link_matches = extract_markdown_links(node_text)
       
        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
        
        
    return new_nodes


from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    split_nodes_delimiter_bold_result = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    split_nodes_delimiter_italic_result = split_nodes_delimiter(split_nodes_delimiter_bold_result, "_", TextType.ITALIC)
    # split_nodes_delimiter_plain_result = split_nodes_delimiter(split_nodes_delimiter_italic_result , "*", TextType.TEXT)
    split_nodes_delimiter_code_result = split_nodes_delimiter(split_nodes_delimiter_italic_result , '`', TextType.CODE)
    image_split_result = split_nodes_image(split_nodes_delimiter_code_result)
    link_split_result = (split_nodes_link(image_split_result))
    
    return link_split_result
