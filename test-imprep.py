import imprep

##### PC Dataset #######

img_path = '../dataset/adv_ships_test_images/'
label_path = '../dataset/adv_ships_test_labels/'
file_path = '../dataset/adv_ships_test_images/1357_8.jpg'
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
Yf = imprep.read_label_as_list(file_path)
J = imprep.image_metadata(file_path,save=True)
Jf = imprep.image_folder_metadata(img_path, save=True)
Jfi = imprep.image_folder_metadata_with_id(img_path, save=True)


print(Jfi)
