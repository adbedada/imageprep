import os
import numpy as np
from PIL import Image


def image_names(path_to_folder, with_extension=False):
    """
     Reads raster files from multiple folders and returns their names

    :param path_to_folder: directory path
    :param with_extension: file extension
    :return: names of the raster files
    """

    name_list = []

    # common image file extensions
    extension = ['jpg', 'png', 'tif', 'jpeg', 'tiff']

    if os.path.isdir(path_to_folder):
        files = os.listdir(path_to_folder)
        for f in files:
            if f.split('.')[-1] in extension:

                if with_extension is True:
                    name_list.append(f)
                else:
                    title, ext = f.split('.')
                    name_list.append(title)
    else:
        file = path_to_folder

        if file.split('.')[-1] in extension:

            if with_extension is True:
                name_list.append(file)
            else:
                title, ext = file.split('.')
                name_list.append(title)

    return name_list


def pad_image(image_file_name, new_size=(600, 600), save=False):

    """
     Pad Image with a given number of rows and columns

    :param image_file_name: image file
    :param new_size: now image size
    :param save: option to save output
    :return:
    """
    # src: https://stackoverflow.com/questions/11142851/adding-borders-to-an-image-using-python/39321668#39321668
    image = Image.open(image_file_name)
    rows, cols = image.size

    # Set number of pixels to expand to the left, top, right,
    # and bottom, making sure to account for even or odd numbers

    if rows % 2 == 0:
        add_left = add_right = (new_size[0] - rows) // 2
    else:
        add_left = (new_size[0] - rows) // 2
        add_right = ((new_size[0] - rows) // 2) + 1

    if cols % 2 == 0:
        add_top = add_bottom = (new_size[1] - cols) // 2
    else:
        add_top = (new_size[1] - cols[1]) // 2
        add_bottom = ((new_size[1] - cols[1]) // 2) + 1

    left = 0 - add_left
    top = 0 - add_top
    right = rows + add_right
    bottom = cols + add_bottom

    image = image.crop((left, top, right, bottom))

    if save is True:

        image.save('padded_output.png')

    return image


def resize_images_in_one_folder(path, output_size=256):
    """
     Re-sizes images in one folder

    :param path: path to the folder
    :param output_size: size of the image output
    :return: re-sized images saved in the same folder
    """
    dirs = os.listdir(path)
    for item in dirs:
        if os.path.isfile(path+item):
            if item.endswith(".jpg"):
                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)

                im_resize = im.resize((output_size,output_size), Image.ANTIALIAS)
                im_resize.save(f + '.jpg', 'JPEG', quality=90)


def resize_images_from_multiple_folders(path, output_size=256):
    """
     Re-sizes images in multiple folders and saves images in each respective folder

    :param path: path to the folder containing all folders with images
    :param output_size:
    :return: re-sized images saved in their respective folder
    """

    for folders in os.listdir(path):
        folder_list = os.path.join(path,folders)
        for item in os.listdir(folder_list):
            if item.endswith(".png"):
                file = os.path.join(folder_list,item)

                im = Image.open(file)
                imResize = im.resize((output_size, output_size), Image.ANTIALIAS)

                f, e = os.path.splitext(file)
                imResize.save(f + '.png', 'JPEG', quality=90)


def list_path_to_files(path_to_folders, save=False):
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
    output_file_name = "path.txt"
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


def images_as_array(path, ext='.jpg'):
    """
     Reads multiple images in a folder and returns a stacked numpy array

    :param path: path to the folder containing the images
    :param ext: file extension. defaulted to jpg
    :return: stacked numpy array of images
    """

    dir = os.listdir(path)
    img_arr_list = []
    for item in dir:
        if os.path.isfile(path + item):
            if item.endswith(ext):
                img_arr = read_image(path+item)
                img_arr = np.expand_dims(img_arr, axis=0)
                img_arr_list.append(img_arr)

    img_stack = np.vstack(img_arr_list)

    return img_stack


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
                if len(content) !=1:
                    label_content.append([item, content])
                else:
                    label_content.append([item,content[0]])

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
