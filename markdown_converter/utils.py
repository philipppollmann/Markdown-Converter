"""
This module contains utility functions that are used in the markdown_converter package.
"""

import os
import mimetypes


def is_directory(path) -> bool:
    """
    Check if the path is a directory
    :param path:
    :return:
    """
    return os.path.isdir(path)


def is_file(path) -> bool:#
    """
    Check if the path is a file
    :param path:
    :return:
    """
    return os.path.isfile(path)


def get_file_type(file_path) -> str:
    """
    Get the file type of the file
    :param file_path:
    :return:
    """
    file_type, _ = mimetypes.guess_type(file_path)
    return file_type
