"""
This module is the core module of the markdown_converter package.
"""
from markitdown import MarkItDown

converter = MarkItDown()

def convert_to_markdown(input_file: str) -> str:
    """
    Convert the input file to markdown.

    Args: input_file: The input file to convert.
    Returns: The markdown representation of the input file.
    """

    return converter.convert(input_file).text_content


def store_file(file_path: str, content: str) -> None:
    """
    Store the content in the file.

    Args: file_path: The file path to store the content.
          content: The content to store in the file.
    """

    with open(file_path, 'w') as file:
        file.write(content)
