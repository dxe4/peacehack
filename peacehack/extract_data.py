import zipfile
import os.path
import os
from glob import glob


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def decompress_files(directory=None):
    directory = directory or os.getcwd()
    files = glob("".join(directory, '*', 'zip'))

    for _file in files:
        decompress_file(_file)


def decompress_file(fname):
    zfile = zipfile.ZipFile(fname)

    for name in zfile.namelist():
        dirname, filename = os.path.split(name)
        dirname = dirname or CURRENT_DIR

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        zfile.extract(name, dirname)

if __name__ == '__main__':
    decompress_files()
