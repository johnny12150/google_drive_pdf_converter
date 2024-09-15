import unittest

from utils.downloader import get_file_name, download_single_file, download_a_folder


class TestGoogleDriveDownloader(unittest.TestCase):
    def test_get_file_name(self):
        file_name = get_file_name('https://drive.google.com/file/d/13ZBJ6P_UvicQFZmuHQ4CumT_8mwvX9YE/view')

    def test_download_single_file(self):
        pass

    def test_download_a_folder(self):
        pass


if __name__ == '__main__':
    unittest.main()
