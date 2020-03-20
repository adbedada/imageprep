import os
from imageprep.coco import *


cur_dir = path = os.path.dirname(__file__)
#
image_path = os.path.join(cur_dir, 'data', 'images/')
label_path = os.path.join(cur_dir, 'data', 'labels/')
#
# one bbox in a single file
image_file0 = os.path.join(cur_dir, 'data', 'images/80_7.jpg')
label_file0 = os.path.join(cur_dir, 'data', 'labels/80_7.txt')

# multiple bboxes in a single file
image_file1 = os.path.join(cur_dir, 'data', 'images/145_28.jpg')
label_file1 = os.path.join(cur_dir, 'data', 'labels/145_28.txt')


def test_bbox_list():
    """checks bbox loading from files"""
    single_bbox_list = bbox_list(label_file0)
    assert len(single_bbox_list) == 1
    assert single_bbox_list == [{'bbox': [267, 223, 391, 319]}]

    multiple_bbox_list = bbox_list(label_file1)
    assert len(multiple_bbox_list) > 1
    assert multiple_bbox_list == [{'bbox': [336, 398, 416, 416]},
                                  {'bbox': [3, 91, 105, 163]},
                                  {'bbox': [134, 31, 196, 95]}]


def test_image_metadata():
    """checks proper mete data collection of image """
    single_image = image_metadata(image_file1)
    assert single_image['file_name'].split('/')[-1] == '145_28.jpg'
    assert single_image['height'] == 416
    assert single_image['width'] == 416


def test_folder_metadata():
    folder_meta = folder_metadata(image_path, label_path, label_ext='.txt')
    print(folder_meta)


def test_image_folder_metadata_with_id():
    folder_images = image_folder_metadata_with_id(image_path)
    assert type(folder_images) == list
    assert len(folder_images) == 4
    fid = [folder_images[i]['id'] for i in range(0, len(folder_images))]
    assert fid == [0, 1, 2, 3]


def test_coco_format_folder():
    coco_format = coco_format_folder(image_path, label_path)
    first_image = coco_format[0]['image'][0]['file_name'].split('/')[-1]
    xmin_list = []
    for idx, x in enumerate(coco_format):
        anno = x['annotations']
        xmin = anno[0]['bbox'][0]
        xmin_list.append(xmin)

    assert first_image == '145_28.jpg'
    assert xmin_list == [336, 257, 0, 267]
