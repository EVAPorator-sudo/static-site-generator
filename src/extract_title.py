import re
def extract_title(markdown):
    lines = markdown.split("\n")
    title_regex = r"^#\s*(.+)$"
    for line in lines:
        if re.match(title_regex, line):
            return line[2:].strip(" ")
    raise Exception("No Valid Header")