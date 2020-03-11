
import click
from imageprep import utils

@click.group()
def commands():
    pass


@click.command()
@click.option('-d', '--directory-to-files', 'directory')
@click.option('-f', '-text-file', 'file')
def list_path(directory, file):
    utils.list_path_to_files(directory, file)


@click.command()
@click.option('-f', '--folder-containing-images', 'folder')
def get_image_name(folder):
    output = utils.image_names(folder)
    print(output)


commands.add_command(list_path)
commands.add_command(get_image_name)
