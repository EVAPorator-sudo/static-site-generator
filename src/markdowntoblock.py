def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    block_list = []
    block = []
    for line in lines:
        if line:
            block.append(line.strip(" "))
        else:
            if block:
                block_list.append("\n".join(block))
                block = []
    block_list.append("\n".join(block))
    return block_list