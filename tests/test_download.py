import unittest

from utils.downloader import get_file_name, download_single_file, download_a_folder


class TestGoogleDriveDownloader(unittest.TestCase):
    def test_get_file_name(self):
        get_file_name('https://drive.google.com/file/d/13ZBJ6P_UvicQFZmuHQ4CumT_8mwvX9YE/view')

    def test_download_single_file(self):
        download_single_file('https://drive.google.com/file/d/13ZBJ6P_UvicQFZmuHQ4CumT_8mwvX9YE/view',
                             '.')

    def test_download_a_folder(self):
        download_a_folder('https://drive.google.com/drive/folders/1iM2Pt85FQeNyXtm1vRGbEhHlRvufbBLe?usp=sharing',
                          '.')


if __name__ == '__main__':
    unittest.main()
