import os
from imageprep import data
from imageprep.utils import *


data_dir = path = os.path.dirname(data.__file__)
#
image_path = os.path.join(data_dir, 'images/')
label_path = os.path.join(data_dir, 'labels/')
#
# one bbox in a single file
image_file0 = os.path.join(data_dir, 'images/79_38.jpg')
label_file0 = os.path.join(data_dir, 'images/79_38.txt')

# multiple bboxes in a single file
image_file1 = os.path.join(data_dir, 'images/145_28.jpg')
label_file1 =  os.path.join(data_dir, 'labels/145_28.txt')


def test_image_names():
    list_of_names = image_names(image_path)
    print("List of Images", list_of_names)


def test_read_label_as_dict():
    dict_label = read_label_as_dict(label_file0)
    print("Label file as a pythondictionary: ", dict_label)


def test_read_labels():
    folder_labels = read_labels(label_path)
    print("Label files in a folder: ", folder_labels)

# def test_list_path_to_files():
#     output= list_path_to_files(image_path)
#     print("List of images", output)
