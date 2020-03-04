
import click
import imprep


@click.command()
@click.option('--directory', 'd', 'directory')
@click.option('--file-path', '-f', 'file_path')
def list_path(directory, file_path):
    imprep.list_path_to_files(directory, file_path)


@click.group(chain=True)
def commands():
    commands.add_command(list_path)
