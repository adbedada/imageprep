import os
from itertools import product
import rasterio as rio
from rasterio import windows
import numpy as np
from osgeo import gdal


class ImageSlicer:
    def __init__(self, input_path, output_path, output_type="png"):
        self.input_path = input_path
        self.output_path = output_path
        self.output_type = output_type
        self.output_tiff = '{}_{}-{}.tif'
        self.output_png = '{}_{}-{}.png'
        self.extension = [".tif", ".tiff"]
        self.width = 256
        self.height = 256

    def get_tiles(self, dataset):
        nols, nrows = dataset.meta['width'], dataset.meta['height']
        offsets = product(range(0, nols, self.width), range(0, nrows, self.width))
        big_window = windows.Window(col_off=0, row_off=0, width=nols, height=nrows)
        for col_off, row_off in  offsets:
            window =windows.Window(col_off=col_off, row_off=row_off, width=self.width, height=self.width).intersection(big_window)
            transform = windows.transform(window, dataset.transform)
            yield window, transform

    def slicer(self):
        list_input = os.listdir(self.input_path)
        for input_f in list_input:
            if os.path.splitext(input_f)[-1] in self.extension:
                with rio.open(os.path.join(self.input_path, input_f)) as src:
                    meta = src.meta.copy()

                    for window, transform in self.get_tiles(src):
                        meta['transform'] = transform
                        meta['width'], meta['height'] = window.width, window.height

                        if self.output_type == "tiff":
                            out_path = os.path.join(self.output_path,
                                                    self.output_tiff.format(os.path.splitext(input_f)[0],
                                                                           int(window.col_off),
                                                                           int(window.row_off)))

                            with rio.open(out_path, 'w', **meta) as sliced_image:
                                sliced_image.write(src.read(window=window))

                        elif self.output_type == "png":
                            profile = src.profile.copy()
                            profile.update(
                                dtype=rio.uint8,
                                driver = "PNG",
                                compress='lzw')
                            out_path = os.path.join(self.output_path,
                                                   self.output_png.format(os.path.splitext(input_f)[0],
                                                                                             int(window.col_off),
                                                                                              int(window.row_off)))

                            with rio.open(out_path, 'w', **profile) as dst:
                                op = src.read(window=window).astype(rio.uint8)
                                dst.write(op)