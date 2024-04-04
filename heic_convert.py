#!/usr/bin/env python3

import os
from PIL import Image
from pillow_heif import register_heif_opener
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("directory", type=str, help="The directory containing the images to be converted.")
parser.add_argument("-o", "--overwrite", action="store_true", help="Overwrite/delete original files")
parser.add_argument("-f", "--format", type=str, default="JPEG", help="Format to convert to (supports JPEG or PNG)")
args = vars(parser.parse_args())

register_heif_opener()

dirpath = os.path.abspath(args["directory"])
heic_files = [file for file in os.listdir(dirpath) if file.endswith(".heic")]

def convert_image(file: str, dir: str) -> None:
    path = os.path.join(dir, file)
    image = Image.open(path)
    base_name = os.path.splitext(os.path.basename(file))[0]
    image.save(os.path.join(dirpath, f"{base_name}.{args["format"].lower()}"), format=f"{args["format"].upper()}")

spinner = ['\\', '|', '/', '-'] 
for i, file in enumerate(heic_files):
    spinchar = spinner[i % len(spinner)]
    print(f"\r{spinchar} Converting {i+1}/{len(heic_files)}", end="", flush=True)
    try:
        convert_image(file, dir=dirpath)
    except Exception as e:
        print(f"An error occured when attempting to convert {file}:\n{e}")

print("\nDone converting.")

if args["overwrite"]:
    for i, file in enumerate(heic_files):
        spinchar = spinner[i % len(spinner)]
        print(f"\rDeleting {i+1}/{len(heic_files)}",end="", flush=True)
        os.remove(os.path.join(dirpath, file))

print("\nDone.")