import os
from imageprep import utils
from xml.etree.ElementTree import Element, SubElement, tostring, XML
from xml.etree import ElementTree
from xml.dom import minidom


"""
VOC FORMAT: 

<?xml version="1.0" ?>
<annotations>
   <folder>../data/balloon/images/</folder>
   <filename>Img_3.jpg</filename>
   <path>../data/balloon/images/Img_3.jpg</path>
   <source>
      <database>unknown</database>
   </source>
   <size>
      <width>1356</width>
      <height>2048</height>
      <depth>3</depth>
   </size>
   <segmented>0</segmented>
   <object>
      <name>0</name>
      <pose>Unspecified</pose>
      <truncated>0</truncated>
      <difficult>0</difficult>
      <occluded>0</occluded>
      <bndbox>
         <xmin>595</xmin>
         <ymin>1</ymin>
         <xmax>848</xmax>
         <ymax>317</ymax>
      </bndbox>
   </object>
   <object>
      <name>1</name>
      <pose>Unspecified</pose>
      <truncated>0</truncated>
      <difficult>0</difficult>
      <occluded>0</occluded>
      <bndbox>
         <xmin>502</xmin>
         <ymin>270</ymin>
         <xmax>1430</xmax>
         <ymax>1355</ymax>
      </bndbox>
   </object>
</annotations>

"""


def convert_to_voc(image_path, label_path, voc_path):
    """
     Creates XML files in Pascal VOC labeling style
    :param image_path: path to the folder containing images
    :param label_path: path to the corresponding labels

       The absolute value label is expected to look like:

            0 236 98 456 372
            0 354 1 577 206
            1 811 25 1023 726
            1 383 164 683 768

        Where 0 and 1 represent classes and
        the bounding class follows xmin,ymin,xmax,ymax style

    :param voc_path: path to output folder for the VOC labels
    :return: Instead of returning values, the function writes outputs
    """

    files = os.listdir(image_path)
    for f in files:

        im = utils.read_image(os.path.join(image_path, f))
        width, height, depth = im.shape

        root = Element("annotations")
        folder = SubElement(root, "folder")
        folder.text = image_path
        # filename
        fname = SubElement(root, "filename")
        fname.text = str(f)
        # dir path
        path = SubElement(root, "path")
        path.text = str(os.path.join(image_path, f))
        # image source
        source = SubElement(root,"source")
        database = SubElement(source,"database")
        database.text = "unknown"
        # dimensions
        size = SubElement(root, "size")
        w = SubElement(size, "width")
        w.text = str(width)
        h = SubElement(size, "height")
        h.text = str(height)
        d = SubElement(size, "depth")
        d.text = str(depth)
        # segmentation
        segmented = SubElement(root, "segmented")
        segmented.text = str(0)
        # bounding box
        counter = 0
        # input text filename
        txt_file = f[:-4] + '.txt'

        bbox = []
        with open(os.path.join(label_path + txt_file)) as input_file:
            for idx, line in enumerate(input_file):
                counter += 1
                # objects
                object = SubElement(root, "object")
                objname = SubElement(object, "name")
                pose = SubElement(object, "pose")
                pose.text = "Unspecified"
                truncated = SubElement(object,"truncated")
                truncated.text = str(0)
                difficult = SubElement(object,"difficult")
                difficult.text = str(0)
                occluded = SubElement(object, "occluded")
                occluded.text = str(0)
                # bounding box
                bndbox = SubElement(object, 'bndbox')
                x_min = SubElement(bndbox, "xmin")
                y_min = SubElement(bndbox, "ymin")
                x_max = SubElement(bndbox, "xmax")
                y_max = SubElement(bndbox, "ymax")

                match = line.strip().split(' ')
                if match:
                    objname.text = str(match[0])
                    xmin = str(match[1])
                    ymin = str(match[2])
                    xmax = str(match[3])
                    ymax = str(match[4])
                    # create a list
                    bbox.append([xmin, ymin, xmax, ymax])

                x_min.text = str(bbox[idx][0])
                y_min.text = str(bbox[idx][1])
                x_max.text = str(bbox[idx][2])
                y_max.text = str(bbox[idx][3])
        # save
        outfile = f[:-4] + '.xml'
        tree = ElementTree.tostring(root, encoding="unicode")
        tree = minidom.parseString(tree).toprettyxml(indent="   ")
        output_file = open(voc_path + outfile, "w")
        output_file.write(tree)
