import os
from imageprep.slicer import ImageSlicer

cur_dir = path = os.path.dirname(__file__)
# path to images and labels
input_path = os.path.join(cur_dir, 'data', 'tiffs/')
output_path = os.path.join(cur_dir, 'data','tiffs', 'sliced_tiff/')


def test_image_slicer():

    image_slicer = ImageSlicer(input_path, output_path, output_type="png")
    image_slicer.slicer()
