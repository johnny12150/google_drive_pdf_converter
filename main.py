import os
import shutil
from pathlib import Path

import gdown


def download_single_file(url, destination):
    gdown.download(url, destination, fuzzy=True)


def download_a_folder(url, destination):
    if 'drive/folders' in url:
        file_list = gdown.download_folder(url)

        # Move download files to given place
        for file in file_list:
            if not os.path.isdir(file):
                shutil.move(file, destination)

        # Delete the source folder
        for file in file_list:
            if os.path.exists(Path(file).parent):
                shutil.rmtree(Path(file).parent)
                print(f"Remove folder: {str(Path(file).parent)}")
    else:
        print('Please enter a valid url')

if __name__ == '__main__':
    # Handle a file link (preview page)
    download_single_file('https://drive.google.com/file/d/13ZBJ6P_UvicQFZmuHQ4CumT_8mwvX9YE/view',
                         'download/test.pdf')

    # Handle a folder
    download_a_folder('https://drive.google.com/drive/folders/1iM2Pt85FQeNyXtm1vRGbEhHlRvufbBLe?usp=sharing',
                         'download')
