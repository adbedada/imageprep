import os
from imageprep import data
from imageprep.yolo import *


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


# output folder
output_path = os.path.join(data_dir, 'yolo_labels/')


def test_convert_to_yolo():
    yolo_labels = convert_to_yolo(image_path, label_path, output_path)
    print("Output for label file with one bbox: ", yolo_labels)


