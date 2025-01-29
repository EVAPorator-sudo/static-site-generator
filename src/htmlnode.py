class HTMLNode():
    def __init__(self, tag = None, text = None, children = None, props = None):
        self.tag = tag
        self.text = text
        self.children = children
        self.props = props
    
    # equality comparison for testing
    def __eq__(self, other):
        return (self.tag == other.tag and self.text == other.text and self.children == other.children and self.props == other.props)

    # not implemented yet
    def to_html(self):
        raise NotImplementedError
    
    # converts properties into HTML syntax
    def props_to_html(self):
        if self.props == None:
            return ""
        parts = []
        for key, value in self.props.items():
            parts.append(f"{key}='{value}'")  
        return ' '.join(parts) 
    
    # outputs attributes as string for testing
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.text}, {self.children}, {self.props})"
