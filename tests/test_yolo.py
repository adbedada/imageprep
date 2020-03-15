from imageprep.yolo import *


image_path = '../data/images/'
label_path = '../data/labels/'

# one bbox in a single file
image_file0 = 'data/images/79_38.jpg'
label_file0 = '../data/images/79_38.txt'

# multiple bboxes in a single file
image_file1 = '../data/images/145_28.jpg'
label_file1 = '../data/labels/145_28.txt'

# output folder
output_path = '../data/yolo_labels/'


def test_convert_to_yolo():
    yolo_labels = convert_to_yolo(image_path, label_path, output_path)
    print("Output for label file with one bbox: ", yolo_labels)


