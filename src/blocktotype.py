import re

def block_to_block_type(block):
    blocktype = {"heading" : r"^#{1,6}\s.*", "code" :r"^```.*```$", "quote" : r"^(>>>.*\n?)+", "unordered_list" : r"^[\*\-]\s.*$"}
    for type in blocktype:
        if re.match(blocktype[type], block):
            return type
    split_block = block.split("\n")
    if all(line.strip().startswith(("* ", "- ")) for line in split_block):
        return "unordered_list"
    if all(re.match(r"^\d+\.\s.*", line.strip()) for line in split_block):
        numbers = [int(line.split('.')[0]) for line in split_block]
        if numbers == list(range(1, len(numbers) + 1)):
            return "ordered_list"
    return "paragraph"