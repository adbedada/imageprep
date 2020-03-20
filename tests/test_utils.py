from imageprep.utils import *


cur_dir = path = os.path.dirname(__file__)
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'images/')
label_path = os.path.join(cur_dir, 'data', 'labels/')

# one bbox in a single file
image_file0 = os.path.join(cur_dir, 'data', 'images/79_38.jpg')
label_file0 = os.path.join(cur_dir, 'data', 'images/79_38.txt')

# multiple bboxes in a single file
image_file1 = os.path.join(cur_dir, 'data', 'images/145_28.jpg')
label_file1 = os.path.join(cur_dir, 'data', 'labels/145_28.txt')


def test_image_names():
    list_of_names = image_names(image_path)
    assert len(list_of_names) == 4
    assert list_of_names == ['145_28', '79_38', '79_45', '80_7']


def test_read_label_as_dict():
    dict_label = read_label_as_dict(label_file1)
    bboxes = dict_label['bbox']
    assert len(bboxes) == 3
    assert bboxes[0] == ['336 398 416 416']


def test_read_labels():
    folder_labels = read_labels(label_path)
    assert folder_labels[0][0] == '145_28.txt'
    assert len(folder_labels) == 4

#
# def test_list_path_to_files():
#     output= list_path_to_files(image_path)
#     print("List of images", output)
