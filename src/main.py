import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

static_dir = "./static"
public_dir = "./public"
content_dir = "./content"
template_file = "./template.html"


def main():
    print("Cleaning public directory for new content")

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.makedirs(public_dir)

    print("Copying static content to public dir")

    copy_files_recursive(static_dir, public_dir)

    print("Generating new content")

    generate_pages_recursive(content_dir, template_file, public_dir)


main()
