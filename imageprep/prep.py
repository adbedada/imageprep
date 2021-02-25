"""
Raster data Preprocessing utility
"""
import numpy as np
import glob
import os.path
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio import features
from osgeo import gdal
from re import sub
from pathlib import Path
from imageprep import utils


def list_raster_data(path):
    """
    Reads raster files from multiple folders and returns their names
    :param path: directory path
    :return: names of the raster files
    """

    images = glob.glob("{}/**/*.tif".format(path), recursive=True)
    image_name = [os.path.basename(tif).split('.')[0]
                  for tif in images]

    # single tiff files
    if len(image_name) == 0:
        image_name = [os.path.basename(path).split('.')[0]]

    return image_name


def read_raster_data(path):
    """
    Reads a set of associated raster bands from a file.
    Can read one or multiple files stored in different folders.
    :param path: file name or directory path
    :return: raster files opened as GDALDataset
    """
    if os.path.isdir(path):
        images = glob.glob("{}/**/*.tif".format(path), recursive=True)
        raster_files = [gdal.Open(f, gdal.GA_ReadOnly) for f in images]
    else:
        raster_files = [gdal.Open(path, gdal.GA_ReadOnly)]

    return raster_files


def raster_to_array(path):
    """
    Converts images inside multiple folders to stacked array
    :param path: directory path
    :return: stacked numpy array
    """
    raster_array = np.stack([raster.ReadAsArray()
                             for raster in read_raster_data(path)],
                             axis=-1)

    return raster_array


def CreateTiff(Name, Array, driver, NDV, GeoT, Proj, DataType, path):
    """
    Converts array to a single or multi band raster file
    :param Name: name of the output tiff file
    :param Array: numpy array to be converted to
    :param driver: output image (data) format
    :param NDV: no Data Value (-9999)
    :param GeoT: geographic transformation
    :param Proj: projection
    :param DataType: array data format
    :return: GeoTiff
    """

    Array[np.isnan(Array)] = NDV

    rows = Array.shape[1]
    cols = Array.shape[0]
    band = Array.shape[2]
    noData = -9999
    driver = gdal.GetDriverByName('GTiff')
    Name_out = os.path.join(path,Name)
    print('tif:'+ Name_out)
    DataSet = driver.Create(Name_out, rows, cols, band, gdal.GDT_Float32)
    DataSet.SetGeoTransform(GeoT)
    DataSet.SetProjection(Proj)

    for i in range(band):
        DataSet.GetRasterBand(i + 1).WriteArray(Array[:, :, i])
        DataSet.GetRasterBand(i + 1).SetNoDataValue(noData)

    DataSet.FlushCache()
    return Name
