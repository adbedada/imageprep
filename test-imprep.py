import imprep

img_path = '../../dataset/xview/Planes/yolo_planes_test_images/'
label_path = '../../dataset/xview/Planes/yolo_planes_test_labels/'
file_path = '../../dataset/xview/Planes/yolo_planes_test_labels/79_45.txt'
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
c = imprep.create_id(label_path)
J = imprep.coco_json(label_path,'data.json')
#print(J)
