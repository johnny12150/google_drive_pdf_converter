import os
import shutil
import requests
from pathlib import Path

import bs4
import gdown


def get_file_name(url):
    res = requests.get(url)
    html = bs4.BeautifulSoup(res.text, features="html.parser")
    html_title = html.title.get_text()
    return html_title.split(" - Google 雲端硬碟")[0]


def download_single_file(url, destination):
    file_name = get_file_name(url)

    gdown.download(url, f'{destination}/{file_name}', fuzzy=True)


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
                         'download')

    # Handle a folder
    download_a_folder('https://drive.google.com/drive/folders/1iM2Pt85FQeNyXtm1vRGbEhHlRvufbBLe?usp=sharing',
                         'download')
