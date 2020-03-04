import imprep

#list_path_to_files('../sample', 'sample.txt')

names = imprep.image_names('../sample')
#print(names)
imprep.pad_image('../sample/slice_Potsdam_ISPRS_top_potsdam_2_10_RGB_0_0_544_544_0.jpg', save=True)

#print(padded)