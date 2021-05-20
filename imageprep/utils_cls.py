import os
import numpy as np
from PIL import Image


class OrganizeOneFolder:

    def __init__(self, path, output_size=256):
        self.path = path
        self.output_size = output_size
        self.Image_list = []
        self.extension = ['.jpg', '.png', '.tif', '.jpeg', '.tiff']

        # def read_images(self):

        if os.listdir(self.path):
            files = os.listdir(self.path)
            for f in files:
                if os.path.splitext(f)[-1] in self.extension:
                    self.Image_list.append(f)

        else:
            f = self.path
            if os.path.splitext(f)[-1] in self.extension:
                self.Image_list.append(f)

    def __len__(self):
        return len(self.Image_list)

    def __getitem__(self, index):
        return self.Image_list[index]

    def resize_images_in_one_folder(self, output_size=256, save=False):

        file_name = self.Image_list
        img_list = []
        for file in file_name:
            img = Image.open(os.path.join(self.path, file))
            resize_image = img.resize((output_size, output_size),
                                      Image.ANTIALIAS)
            if save is True:
                resize_image.save(file, 'JPEG', quality=90)
            else:
                img_list.append(resize_image)

        return img_list

    def read_images_as_array(self):
        img_file = self.Image_list
        img_arr_list = []
        for img in img_file:
            img_path = Image.open(os.path.join(self.path, img))
            img_arr = np.asarray(img_path)
            img_arr_list.append(img_arr)
        return img_arr_list


class OrganizeMultipleFolders:

    def __init__(self, path):
        self.path = path
        self.Image_list = []

        for folders in os.listdir(path):
            folders_list = os.path.join(path, folders)
            if not folders.startswith("."):
                images = os.listdir(folders_list)
                for img in images:
                    self.Image_list.append(img)

    def __len__(self):
        return len(self.Image_list)

    def __getitem__(self, item):

        return self.Image_list[item]

    def class_names(self):
        folders_name = []
        for folders in os.listdir(self.path):
            if not folders.startswith("."):
                folders_name.append(folders)

        return folders_name

    def get_path(self):
        folders_path = []
        for folders in os.listdir(self.path):
            if not folders.startswith("."):
                folders_list = os.path.join(self.path, folders)
                folders_path.append(folders_list)
        return folders_path

    def call_read_images_as_array(self):
        img_arr_list = []
        paths = self.get_path()
        for p in paths:
            img_arr = OrganizeOneFolder(p).read_images_as_array()
            img_arr_list.append(img_arr)
            return img_arr_list
