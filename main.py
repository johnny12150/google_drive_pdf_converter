import argparse
from glob import glob

from utils.downloader import download_single_file, download_a_folder
from utils.converter import merge_pages


def parsing():
    parser = argparse.ArgumentParser()

    parser.add_argument('url')
    parser.add_argument('output_folder')

    return parser.parse_args()


def main(url, output_folder):
    if 'file/d' in url:
        download_single_file(url, output_folder)
    if 'drive/folders' in url:
        download_a_folder(url, output_folder)

    for file in glob(f'{output_folder}/*.pdf'):
        if not '4_in_1' in file:
            merge_pages(file, f'{file.split(".pdf")[0]}_4_in_1.pdf', 4)
            print(f'{file} has been merged')


if __name__ == '__main__':
    args = parsing()
    main(args.url, args.output_folder)
