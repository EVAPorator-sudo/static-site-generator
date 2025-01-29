from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, text, props = None):
        super().__init__(tag, text, None, props)
    
    # converts self into HTML syntax as a string
    def to_html(self):
        if self.text == None:
            raise ValueError("LeafNode must have text")
        elif self.tag == None:
            return self.text
        elif self.props == None:
            return f"<{self.tag}>{self.text}</{self.tag}>"
        else:    
            return f"<{self.tag} {self.props_to_html()}>{self.text}</{self.tag}>"

