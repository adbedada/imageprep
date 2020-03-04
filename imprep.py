import os
import re
from PIL import Image


def resize_images_in_one_folder(path, output_size=256):

    """
     Re-sizes images in one folder

    :param path: path to the folder
    :return: re-sized images saved in the same folder
    """
    dirs = os.listdir(path)
    for item in dirs:
        print(dirs)
        if os.path.isfile(path+item):
            if item.endswith(".jpg"):
                im = Image.open(path+item)

                f, e = os.path.splitext(path+item)

                imResize = im.resize((output_size,output_size), Image.ANTIALIAS)
                imResize.save(f + '.jpg', 'JPEG', quality=90)


def resize_images_from_multiple_folders(path, output_size=256):

    """
    Re-sizes images in multiple folders and saves images in each respective folder
    :param path: path to the folder containing all folders with images
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


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    return x, y, w, h


def reverse(size, box):
    dw = size[0]
    dh = size[1]
    xmin = int(((dw * box[0]) * 2) - dw)
    ymin = int(((dh * box[1]) * 2) - dh)

    xmax = int((dw * box[2]) + xmin)
    ymax = int((dw * box[3]) + ymin)

    return xmin, ymin, xmax, ymax


def convert_to_yolo(input_label_path, output_label_path,output_images):

    g = open("output.txt", "w")
    for file in os.listdir(input_label_path):

        if ".txt" in file:
            filename = file[:-4] + ".jpg"

            input_file = open(os.path.join(input_label_path + file))
            file = file[:-4] + '.txt'

            output_file = open(output_label_path + file, "w")

            file_path = output_images + filename

            g.write(file_path + "\n")
            for line in input_file.readlines():
                match = re.findall(r"(\d+)", line)

                if match:
                    xmin = float(match[0])
                    ymin = float(match[1])
                    xmax = float(match[2])
                    ymax = float(match[3])

                    b = (xmin, xmax, ymin, ymax)
                    im = Image.open(file_path)
                    size = im.size
                    bb = convert(size, b)

                    output_file.write("0" + " " + " ".join([str(a) for a in bb]) + "\n")

            output_file.close()
            input_file.close()
    g.close()


def list_path_to_files(path_to_folders, output_file_name, output_file_extension='.png'):
    """
    saves the list of directory path to files (images or labels) in one text file

    :param path_to_folders: path to the folder containing images or labels
    :param output_file_name: name of output text file (include *txt extension when providing name)
    :param output_file_extension: file extension for the output

    :return: a text file with a list of path to files
    """

    # file extensions
    extension = ['jpg', 'png', 'tif', 'jpeg', 'tiff']

    txt = open(os.path.join(path_to_folders, output_file_name), 'w')
    counter = 0
    files = os.listdir(path_to_folders)
    for f in files:
        if f.split('.')[-1] in extension:
            title, ext = f.split('.')
            txt.write(path_to_folders + title + output_file_extension + "\n")
            counter = counter + 1

list_path_to_files('../sample', 'sample.txt')