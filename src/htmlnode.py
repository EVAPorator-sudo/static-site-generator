class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string_so_far = ""
        for key in self.props:
            string_so_far += f"{key}={self.props[key]} "
        string_so_far.strip(" ")
        return string_so_far
    
    def __repr__(self):
        return(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")
