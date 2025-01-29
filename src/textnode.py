from enum import Enum
from leafnode import LeafNode
from htmlnode import HTMLNode

# enum for text type
class TextType(Enum):
    TEXT = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

# textnode class construction
class TextNode():
    def __init__(self, text,  text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # equality comparison for testing
    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return 
    
    # outputs a string of attributes for testing 
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    # converts to Leaf or HTML node based on text type
    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC: 
                return HTMLNode("i", self.text)
            case TextType.CODE:
                return HTMLNode("code", self.text)
            case TextType.LINK:
                return HTMLNode("a", self.text, None,{"href" : self.url})
            case TextType.IMAGE:
                return HTMLNode("img", "",None, {"src" : self.url, "alt" : self.text})
            case _:
                raise Exception("Invalid node type")