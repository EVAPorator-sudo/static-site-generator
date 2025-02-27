from pagegenerate import generate_page
import os

def generate_page_recursively(dir_path_content, template_path, dest_dir_path):
    directory = os.listdir(dir_path_content)
    for path in directory:
        fullpath = f"{dir_path_content}/{path}"
        destpath = f"{dest_dir_path}/{path}"
        if os.path.isfile(fullpath) == True:
            destpath = destpath.rstrip(".md")
            generate_page(fullpath, template_path, f"{destpath}.html")
        else:
            os.makedirs(destpath)
            generate_page_recursively(fullpath, template_path, f"{dest_dir_path}/{path}")