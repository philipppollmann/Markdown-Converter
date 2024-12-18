import click
import os
from markdown_converter.core import convert_to_markdown
from markdown_converter.utils import is_directory, is_file

@click.group()
def main():
    """
    This is the main entry point for the markdown_converter package.
    """
    pass

@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def convert(input_path: str, output_path: str):
    """
    Convert the input file or directory to markdown and save it to the output file or directory.

    :param input_path: Path to the input file or directory.
    :param output_path: Path to the output file or directory.
    """

    if is_directory(input_path) and is_directory(output_path):
        for root, _, files in os.walk(input_path):
            for file in files:
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_path)
                output_file = os.path.join(output_path, relative_path)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                markdown_content = convert_to_markdown(input_file)
                with open(output_file, 'w') as f:
                    f.write(markdown_content)
    elif is_file(input_path) and is_file(output_path):
        markdown_content = convert_to_markdown(input_path)
        with open(output_path, 'w') as f:
            f.write(markdown_content)
    else:
        raise ValueError("Both input and output paths must be either files or directories.")

main.add_command(convert)

if __name__ == '__main__':
    main()