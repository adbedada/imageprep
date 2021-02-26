import os
import numpy as np
from imageprep.prep import ImageProcessor as IP

cur_dir = os.path.dirname(__file__)
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'tiffs/')

processor = IP(image_path)

def test_image_names():
    list_of_names = processor.list_raster_data()
    assert len(list_of_names) == 4
    print(list_of_names)


def test_read_raster_data():
    gdal_dataset = processor.read_raster_data()
    print(gdal_dataset)


def test_raster_to_array():
    raster_array = processor.raster_to_array()
    assert isinstance(raster_array, np.ndarray)
    print(np.shape(raster_array))

