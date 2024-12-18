import os
import mimetypes


def is_directory(path) -> bool:
    return os.path.isdir(path)


def is_file(path) -> bool:
    return os.path.isfile(path)


def get_file_type(file_path) -> str:
    file_type, _ = mimetypes.guess_type(file_path)
    return file_type