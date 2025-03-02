from pagegenerate import generate_page
import os

def generate_page_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True) # if the destination directory doesent exist create it
    directory = os.listdir(dir_path_content)
    for path in directory: # iterates over everythin in the directory
        fullpath = os.path.join(dir_path_content, path) 
        destpath = os.path.join(dest_dir_path, path) # determines the path to pull the content from and the destination
        if os.path.isfile(fullpath) == True:
            if fullpath.endswith(".md"):
                destpath = destpath.removesuffix(".md")
                generate_page(fullpath, template_path, f"{destpath}.html", basepath) # if it is a markdown file convert it into html and copy to the target directory
        else:
            dest_subdir_path = os.path.join(dest_dir_path, path)
            generate_page_recursively(fullpath, template_path, dest_subdir_path, basepath) # if it is a subdirectory repeat the process inside 