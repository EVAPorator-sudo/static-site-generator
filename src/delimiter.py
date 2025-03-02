from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Process text nodes for delimiters
        text = old_node.text
        pieces = []
        remaining_text = text
        in_delimiter = False
        
        while delimiter in remaining_text:
            split_index = remaining_text.find(delimiter)
            if split_index > 0:
                pieces.append((remaining_text[:split_index], in_delimiter))
            
            # Move past this delimiter
            remaining_text = remaining_text[split_index + len(delimiter):]
            in_delimiter = not in_delimiter
        
        # Add any remaining text
        if remaining_text:
            pieces.append((remaining_text, in_delimiter))
        
        # If we're still inside a delimiter at the end, that's an unmatched delimiter
        # But instead of raising an exception, we'll just treat the text normally
        if in_delimiter:
            # Just add the original node as-is
            new_nodes.append(old_node)
        else:
            # Convert the pieces to nodes
            for piece_text, is_delimited in pieces:
                if not piece_text:
                    continue
                    
                if is_delimited:
                    # This text is between delimiters, apply special formatting
                    new_nodes.append(TextNode(piece_text, text_type))
                else:
                    # This is regular text
                    new_nodes.append(TextNode(piece_text, TextType.TEXT))
    
    return new_nodes