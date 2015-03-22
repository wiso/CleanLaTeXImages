import logging
logging.basicConfig(level=logging.INFO)


def find_files(folder):
    import os
    result = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            result.append(file)
    return result


def find_img_in_latex(latex_file):
    result = []
    import re
    regex_string = "\\includegraphics(?:\[.*?\])?\{(.+?)\}"
    r = re.compile(regex_string)
    with open(latex_file) as f:
        it = r.finditer(f.read())
        for m in it:
            if m:
                result.append(m.group(1))
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("latex_file", help="latex file to be scan")
    parser.add_argument("img_folder", help="folder with images")

    args = parser.parse_args()

    logging.info("finding all images in folder %s", args.img_folder)
    img_filenames = find_files(args.img_folder)
    logging.info("parsing %s latex file", args.latex_file)

    print find_img_in_latex(args.latex_file)
