import logging
logging.basicConfig(level=logging.INFO)
from os.path import join, relpath, dirname, splitext
from os import remove


def find_files(folder):
    import os
    for root, dirs, files in os.walk(folder):
        for file in files:
            yield join(root, file)


def find_img_in_latex(latex_file):
    import re
    regex_string = "\\includegraphics(?:\[.*?\])?\{(.+?)\}"
    r = re.compile(regex_string)
    with open(latex_file) as f:
        it = r.finditer(f.read())
        for m in it:
            if m:
                yield m.group(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("latex_file", help="latex file to be scan")
    parser.add_argument("img_folder", help="folder with images")

    args = parser.parse_args()

    logging.info("finding all images in folder %s", args.img_folder)
    img_filenames = find_files(args.img_folder)
    logging.info("parsing %s latex file", args.latex_file)

    all_used_img = set(find_img_in_latex(args.latex_file))
    main_folder = dirname(args.latex_file)

    print "all images in latex: ", len(all_used_img)
    for img in find_files(args.img_folder):
        img_relpath = relpath(img, main_folder)
        if splitext(img_relpath)[0] not in all_used_img:
            ans = None
            while ans not in ('y', '', 'n'):
                ans = raw_input("remove %s ([y]/n)? " % img)
            if ans in ('', 'y'):
                remove(img)
                print "removed %s" % img
