import os
# from imageprep.utils_cls import OrganizeOneFolder, OrganizeMultipleFolders

cur_dir = os.path.dirname(__file__)


def test_organize_folder():
    pass
# mif = '~/projects/mltut/UCMerced_LandUse/images/'

# path to images and labels
# image_path = os.path.join(cur_dir, 'data', 'balloon/images/')
# label_path = os.path.join(cur_dir, 'data', 'balloon/abs_label/')
# yolo_label = os.path.join(cur_dir, 'data', 'balloon/yolo_label/')
#
# f1 = OrganizeOneFolder(image_path)
# r1 = f1.read_images_as_array()
# print([i.shape for i in r1])
# OrganizeOneFolder(mif).resize_images_in_one_folder()
# f2 = OrganizeMultipleFolders(mif)
# # print(f2.class_names())
# # print(len(f2))
# R1 = f2.call_read_images_as_array()
# print(R1)

# for val in range(len(f2)):
#    img = f2[val]
#    img_arr  = OrganizeImageFolder(mif).read_images_as_array()
#    print(img_arr)
