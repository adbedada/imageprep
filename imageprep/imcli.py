"""imageprep.imcli."""

import click

from imageprep import utils, yolo

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def commands():

    """Dataset Preparation Helper"""
    pass


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-d", "--directory", "directory", help="Path to the image")
def create_path_file(directory):
    """
    Writes out the path to images in a folder as a list

    Args:
        directory: path to dir

    Returns: list of files

    """
    output = utils.list_path_to_files(directory)
    print(output)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-d", "--directory", "directory", help="folder containing images")
@click.option("-e", "--extension", is_flag=False, help="Option to print file extension")
def get_image_name(folder, extension):

    """
     Prints out the names of images in a folder

    Args:
        folder: path to dir
        extension: type of image extension

    Returns: list of image names

    """
    if extension == "True":

        output = utils.image_names(folder, with_extension=True)
    else:
        output = utils.image_names(folder)

    print(output)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "-i", "--image", "image_path", help="Path to the folders containing images"
)
@click.option("-l", "--label", "label_path", help="Path to the corresponding labels")
@click.option(
    "-o", "--output", "output_path", help="Path to output(YOLO labels) folder"
)
def convert_to_yolo(image_path, label_path, output_path):

    """
    Converts absolute bbox values to relative ones

    Args:
        image_path: directory path to images
        label_path: directory path to labels
        output_path: directory path to output

    Returns:

    """

    yolo.convert_to_yolo(image_path, label_path, output_path)
    print("Conversion Completed!")


commands.add_command(create_path_file)
commands.add_command(get_image_name)
commands.add_command(convert_to_yolo)
