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
