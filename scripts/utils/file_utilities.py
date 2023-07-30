import os
import glob


def get_path():
    try:
        path = os.path.dirname(os.path.realpath(__file__))
    except:
        path = os.path.dirname(os.path.realpath("__file__"))

    return path


def find_files(path, extension):
    return glob.glob(f"{path}/*.{extension}")


def find_most_recent_file(path, extension):
    files = find_files(path, extension)
    return max(files, key=os.path.getctime)
