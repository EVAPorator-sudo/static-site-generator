import re
from textnode import TextNode
from textnode import TextType

def splitter(nodes, type):
    new_node_list = []
    if type == TextType.IMAGE:
                regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    else:
                regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in nodes:
        if node.text_type == TextType.TEXT:
            text = node.text 
            split_text = re.split(regex, text)
            links = re.findall(regex, text)
            for i in range(0, len(links)):
                if split_text[i]:
                    new_node_list.append(TextNode(split_text[i], TextType.TEXT))
                new_node_list.append(TextNode(links[i][0], type, links[i][1]))
            if split_text[-1]:
                new_node_list.append(TextNode(split_text[-1], TextType.TEXT))
        else:
            new_node_list.append(node)
    return new_node_list

def split_nodes_image(old_nodes):
    return splitter(old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return splitter(old_nodes, TextType.LINK)