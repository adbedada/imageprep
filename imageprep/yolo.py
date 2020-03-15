import os
import re
import json
from PIL import Image
from imageprep.utils import *


def yolo_label_format(size, box):
    """
     Rule to convert anchors to YOLO label format

    :param size: Height and width of the image as a list
    :param box: the four corners of the bounding box as a list
    :return: YOLO style labels
    """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    return x, y, w, h


def reverse_yolo_to_anchor(size, box):
    """
     Reverse YOLO label format to anchors bbox

    :param size: Size of the image
    :param box: YOLO labels
    :return: Anchor bbox values
    """
    dw = size[0]
    dh = size[1]
    xmin = int(((dw * box[0]) * 2) - dw)
    ymin = int(((dh * box[1]) * 2) - dh)
    xmax = int((dw * box[2]) + xmin)
    ymax = int((dw * box[3]) + ymin)

    return xmin, ymin, xmax, ymax


def convert_to_yolo(image_path, input_path, output_path):
    """
     Converts labels to YOLO data format

    :param image_path: path to the folder containing images
    :param input_path:  path to the corresponding labels
    :param output_path: path to output folder for the YOLO labels
    :return: YOLO style labels
    """
    g = open("output.txt", "w")
    for file in os.listdir(input_path):

        if ".txt" in file:
            filename = file[:-4] + ".jpg"
            input_file = open(os.path.join(input_path + file))
            file = file[:-4] + '.txt'
            output_file = open(output_path + file, "w")
            file_path = image_path + filename

            g.write(file_path + "\n")
            for line in input_file.readlines():
                match = re.findall(r"(\d+)", line)

                if match:
                    xmin = float(match[0])
                    ymin = float(match[1])
                    xmax = float(match[2])
                    ymax = float(match[3])

                    b = (xmin, xmax, ymin, ymax)
                    im = Image.open(file_path)
                    size = im.size
                    bb = yolo_label_format(size, b)

                    output_file.write("0" + " " + " ".join([str(a) for a in bb]) + "\n")

            output_file.close()
            input_file.close()
    g.close()
