import os
from imageprep import utils


cur_dir = os.path.dirname(__file__)
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'balloon/images/')
label_path = os.path.join(cur_dir, 'data', 'balloon/abs_label/')
yolo_label = os.path.join(cur_dir, 'data', 'balloon/yolo_label/')

# one bbox in a single file
image_file0 = os.path.join(cur_dir, 'data', 'balloon/images/Img_1.jpg')
label_file0 = os.path.join(cur_dir, 'data', 'balloon/abs_label/Img_1.txt')

# multiple bboxes in a single file
image_file1 = os.path.join(cur_dir, 'data', 'balloon/images/Img_2.jpg')
label_file1 = os.path.join(cur_dir, 'data', 'balloon/abs_label/Img_2.txt')

#yolo label
label_file2 = os.path.join(cur_dir, 'data', 'balloon/yolo_label/Img_1.txt')
# label_path = os.path.join(cur_dir, 'data', 'labels/')
#
# # one bbox in a single file
# image_file0 = os.path.join(cur_dir, 'data', 'images/79_38.jpg')
# label_file0 = os.path.join(cur_dir, 'data', 'images/79_38.txt')
#
# # multiple bboxes in a single file
# image_file1 = os.path.join(cur_dir, 'data', 'images/145_28.jpg')
# label_file1 = os.path.join(cur_dir, 'data', 'labels/145_28.txt')


def test_image_names():
    list_of_names = utils.image_names(image_path)
    assert len(list_of_names) == 4
    print(list_of_names)


def test_read_label_as_dict():
    dict_label = utils.read_label_as_dict(label_file1)
    bboxes = dict_label['bbox']
    assert len(bboxes) == 4


def test_read_labels():
    folder_labels = utils.read_labels(label_path)
    assert len(folder_labels) == 4
    print(folder_labels[0])


def test_list_path_to_files():
    output = utils.list_path_to_files(image_path)
    print("List of images", output)
