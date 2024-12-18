import click

@click.group()
def main():
    pass


@click.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def convert(input_file, output_file):
    output_file.write(input_file.read().upper())


if __name__ == '__main__':
    main()