import os
import json
from PIL import Image
from imageprep.utils import *


def bbox_reader(path):
    """
     Return the bounding box of a list with file name and bbox

    :param path: Directory path to the label text file
    :return: Bounding box
    """
    label_list = read_label_as_list(path)
    bbox = label_list[0][1]
    new_bbox = []

    for idx, bb in enumerate(bbox):

        if len(bbox) != 1:
            nbb = bb[0].split()

            for i in range(0, len(nbb)):
                try:
                    nbb[i] = int(nbb[i])
                except ValueError:
                    nbb[i] = float(nbb[i])
            new_bbox.append(nbb)
        else:
            bbox = bbox[0].split()
            for i in range(0, len(bbox)):
                try:
                    bbox[i] = int(bbox[i])
                except ValueError:
                    bbox[i] = float(bbox[i])
            new_bbox.append(bbox)

    return new_bbox


def bbox_list(path):
    """
     Creates a dictionary with the bbox key

    :param path: Directory path to the label text file
    :return: List with a dict of bboxes
    """

    bb_dict = []
    key_list = ['bbox']
    bb_list = bbox_reader(path)

    for idx, bb in enumerate(bb_list):
        idx += 0
        bb_dz = dict(zip(key_list, [bb]))
        bb_dict.append(bb_dz)

    return bb_dict


def bbox_coco(path, save=False):
    """
     Creates a JSON object/Dict with Keys identifying bboxes

    :param path: Directory path to the label text file
    :return: Dictionary with COCO style data format
    """
    obj = {}

    bb_dict = bbox_list(path)

    bz = []
    for idx, value in enumerate(bb_dict):
        idx +=1
        value['id'] = idx

        xmin = int(value['bbox'][0])
        ymin = int(value['bbox'][1])
        xmax = int(value['bbox'][2])
        ymax = int(value['bbox'][3])

        w = xmax - xmin
        h = ymax - ymin
        bz.append([w, h])

        value["segmentation"] = []
        value["area"] = h*w
        value["category_id"] = 0

    obj["annotations"] = bb_dict

    if save is True:

        output_file = 'data/data.json'
        with open(output_file, 'w') as f:
            json.dump(obj, f)

    return bb_dict


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


def image_metadata(image, save=False):
    """
     Create a meta data JSON object for an image

    :param image: Path and name of the image
    :param save: Option to Save metadata to a JSON file
    :return: JSON object
    """
    obj = {}
    f_name = []
    img = Image.open(image)
    name = img.filename
    height, width = img.size

    f_name.append(name)
    obj['file_name'] = f_name[0]
    obj['height'] = height
    obj['width'] = width

    if save is True:
        output_file = 'data/data.json'

        with open(output_file, 'w') as f:
            json.dump(obj, f)

    return obj


def image_folder_metadata(path, save=False):
    """
     Creates a JSON metadata list for images in a folder

    :param path: Path to the folder containing the images
    :param save: Option to Save metadata to a JSON file
    :return: The list or JSON object of metadata
    """
    obj = {}
    extension = ['jpg', 'png', 'tif', 'jpeg', 'tiff']
    img_list = []

    if os.path.isdir(path):
        files = os.listdir(path)
        for f in files:
            if f.split('.')[-1] in extension:
                json_file = image_metadata(path+f)
                img_list.append(json_file)

    if save is True:
        obj['images'] = img_list
        output_file = 'data.json'
        with open(output_file, 'w') as f:
            json.dump(obj, f)

    return img_list


def image_folder_metadata_with_id(path,save=False):
    """
     Creates a JSON metadata with ID for images in a folder

    :param path: Path to the folder containing the images
    :param save: Option to Save metadata to a JSON file
    :return: The list or JSON object of metadata
    """
    obj = {}
    img_list = image_folder_metadata(path)
    obj['images'] = img_list

    for idx, v in enumerate(img_list):
        v['id'] = idx

    if save is True:
        output_file = 'data.json'
        with open(output_file, 'w') as f:
            json.dump(obj, f)

    return img_list


def folder_metadata(img_path, label_path, label_ext='.txt'):
    """
     Creates a dictionary for images and labels in a folder

    :param img_path: Path to the folder containing images
    :param label_path: Path to the folder containing the corresponding labels
    :param label_ext: file extension of the label files. Defaulted to .txt
    :return: Python Dictionary
    """
    img_ext = ['jpg', 'png', 'tif', 'jpeg', 'tiff']

    images_list = []

    if os.path.isdir(img_path):
        images = os.listdir(img_path)
        for image in images:
            if image.split('.')[-1] in img_ext:
                image_file_path = img_path+image
                image_name = image.split('.')[0]
                label_file_path = label_path+image_name+label_ext
                img_label_meta_folder = image_and_label_meta(image_file_path,label_file_path)
                images_list.append(img_label_meta_folder)

    return images_list


def image_and_label_meta(img_path, label_path, save=False):
    """
     Creates JSON object for a single image and label file

    :param img_path: Path to image
    :param label_path: Path to the label file for the image
    :param save: Option to save the object to JSON file
    :return: JSON object
    """
    image_meta = image_metadata(img_path)
    label_meta = bbox_coco(label_path)
    img_name = img_path.split('/')[-1].split('.')[0]
    label_name = label_path.split('/')[-1].split('.')[0]

    obj = {}
    if img_name != label_name:
        print("Files don't match.")
    else:
        obj['image'] = [image_meta]
        obj['annotations'] = label_meta

    if save is True:
        output_file = 'data/data.json'
        with open(output_file,'w') as f:
            json.dump(obj,f)

    return obj


def coco_format_folder(img_path, label_path, save=False):
    """
     Creates JSON object or a dictionary of images and labels with COCO format

    :param img_path: Path to the folder containing images
    :param label_path: Path to the folder containing the corresponding labels
    :param save: Option to save object to file
    :return: JSON object of a Dictionary depending on the option provided.
    """
    obj ={}
    images_list = folder_metadata(img_path, label_path)
    obj['instances'] = images_list
    for idx, v in enumerate(images_list):
        v['image_id'] = idx

    if save is True:
        with open('dataset.json', 'w') as f:
            json.dump(obj, f)

    return images_list
