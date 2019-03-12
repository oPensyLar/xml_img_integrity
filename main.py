import argparse
from PIL import Image
import os
import time
import xml.etree.cElementTree as ET

def check_image(img_filepath):

    try:
        im = Image.open(img_filepath)
        im.verify()
        im.close()
        im = Image.open(img_filepath)
        im.transpose(Image.FLIP_LEFT_RIGHT)
        im.close()

    except:
        return -1

    return 0

def check_xml(xml_filepath):
    tree = ET.parse(xml_filepath)


def main():
    parser = argparse.ArgumentParser(description='Check integrity before create TFRecords')

    parser.add_argument("-x", "--input-xml", dest="xml",
                    help="Input folder XML", metavar="Input folder XMLs")

    parser.add_argument("-i", "--input-image", dest="image",
                    help="Input folder image", metavar="Input folder images")

    args = parser.parse_args()

    if args.xml and args.image:

        print("[+] Checking XML directory " + args.xml)
        all_xml = os.listdir(args.xml)

        for current_file in all_xml:
            filepath = args.xml + current_file
            check_xml(filepath)


        print("[+] Checking JPG directory " + args.image)
        all_imgs = os.listdir(args.image)

        for current_file in all_imgs:
            filepath = args.image + current_file
            retCode = check_image(filepath)

            if retCode == 1:
                print("[!] Image damage: " + filepath)

            time.sleep(1)


main()