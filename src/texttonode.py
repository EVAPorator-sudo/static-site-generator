from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from linksplitter import split_nodes_link, split_nodes_image

def text_to_textnode(text):
    node_list = [TextNode(text, TextType.TEXT)]
    delimiter_list = [["**", TextType.BOLD],["*", TextType.ITALIC],["`", TextType.CODE]]
    for delimiter in delimiter_list:
        node_list = split_nodes_delimiter(node_list, delimiter[0], delimiter[1])
    return split_nodes_image(split_nodes_link(node_list))