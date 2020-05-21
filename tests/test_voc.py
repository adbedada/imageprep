import os
from imageprep import voc


cur_dir = path = os.path.dirname(__file__)
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'balloon/images/')
label_path = os.path.join(cur_dir, 'data', 'balloon/abs_label/')
output_path = os.path.join(cur_dir, 'data', 'balloon/voc_label/')


def test_list_path_to_files():
    voc.convert_to_voc(image_path, label_path, output_path)
    print("Completed!")
