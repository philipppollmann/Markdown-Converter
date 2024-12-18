"""
This module contains the command line interface for the markdown_converter package.
"""
import click

@click.group()
def main():
    """
    This is the main entry point for the markdown_converter package.
    :return:
    """
    pass


@click.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def convert(input_file, output_file):
    """

    :param input_file:
    :param output_file:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
