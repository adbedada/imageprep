import os
from imageprep import utils
from xml.etree.ElementTree import Element, SubElement, tostring, XML
from xml.etree import ElementTree

from bs4 import BeautifulSoup
#from ElementTree_pretty import prettify

# x = your xml
#
#

"""
<annotation>
	<folder>GeneratedData_Train</folder>
	<filename>000001.png</filename>
	<path>/my/path/GeneratedData_Train/000001.png</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>224</width>
		<height>224</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>21</name>
		<pose>Frontal</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<occluded>0</occluded>
		<bndbox>
			<xmin>82</xmin>
			<xmax>172</xmax>
			<ymin>88</ymin>
			<ymax>146</ymax>
		</bndbox>
    </object>
</annotation>

"""

img_path = "../data/images/"
label_path = "../data/labels/"
out_path = "../data/voc/"

img_arr = utils.images_as_array(img_path)

files = os.listdir(img_path)
for f in files:

    im = utils.read_image(os.path.join(img_path, f))
    width, height, depth = im.shape

    root = Element("annotations")
    folder = SubElement(root, "folder")
    folder.text = img_path
    # filename
    fname = SubElement(root, "filename")
    fname.text = str(f)
    # dir path
    path = SubElement(root, "path")
    path.text = str(os.path.join(img_path, f))
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

    object = SubElement(root, "object")
    bndbox = SubElement(object,'bndbox')
    x_min = SubElement(bndbox, "xmin")
    y_min = SubElement(bndbox, "ymin")
    x_max = SubElement(bndbox, "xmax")
    y_max = SubElement(bndbox, "ymax")


    txt_file = f[:-4] + '.txt'
    input_file = open(os.path.join(label_path + txt_file))
    #print(input_file)
    bbox = []
    for line in input_file.readlines():
        match = line.strip().split(' ')

        if match:
            xmin = str(match[0])
            ymin = str(match[1])
            xmax = str(match[2])
            ymax = str(match[3])

            bbox.append([xmin, ymin, xmax, ymax])

    #print(bbox[0][0])
    x_min.text = str(bbox[0][0])
    y_min.text = str(bbox[0][1])
    x_max.text = str(bbox[0][2])
    y_max.text = str(bbox[0][3])



    outfile = f[:-4] + '.xml'
    tree = ElementTree.tostring(root, encoding="unicode")
    output_file = open(out_path + outfile, "w")
    output_file.write(tree)

