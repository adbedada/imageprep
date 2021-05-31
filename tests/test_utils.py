import os
from imageprep import utils


cur_dir = os.path.dirname(__file__)
# path to images and labels
label_path = os.path.join(cur_dir, 'data',
                          'balloon/abs_label/')

label_file1 = os.path.join(cur_dir, 'data',
                           'balloon/abs_label/Img_2.6.141.txt')


def test_read_label_as_dict():
    dict_label = utils.read_label_as_dict(label_file1)
    bboxes = dict_label['bbox']
    assert len(bboxes) == 4


def test_read_labels():
    folder_labels = utils.read_labels(label_path)
    assert len(folder_labels) == 4
    print(folder_labels[0])
