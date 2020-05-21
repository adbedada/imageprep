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

    im = utils.read_image(os.path.join(img_path,f))
    width, height,depth = im.shape

    root = Element("annotations")
    folder = SubElement(root, "folder")
    folder.text = img_path

    fname = SubElement(root, "filename")
    fname.text = str(f)

    path = SubElement(root, "path")
    path.text = str(os.path.join(img_path, f))

    outfile = f[:-4] + '.xml'
    tree = ElementTree.tostring(root)
    output_file = open(out_path + outfile, "w")
    output_file.write(str(tree))

