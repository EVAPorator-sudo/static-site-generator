import os
import shutil
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
    copydir("static", "public")

main()