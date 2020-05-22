import json
import itertools
from imageprep.utils import *
from imageprep import yolo


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
    :param save: option to save
    :return: Dictionary with COCO style data format
    """
    obj = {}

    bb_dict = bbox_list(path)
    new_bb_dict = []
    bz = []
    for idx, value in enumerate(bb_dict):
        idx +=1
        value['id'] = idx
        obj_class = int(value['bbox'][0])

        xmin = float(value['bbox'][1])
        ymin = float(value['bbox'][2])
        xmax = float(value['bbox'][3])
        ymax = float(value['bbox'][4])

        new_bb_dict = [xmin, ymin,xmax,ymax]

        w = xmax - xmin
        h = ymax - ymin
        bz.append([w, h])

        img_area = h*w
        value["segmentation"] = []
        value['area'] = img_area
        value['bbox'] = new_bb_dict
        value['category_id'] = obj_class

    return bb_dict


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

    # if save is True:
    #     obj['images'] = img_list
    #     output_file = 'data.json'
    #     with open(output_file, 'w') as f:
    #         json.dump(obj, f)

    return img_list


def image_folder_metadata_with_id(path):
    """
     Creates a JSON metadata with ID for images in a folder

    :param path: Path to the folder containing the images
    :param save: Option to Save metadata to a JSON file
    :return: The list or JSON object of metadata
    """

    img_list = image_folder_metadata(path)

    for idx, v in enumerate(img_list):
        v['id'] = idx

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

    images_and_labels_list = []
    image_files = []
    label_files = []

    if os.path.isdir(img_path):
        images = os.listdir(img_path)
        for image in images:
            try:
                if image.split('.')[-1] in img_ext:
                        image_file_path = img_path+image
                        image_name = image.split('.')[0]
                        label_file_path = label_path+image_name+label_ext
                        img_label_meta_folder = image_and_label_meta(image_file_path, label_file_path)
                        image_files.append(image_file_path)
                        label_files.append(label_file_path)
                        images_and_labels_list.append(img_label_meta_folder)

            except ValueError:
                # Exception for mis-match  in the number of files

                if len(image_files) > len(label_files):

                    print('There are more files in the images folder than in the labels folder!')
                elif len(label_files) > len(image_files):
                    print('There are more files in the labels folder than in the images folder!')
                else:
                    print("Check if files match in count!")

    return images_and_labels_list


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

    return obj


def coco_format_folder(img_path, label_path, save=False):
    """
     Creates JSON object or a dictionary of images and labels with COCO format

    :param img_path: Path to the folder containing images
    :param label_path: Path to the folder containing the corresponding labels
    :param save: Option to save object to file
    :return: JSON object of a Dictionary depending on the option provided.
    """
    obj = {}
    images_list = folder_metadata(img_path, label_path)
    obj['instances'] = images_list
    for idx, v in enumerate(images_list):
        v['image_id'] = idx

    if save is True:
        with open('data.json', 'w') as f:
            json.dump(obj, f)

    return images_list


def coco_for_detectron2(img_dir, label_dir, bbox_mode='BoxMode.XYXY_ABS'):
    """
     Creates Detectron2 compatible COCO data format

    :param img_dir: Path to the image containing images
    :param label_dir: Path to the corresponding labels
    :param bbox_mode: Detectron2 specification for the value of bbox.
    :return: Python dictionary
    """
    data_dict = coco_format_folder(img_dir, label_dir)
    dataset_dicts = []

    for idx, v in enumerate(data_dict):

        record = {}
        file_name = v['image'][0]['file_name']
        height = v['image'][0]['height']
        width = v['image'][0]['width']

        record["file_name"] = file_name
        record["height"] = height
        record["width"] = width
        record["image_id"] = idx

        annotations = v['annotations']

        xmin = annotations[0]['bbox'][0]
        ymin = annotations[0]['bbox'][1]
        xmax = annotations[0]['bbox'][2]
        ymax = annotations[0]['bbox'][3]

        poly = [
            (xmin, ymin), (xmax, ymin),
            (xmax, ymax), (xmin, ymax)
        ]
        poly = list(itertools.chain.from_iterable(poly))

        for j in range(0, len(annotations)):
            annotations[j]['bbox_mode'] = bbox_mode
            annotations[j]['segmentation'] = [poly]

        record["annotations"] = annotations
        dataset_dicts.append(record)

    return dataset_dicts


def coco_from_yolo_for_detectron2(img_dir, label_dir, bbox_mode='BoxMode.XYXY_ABS'):
    """
     Creates Detectron2 compatible COCO data format

    :param img_dir: Path to the image containing images
    :param label_dir: Path to the corresponding labels
    :param bbox_mode: Detectron2 specification for the value of bbox.
    :return: Python dictionary
    """
    data_dict = coco_format_folder(img_dir, label_dir)
    dataset_dicts = []
    for idx, v in enumerate(data_dict):

        record = {}
        file_name = v['image'][0]['file_name']
        height = v['image'][0]['height']
        width = v['image'][0]['width']

        record["file_name"] = file_name
        record["height"] = height
        record["width"] = width
        record["image_id"] = idx

        annotations = v['annotations']
        for j, b in enumerate(annotations):
            category_id = b['bbox'][0]

            xmin = b['bbox'][1]
            ymin = b['bbox'][2]
            xmax = b['bbox'][3]
            ymax = b['bbox'][4]

            new_bbox = [xmin, ymin, xmax, ymax]
            abs_bbox = yolo.reverse_yolo_to_absolute((height, width), new_bbox)

            nxmin = abs_bbox[0]
            nymin = abs_bbox[1]
            nxmax = abs_bbox[2]
            nymax = abs_bbox[3]

            poly = [
                (nxmin, nymin), (nxmax, nymin),
                (nxmax, nymax), (nxmin, nymax)
            ]

            poly = list(itertools.chain.from_iterable(poly))

            annotations[j]['bbox'] = abs_bbox
            annotations[j]['bbox_mode'] = bbox_mode
            annotations[j]['category_id'] = category_id
            annotations[j]['segmentation'] = [poly]

            record["annotations"] = annotations
        dataset_dicts.append(record)

    return dataset_dicts
