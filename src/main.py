import os
import sys
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

static_dir = "./static"
public_dir = "./docs"
content_dir = "./content"
template_file = "./template.html"
basepath = "/"


def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print("Cleaning public directory for new content")

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.makedirs(public_dir)

    print("Copying static content to public dir")

    copy_files_recursive(static_dir, public_dir)

    print("Generating new content")

    generate_pages_recursive(content_dir, template_file, public_dir, basepath)


main()
