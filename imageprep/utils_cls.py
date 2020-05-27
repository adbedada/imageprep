import os
import numpy as np
from PIL import Image


class OrganizeFolderData:

    def __init__(self, path, output_size=256, with_extension=False):
        self.path = path
        self.output_size = output_size
        self.with_extension = with_extension


    def read_images(self,path, with_extension):

        name_list = []
        extensions = ['jpg', 'png', 'tif', 'jpeg', 'tiff']





