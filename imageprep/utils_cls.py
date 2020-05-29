import os
import numpy as np
from PIL import Image


class OrganizeImages:

    def __init__(self, path, output_size=256, with_extension=False):
        self.path = path
        self.output_size = output_size
        self.with_extension = with_extension

    def __len__(self):
        return len(self.read_images())

    def __getitem__(self, index):
        return self.read_images()[index]

    def read_images(self):

        name_list = []
        extension = ['.jpg', '.png', '.tif', '.jpeg', '.tiff']

        if os.listdir(self.path):
            files = os.listdir(self.path)
            for f in files:
                if os.path.splitext(f)[-1] in extension:
                    if self.with_extension is True:
                        name_list.append(f)
                    else:
                        title, ext = os.path.splitext(f)
                        name_list.append(title)

        else:
            for folders in os.listdir(self.path):
                folders_list = os.path.join(self.path, folders)
                print(folders_list)
                folder_path = os.path.join(self.path, folder)
                for files in os.listdir(folder_path):

                    for f in files:

                        if os.path.splitext(f)[-1] in extension:
                            if self.with_extension is True:
                                name_list.append(f)
                            else:
                                title, ext = os.path.splitext(f)
                                name_list.append(title)

        return name_list

    def resize_images_in_one_folder(self, output_size=256, save=False):

        file_name = self.read_images()

        for file in file_name:
            img = Image.open(os.path.join(self.path, file))
            resize_image = img.resize((output_size, output_size), Image.ANTIALIAS)
            if save is True:
                resize_image.save(file, 'JPEG', quality=90)
            else:
                return resize_image





mif = '/Users/eddiebedada/projects/mltut/UCMerced_LandUse/images/'
cur_dir = '/Users/eddiebedada/to24/ai_assurance/sprint_6/imageprep/tests/'
# path to images and labels
image_path = os.path.join(cur_dir, 'data', 'balloon/images/')
label_path = os.path.join(cur_dir, 'data', 'balloon/abs_label/')
yolo_label = os.path.join(cur_dir, 'data', 'balloon/yolo_label/')


folder = OrganizeImages(image_path, with_extension=True)

fnames = folder.read_images()
print(fnames)






