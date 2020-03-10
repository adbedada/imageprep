import imprep

##### PC Dataset #######

image_path = 'data/'
label_path = 'data/'
#image_file = 'data/79_38.jpg'
image_file = 'data/145_28.jpg'
#label_file1 = 'data/79_38.txt'
label_file1 = "data/145_28.txt"
#label_file1 = "data/79_38.txt"
##### GPU Dataset ######
# img_path = '../../dataset/xview/Planes/yolo_planes_test_images/'
# label_path = '../../dataset/xview/Planes/yolo_planes_test_labels/'
# file_path = '../../dataset/xview/Planes/yolo_planes_test_labels/79_45.txt'
################# file path list #######################
# list_path_to_files('../sample', 'sample.txt')

################# Name list ############################
# names = imprep.image_names('../../dataset/xview/Planes/yolo_planes_test_images/')
# for n in names:
#    print(n)

################ Image Padding ########################
# print(names)
# imprep.pad_image('../sample/slice_Potsdam_ISPRS_top_potsdam_2_10_RGB_0_0_544_544_0.jpg', save=True)
# print(padded)

############# Image as Arrays #########################
# img_array = imprep.images_as_array(path)
# print(img_array.shape)

############# Yolo labels ####################################

Y = imprep.read_labels(label_path)
Yf = imprep.read_label_as_list(label_file1)
J = imprep.image_metadata(image_file,save=True)
Jf = imprep.image_folder_metadata(image_path, save=True)
Jfi = imprep.image_folder_metadata_with_id(image_path, save=True)

B = imprep.bbox_reader(label_file1)
Bl = imprep.bbox_list(label_file1)
Bc = imprep.bbox_coco(label_file1, save=False)
#
#print(J)
#print(Jf)
#print(Jfi)
#print(Bc)

CJ = imprep.image_and_label_meta(image_file,label_file1, save=True)
FM = imprep.folder_metadata(image_path, label_path)
CF = imprep.coco_format_folder(image_path, label_path)
print(FM)
print(CF)

