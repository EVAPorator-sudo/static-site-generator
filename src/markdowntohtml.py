import re
from leafnode import LeafNode
from htmlnode import HTMLNode
from markdowntoblock import markdown_to_blocks
from blocktotype import block_to_block_type
from parentnode import ParentNode
from texttonode import text_to_textnode

def type_to_tag(block):
    type = block_to_block_type(block)
    match type:
        case "heading":
            hashnum = len(re.match(r"^#+", block).group())
            return f"h{hashnum}"
        case "code":
            return "pre"
        case "quote":
            return "blockquote"
        case "unordered_list":
            return "ul"
        case "ordered_list":
            return "ol"
        case "paragraph":
            return "p"
    
import re

def formatter(block, tag=None):
    if tag is None:
        tag = type_to_tag(block)
    if tag not in parenttags:
        match tag:
            case tag if tag.startswith("h"):
                return block.strip("#").lstrip(" ")
            case "code":
                return block.strip("```")
            case "blockquote":
                # Handle multiline blockquotes
                lines = block.split("\n")
                formatted_lines = [f"{line.lstrip('> ').strip()}" for line in lines]
                return " ".join(formatted_lines)
            case "li":
                if re.match(r"^\d", block):
                    return re.sub(r"^\d+\.\s", "", block)
                return block.lstrip("- ").lstrip("* ")
    return block

def parentformatter(node):
    tag = node.tag
    if tag in parenttags:
        match tag:
            case "pre":
                return ParentNode(tag, [LeafNode("code", formatter(node.text, "code"))])
            case "ul":
                child_list = []
                for line in node.text.split("\n"):
                    child_list.append(HTMLNode("li", formatter(line, "li")))
                return ParentNode(tag, child_list)
            case "ol":
                child_list = []
                for line in node.text.split("\n"):
                    child_list.append(HTMLNode("li", formatter(line, "li")))
                return ParentNode(tag, child_list)
    else:
        return node
    
def nodetype(node):
    text = node.text
    tag = node.tag
    if tag != "code":
        match tag:
            case "p":
                nodelist = text_to_textnode(text)
                return ParentNode(tag, [text_node.text_node_to_html_node() for text_node in nodelist])
            case "ul":
                parentlist = []
                for line in node.children:
                    nodelist = text_to_textnode(line.text)
                    parentlist.append(ParentNode("li", [text_node.text_node_to_html_node() for text_node in nodelist]))
                return ParentNode(tag, parentlist)
            case "ol":
                parentlist = []
                for line in node.children:
                    nodelist = text_to_textnode(line.text)
                    parentlist.append(ParentNode("li", [text_node.text_node_to_html_node() for text_node in nodelist]))
                return ParentNode(tag, parentlist)
            case tag if tag.startswith('h'):
                nodelist = text_to_textnode(text)
                return ParentNode(tag, [text_node.text_node_to_html_node() for text_node in nodelist])
            case "blockquote":
                nodelist = text_to_textnode(text)
                return ParentNode(tag, [text_node.text_node_to_html_node() for text_node in nodelist])
    return node

def markdown_to_html(markdown):
    global parenttags
    parenttags = ["pre", "ul", "ol"]
    nodelist = []
    blocks = markdown_to_blocks(markdown)
    tohtml = lambda x: HTMLNode(type_to_tag(x), formatter(x))
    html_list = list(map(tohtml, blocks))
    nodelist = list(map(parentformatter, html_list))
    nodes = list(map(nodetype, nodelist))
    return ParentNode("div",nodes).to_html()