from leafnode import LeafNode
node = LeafNode("h1", "this is a test node", {"href": "https://www.google.com"})
print(node.__str__())
print(node.to_html())