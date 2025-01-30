import re

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    extracted_images = []
    for image in images:
        extracted_images.append((image[0], image[1]))
    return extracted_images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    extracted_links = []
    for link in links:
        extracted_links.append((link[0], link[1]))
    return extracted_links
