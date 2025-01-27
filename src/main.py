from textnode import TextNode, TextType

def main():
    Node = TextNode("abcd", TextType.NORMAL, "https://www.this-is-fake.com")
    print(Node.__repr__())

main()