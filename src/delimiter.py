from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            if text.count(delimiter) %2 != 0:
                raise Exception("unmatched delimiter")
            split_text = text.split(delimiter)
            type = TextType.TEXT
            if text[0] == delimiter:
                type = node.text_type
            for string in split_text:
                if string:
                    new_nodes.append(TextNode(string, type))
                if type == text_type:
                    type = TextType.TEXT
                else:
                    type = text_type
    return new_nodes