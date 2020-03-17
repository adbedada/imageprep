
from imageprep.yolo import *


cur_dir = path = os.path.dirname(__file__)
#
image_path = os.path.join(cur_dir, 'data', 'images/')
label_path = os.path.join(cur_dir, 'data', 'labels/')

# output folder
output_path = os.path.join(cur_dir, 'data', 'yolo_labels/')

# one bbox in a single file
image_file0 = os.path.join(cur_dir, 'data', 'images/79_38.jpg')
label_file0 = os.path.join(cur_dir, 'data', 'images/79_38.txt')

# multiple bboxes in a single file
image_file1 = os.path.join(cur_dir, 'data', 'images/145_28.jpg')
label_file1 = os.path.join(cur_dir, 'data', 'labels/145_28.txt')


def test_convert_to_yolo():
    yolo_labels = convert_to_yolo(image_path, label_path, output_path)
    print("Output for label file with one bbox: ", yolo_labels)


