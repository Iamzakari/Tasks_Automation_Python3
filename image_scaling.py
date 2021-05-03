#!/usr/bin/env python3

import os, sys
from PIL import Image


'''This script uses the Python Imaging Library PIL/Pillow
to open resize and rotates given images present in a folder one by one'''


def scale_convert_images(size, inpath, outpath):
    """this fucntion process a folder and resize the image save back to a given folder"""
    #List files in the given directory
    for infile in os.listdir(inpath):
        outfile = os.path.splitext(infile)[0]
        try:
            with Image.open(infile).convert('RGB') as im:
                im.thumbnail(size)
                #rotate degree from 90 to 270
                im.rotate(270).save(outpath + outfile, "JPEG")
        except OSError:
            print("cannot convert", infile)


def main():
    height = int(input("PLease input the height of the image: \n"))
    width = int(input("PLease input the width of the image: \n"))
    new_size =(height, width)
    in_path = input("PLease enter images directory path: \n")
    out_path = input("PLease enter images destination directory path: \n")
    scale_convert_images(new_size, in_path, out_path)

if __name__ == "__main__":
    main()
