import os
from imageprep import prep


cur_dir = os.path.dirname(__file__)
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'tiffs/')


def test_image_names():
    list_of_names = prep.list_raster_data(image_path)
    assert len(list_of_names) == 4
    print(list_of_names)


def test_read_raster_data():
    gdal_dataset = prep.read_raster_data(image_path)
    print(gdal_dataset)


def test_raster_to_array():
    raster_array = prep.raster_to_array(image_path)
    print(raster_array)

