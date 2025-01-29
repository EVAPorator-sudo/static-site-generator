from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    # recursively converts children into valid nested HTML syntax
    def children_to_html(self):
        return ''.join(child.to_html() for child in self.children)
    
    # converts self into valid HTML syntax
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        children_html = self.children_to_html()
        props_html = self.props_to_html() if self.props else ""
        if (len(self.children) == 1 and isinstance(self.children[0], ParentNode) and self.children[0].tag == self.tag):
            return self.children[0].to_html()
        return f"<{self.tag} {props_html}>{children_html}</{self.tag}>" if props_html else f"<{self.tag}>{children_html}</{self.tag}>"
