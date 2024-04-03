#!/usr/bin/env python3

import os
from PIL import Image
from pillow_heif import register_heif_opener
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--directory", default=None, type=str, help="Directory")
parser.add_argument("-o", "--overwrite", default="n", type=str, help="Overwrite/delete original files [y/n]")
args = vars(parser.parse_args())

dirpath = os.path.abspath(args["directory"])
overwrite = True if args["overwrite"] in ["Y", "y"] else False

register_heif_opener()

heic_files = [file for file in os.listdir(dirpath) if file.endswith(".heic")]

for i, file in enumerate(heic_files):
    print(f"Converting {i+1}/{len(heic_files)}")
    image = Image.open(os.path.join(dirpath, file))
    base_name = os.path.splitext(os.path.basename(file))[0]
    image.save(os.path.join(dirpath, f"{base_name}.jpeg"))

if overwrite:
    for i, file in enumerate(heic_files):
        print(f"Deleting {i+1}/{len(heic_files)}")
        os.remove(os.path.join(dirpath, file))

print("Done.")