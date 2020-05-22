import re
from imageprep.utils import *


def yolo_label_format(size, box):
    """
     Rule to convert anchors to YOLO label format

     Expects the box to have (xmin, ymin, xmax, ymax)

    :param size: Height and width of the image as a list
    :param box: the four corners of the bounding box as a list
    :return: YOLO style labels
    """
    dw = 1. / size[0]
    dh = 1. / size[1]

    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    return x, y, w, h


def reverse_yolo_to_absolute(size, box):
    """
     Rule to reverse YOLO label format to anchors bbox

    :param size: Size of the image
    :param box: YOLO labels
    :return: Anchor bbox values
    """

    # src: https://github.com/CosmiQ/yolt/blob/653829c5745d7bde7120e4f6bae8600b2ada4554/scripts/convert.py#L105

    # dw = size[0]
    # dh = size[1]
    # xmin = int(((dw * box[0]) * 2) - dw)
    # ymin = int(((dh * box[1]) * 2) - dh)
    # xmax = int((dw * box[2]) + xmin)
    # ymax = int((dw * box[3]) + ymin)

    x, y, w, h = box
    dw = 1./size[0]
    dh = 1./size[1]
    w0 = w/dw
    h0 = h/dh
    x_center = x/dw
    y_center = y/dh

    xmin, xmax = x_center - w0/2., x_center+ w0/2.
    ymin, ymax = y_center - h0/2., y_center + h0/2.

    return int(xmin), int(ymin), int(xmax), int(ymax)


def convert_to_yolo(image_path, input_path, output_path):
    """
     Converts labels to YOLO data format

    :param image_path: path to the folder containing images
    :param input_path:  path to the corresponding labels
    :param output_path: path to output folder for the YOLO labels
    :return: YOLO style labels
    """

    for file in os.listdir(input_path):

        if ".txt" in file:
            filename = file[:-4] + ".jpg"
            input_file = open(os.path.join(input_path + file))
            file = file[:-4] + '.txt'
            output_file = open(output_path + file, "w")
            file_path = image_path + filename

            for line in input_file.readlines():
                match = re.findall(r"(\d+)", line)
                b_val = []
                if match:
                    if len(match) == 5:
                        xmin = float(match[1])
                        ymin = float(match[2])
                        xmax = float(match[3])
                        ymax = float(match[4])

                        b_val.append([xmin, ymin, xmax, ymax])

                    else:
                        xmin = float(match[0])
                        ymin = float(match[1])
                        xmax = float(match[2])
                        ymax = float(match[3])
                        b_val.append([xmin, ymin, xmax, ymax])

                    b = (b_val[0][0], b_val[0][1], b_val[0][2], b_val[0][3])

                    im = Image.open(file_path)
                    size = im.size
                    bb = yolo_label_format(size, b)

                    output_file.write("0" + " " + " ".join([str(a) for a in bb]) + "\n")

            output_file.close()
            input_file.close()


def convert_from_yolo(image_path, input_path, output_path):
    """
     Converts labels to YOLO data format

    :param image_path: path to the folder containing images
    :param input_path:  path to the corresponding labels
    :param output_path: path to output folder for the YOLO labels
    :return: YOLO style labels
    """
    for file in os.listdir(input_path):

        if ".txt" in file:
            filename = file[:-4] + ".jpg"
            input_file = open(os.path.join(input_path + file))
            file = file[:-4] + '.txt'
            output_file = open(output_path + file, "w")
            file_path = image_path + filename

            for line in input_file.readlines():
                match = line.strip().split(' ')

                if match:
                    objcls = match[0]
                    xcenter = float(match[1])
                    ycenter = float(match[2])
                    width = float(match[3])
                    height = float(match[4])

                    b = (xcenter, ycenter, width, height)
                    im = Image.open(file_path)
                    size = im.size
                    bb = reverse_yolo_to_absolute(size, b)

                    output_file.write(objcls+ " " + " ".join([str(a) for a in list(bb)]) + "\n")

            output_file.close()
            input_file.close()
