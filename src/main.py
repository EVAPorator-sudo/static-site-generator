import os
import sys
import shutil
from genpagerecursive import generate_page_recursively

def copydir(target, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    contents = os.listdir(target)
    for content in contents:
        source_path = os.path.join(target, content)
        dest_path = os.path.join(destination, content)
        if os.path.isfile(source_path) == True:
            shutil.copy(source_path, dest_path)
        else:
            copydir(source_path, dest_path)


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/" # deafaults path if no arguements are given
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    copydir("static", "docs")
    generate_page_recursively("content", "template.html", "docs", basepath)

main()