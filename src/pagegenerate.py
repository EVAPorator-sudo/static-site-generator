import os
from markdowntohtml import markdown_to_html
from extract_title import extract_title

def directory_gen(path):
    split_path = path.split("/")[:-1]
    current_directory = ""
    for directory in split_path:
        if not current_directory:
            current_directory = directory
        else:
            current_directory += f"/{directory}"
        if not os.path.exists(current_directory):
            os.mkdir(current_directory)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"generating page from {from_path} to {dest_path} from {template_path}")
    with open(from_path, 'r') as from_file:
        markdown = from_file.read()
    with open(template_path, 'r') as template_file:
        template = template_file.read()
    content = markdown_to_html(markdown)
    title = extract_title(markdown)
    template = template.replace("Title", title)
    template = template.replace("Content", content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace("href='/", f"href='{basepath}")
    template = template.replace('src="/', f'src="{basepath}')
    template = template.replace("src='/", f"src='{basepath}")
    directory_gen(dest_path)
    with open(dest_path, 'w') as dest_file:
        dest_file.write(template)