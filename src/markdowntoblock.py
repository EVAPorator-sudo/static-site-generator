def markdown_to_blocks(markdown):
    lines = markdown.split("\n")  # Split markdown into lines
    block_list = []
    block = []
    for line in lines:
        if line.startswith("#"):  # Detect headings
            if block:
                block_list.append("\n".join(block))  # Add the current block to the list
                block = []  # Start a new block
            block_list.append(line.strip(" "))  # Add the heading directly as a new block
        elif line and block and line[0] in "*-" and not block[0][0] in "*-":
            if block:
                block_list.append("\n".join(block))
                block = [line]
        elif line: 
            # If the line has content, append it to the current block
            block.append(line.strip(" "))
        elif block and (block[0][0] == "`" or block[0][0] == ">"):  
            # If in a code, quote, or list block, keep appending
            block.append(line)
        else:
            # If the line is empty, finish the current block
            if block:
                block_list.append("\n".join(block))
                block = []
    # Append the last block if it's not empty
    if block:
        block_list.append("\n".join(block))
    return block_list