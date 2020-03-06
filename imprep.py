import os
import re
import glob
import json
import numpy as np
from PIL import Image


def image_names(path_to_folder):
    """
    Reads raster files from multiple folders and returns their names

    :param path_to_folder: directory path
    :return: names of the raster files
    """

    # common image file extensions
    extension = ['jpg', 'png', 'tif', 'jpeg', 'tiff']
    files = os.listdir(path_to_folder)
    name_list = []

    for f in files:
        if f.split('.')[-1] in extension:
            title, ext = f.split('.')
            name_list.append(title)

    return name_list


def pad_image(image_file_name, new_size=(600, 600), save=False):

    """
    Pad Image with a given number of rows and columns
    :param image_file_name: image file
    :param new_size: now image size
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
    """
    Conversion for Object detection labels to YOLO format

    :param size: image size
    :param box: bounding box
    :return: yolo format labels
    """
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
    """
    Reverse YOLO label format to anchors bbox

    :param size: Size of the image
    :param box: YOLO labels
    :return: Anchor bbox values
    """
    dw = size[0]
    dh = size[1]
    xmin = int(((dw * box[0]) * 2) - dw)
    ymin = int(((dh * box[1]) * 2) - dh)
    xmax = int((dw * box[2]) + xmin)
    ymax = int((dw * box[3]) + ymin)

    return xmin, ymin, xmax, ymax


def convert_to_yolo(input_label_path, output_label_path,output_images):
    """
    Converts labels to YOLO

    :param input_label_path:
    :param output_label_path:
    :param output_images:
    :return:
    """
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
    Saves the path to files (images or labels) in one text file

    :param path_to_folders: path to the folder containing images or labels
    :param output_file_name: name of output text file
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


def image_as_array(file):
    """
     Reads image and returns a numpy array

    :param file: image file name
    :return: numpy array
    """
    img = Image.open(file)
    img_arr = np.asarray(img)
    return img_arr


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
                img_arr = image_as_array(path+item)
                img_arr = np.expand_dims(img_arr, axis=0)
                img_arr_list.append(img_arr)

    img_stack = np.vstack(img_arr_list)

    return img_stack


def read_labels(input_path, ext='.txt'):

    dir = os.listdir(input_path)
    label_content = []
    for item in dir:
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


def create_id(path):
    dir = os.listdir(path)
    items =[]
    num = 0
    for item in dir:
        num +=1
        items.append([num, item])
    return items


def read_label_as_dict(file,ext='.txt'):
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
    label_content = []
    if os.path.isfile(file):
        if file.endswith(ext):
            content = []
            input_file = open(file)
            #file_name = file.split('/')[-1]
            for line in input_file.read().splitlines():
                content.append([line])
            if len(content) != 1:
                label_content.append([file, content])
            else:
                label_content.append([file, content[0]])

    return label_content



def coco_json_names(path):
    obj ={}
    labels = read_labels(path)
    for idx, label in enumerate(labels):
        names, bbox = (label[0],label[1])
        return names, bbox


def coco_json(path,output_file):
    obj = {}
    labels = read_labels(path)
    for key, (old_key, value) in enumerate(labels):
        nkey = key+1
        obj[key] = [old_key,value]

    with open(output_file, 'w') as f:
        json.dump(obj,f)

    return obj
    # for file in os.listdir(path):
    #     file_path = path+file
    #     obj['file_name'] = file_path
    #     label = []
    #     for idx, bbox in enumerate(read_label_as_list(file_path)):
    #
    #         obj['idx'] = idx

    return obj


