from imageprep.coco import *

image_path = '../data/images/'
label_path = '../data/labels/'

# one bbox in a single file
image_file0 = 'data/images/79_38.jpg'
label_file0 = '../data/images/79_38.txt'

# multiple bboxes in a single file
image_file1 = '../data/images/145_28.jpg'
label_file1 = '../data/labels/145_28.txt'


def test_bbox_list():
    single_bbox_list = bbox_list(label_file0)
    print("Output for label file with one bbox: ", single_bbox_list)

    multiple_bbox_list = bbox_list(label_file1)
    print("Output for label file with bboxes: ", multiple_bbox_list)


def test_image_metadata():
    single_image = image_metadata(image_file1)
    print("Metadata for one image: ", single_image)


def test_image_folder_metadata_with_id():
    folder_images = image_folder_metadata_with_id(image_path)
    print("Meadata for images in a folder: ", folder_images)


def test_coco_format_folder():
    coco_format = coco_format_folder(image_path, label_path)
    print("COCO format: ", coco_format)
