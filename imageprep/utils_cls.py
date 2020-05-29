import os
import numpy as np
from PIL import Image


class OrganizeImageFolder:

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

        for file in file_name:
            img = Image.open(os.path.join(self.path, file))
            resize_image = img.resize((output_size, output_size), Image.ANTIALIAS)
            if save is True:
                resize_image.save(file, 'JPEG', quality=90)
            else:
                print("Image Resized but not Saved")


class OrganizeImageFolders:

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
        for folders in os.listdir(self.path):
            if not folders.startswith("."):
                print(folders)


mif = '/Users/eddiebedada/projects/mltut/UCMerced_LandUse/images/'
cur_dir = '/Users/eddiebedada/to24/ai_assurance/sprint_6/imageprep/tests/'
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'balloon/images/')
label_path = os.path.join(cur_dir, 'data', 'balloon/abs_label/')
yolo_label = os.path.join(cur_dir, 'data', 'balloon/yolo_label/')


f1 = OrganizeImageFolder(image_path)
#print(len(f1))
#print(f1[2])
print(f1.resize_images_in_one_folder())


# f2 = OrganizeImageFolders(mif)
# print(f2.class_names())
# print(len(f2))
#
#
