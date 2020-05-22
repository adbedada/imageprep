import os
from imageprep import yolo


cur_dir = path = os.path.dirname(__file__)
#
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'balloon/images/')
label_path = os.path.join(cur_dir, 'data', 'balloon/abs_label/')
yolo_label = os.path.join(cur_dir, 'data', 'balloon/yolo_label/')
from_yolo = os.path.join(cur_dir, 'data', 'balloon/from_yolo/')

# one bbox in a single file
image_file0 = os.path.join(cur_dir, 'data', 'balloon/images/Img_1.jpg')
label_file0 = os.path.join(cur_dir, 'data', 'balloon/abs_label/Img_1.txt')

# multiple bboxes in a single file
image_file1 = os.path.join(cur_dir, 'data', 'balloon/images/Img_2.jpg')
label_file1 = os.path.join(cur_dir, 'data', 'balloon/abs_label/Img_2.txt')

#yolo label
label_file2 = os.path.join(cur_dir, 'data', 'balloon/yolo_label/Img_1.txt')


def test_convert_to_yolo():
    yolo.convert_to_yolo(image_path, label_path, yolo_label)
    print("Check output folder!")


def test_convert_from_yolo():
    yolo.convert_from_yolo(image_path, yolo_label, from_yolo)
    print("Check output folder!")
