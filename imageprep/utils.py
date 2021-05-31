import os
import numpy as np
from PIL import Image


def list_path_to_files(path_to_folders, output_file_name, save=False):
    """
     Saves the path to files (images or labels) in one text file

    :param path_to_folders: path to the folder containing images or labels
    :param output_file_name: name of output text file
    :param save: option to save list to a text file
    :return: a text file with a list of path to files
    """
    # common file extensions
    extension = ['jpg', 'png', 'tif', 'jpeg', 'tiff']

    files = os.listdir(path_to_folders)
    counter = 0
    cwd = os.getcwd()
    output_file_name = output_file_name
    txt = open(os.path.join(cwd, output_file_name), 'w')
    all_files = []
    for f in files:
        if f.split('.')[-1] in extension:
            if save is True:
                txt.write(path_to_folders + f + "\n")
                counter = counter + 1

            else:
                list_path = path_to_folders+f
                all_files.append(list_path)

    return all_files


def read_image(file, as_array=True):
    """
     Reads image and returns a numpy array

    :param file: image file namec
    :param as_array: option to read image to array.
    :return: numpy array
    """
    img = Image.open(file)
    if as_array is True:
        img = np.asarray(img)
    return img


def read_labels(input_path, ext='.txt'):
    """
     Read multiple label text files

    :param input_path: path to the folder containing the labels text files
    :param ext: name of file extension. defaulted to jpg
    :return:
    """

    folder = os.listdir(input_path)
    label_content = []
    for item in folder:
        if os.path.isfile(input_path+item):
            if item.endswith(ext):
                content = []
                input_file = open(os.path.join(input_path + item))
                for line in input_file.read().splitlines():
                    content.append([line])
                if len(content) != 1:
                    label_content.append([item, content])
                else:
                    label_content.append([item, content[0]])

    return label_content


def read_label_as_dict(file, ext='.txt'):
    """
     Reads a label file in text format as a dictionary

    :param file: Name of the label file
    :param ext: Name of the file extension. Defaulted to text
    :return: A dictionary of the label
    """
    label_content = {}
    if os.path.isfile(file):
        if file.endswith(ext):
            content = []
            input_file = open(file)
            for line in input_file.read().splitlines():
                content.append([line])
            if len(content) != 1:
                label_content['name'] = file
                label_content['bbox'] = content
            else:
                label_content['name'] = file
                label_content['bbox'] = content[0]

    return label_content


def read_label_as_list(file, ext='.txt'):
    """
     Reads a label file in text format as a list

    :param file: Name of the label file
    :param ext: Name of the file extension. Defaulted to text
    :return: Label as a list
    """
    label_content = []
    if os.path.isfile(file):
        if file.endswith(ext):
            content = []
            input_file = open(file)

            for line in input_file.read().splitlines():
                content.append([line])
            if len(content) != 1:
                label_content.append([file, content])
            else:
                label_content.append([file, content[0]])

    return label_content
