### ImagePrep

ImagePrep is a collection of utility functions supporting some of the most
commonly used data formats for object detection models. It enables users to
read and organize datasets in data formats required by the models. 

Currently, the program supports image processing for YOLO and COCO based formats.
 

##### Installation

    git clone https://github.com/adbeda/imageprep
    
    cd imageprep && pip install -e .



##### Usage

   Get image names
   ```python
from imageprep import utils
  
  
# folder containing images
image_path = "path/to/image/directory/"

# run task
list_of_names = utils.image_names(image_path)

print(list_of_names)

```
Output:
```python
['145_28.jpg', '79_38.jpg', '79_45.jpg', '80_7.jpg']
```   
      
   Get image names 
   ```python
from imageprep import coco

# folder containing images
image_path = "path/to/image/directory/"
label_path = "path/to/label/directory/"

# run task
coco_dict = coco.coco_format_folder(image_path, label_path)

print(coco_dict)
``` 
Output:
     
   ```json
[
  {
      "image":[{
            "file_name":"data/145_28.jpg",
            "height":416,
            "width":416
         }],
      "annotations":[{
            "bbox":[336, 398, 416, 416],
            "id":1,
            "segmentation":[],
            "area":1440,
            "category_id":0
         },
         {
            "bbox":[3, 91, 105, 163],
            "id":2,
            "segmentation":[],
            "area":7344,
            "category_id":0
         },
         {
            "bbox":[134, 31, 196, 95],
            "id":3,
            "segmentation":[],
            "area":3968,
            "category_id":0
         }
      ],
      "image_id":0
   },
   {
      "image":[{
            "file_name":"data/79_38.jpg",
            "height":416,
            "width":416
         }],
      "annotations":[{
            "bbox":[257, 306, 325, 370],
            "id":1,
            "segmentation":[],
            "area":4352,
            "category_id":0
         }],
      "image_id":1},
   {
      "image":[{
            "file_name":"data/79_45.jpg",
            "height":416,
            "width":416
         }],
      "annotations":[{
            "bbox":[0, 399, 133, 416],
            "id":1,
            "segmentation":[],
            "area":2261,
            "category_id":0
         },
         {
            "bbox":[161, 255, 239, 343],
            "id":2,
            "segmentation":[],
            "area":6864,
            "category_id":0
         },
         {
            "bbox":[336, 32, 416, 108],
            "id":3,
            "segmentation":[],
            "area":6080,
            "category_id":0
         }],
      "image_id":2},
   {
      "image":[{
            "file_name":"data/80_7.jpg",
            "height":416,
            "width":416
         }],
      "annotations":[{
            "bbox":[267, 223, 391, 319],
            "id":1,
            "segmentation":[],
            "area":11904,
            "category_id":0
         }],
      "image_id":3
      }
   ]
```
    

##### Toy Dataset:

If you're interested, a [toy dataset](https://drive.google.com/file/d/1Suh0nw0IQUFpuFFiygkO1joUK4hXQSSV/view?usp=sharing)
used for prototyping the functions is available for download.
