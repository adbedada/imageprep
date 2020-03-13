### ImagePrep

ImagePrep is collection of basic utility functions that can help prepare a dataset for an 
Object Detection task. 

Certain DL/ML libraries require a dataset to be organized in a structure or format that 
fits into their workflow (e.g, COCO, YOLO, VOC formats). With ImagePrep, you can easily 
prepare images and labels according to these data format requirements. Currently, 
the tool simplifies the workaround COCO and YOLO style data preparation needs. 


Why ImagePrep? 
- To refer and customize the functions now that they are in one place
- And, in the long run, to make data preparation processes easier
 

##### Installation
    
    # clone repo
    git clone https://github.com/adbeda/imageprep
    
    # install
    cd imageprep && pip install -e .



##### Usage

   Basic example 1: Get image names
   ```python
from imageprep import utils
  
"""
data
├── images
    ├── 145_28.jpg
    ├── 79_38.jpg
    ├── 79_45.jpg
    └── 80_7.jpg

"""
# folder containing images
image_path = "data/images/"

# run task
list_of_names = utils.image_names(image_path)

print(list_of_names)

```
Output:
```python

['145_28.jpg', '79_38.jpg', '79_45.jpg', '80_7.jpg']

```   
      
Basic example 2: organize images and labels in COCO style  
   ```python
from imageprep import coco

"""
Folder Structure of moc dataset

data
├── images
│   ├── 145_28.jpg
│   ├── 79_38.jpg
│   ├── 79_45.jpg
│   └── 80_7.jpg
└── labels
    ├── 145_28.txt
    ├── 79_38.txt
    ├── 79_45.txt
    └── 80_7.txt
"""

# folder containing images
image_path = "data/images/"
label_path = "data/labels/"

# run task
coco_dict = coco.coco_format_folder(image_path, label_path)

print(coco_dict)
``` 
Output:
     
   ```json
[ {
      "image":[{
            "file_name":"data/images/145_28.jpg",
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
            "file_name":"data/images/79_38.jpg",
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
      "image_id":1}
   
   ]
```

#### Command Line

```commandline
imageprep -h

Usage: imageprep [OPTIONS] COMMAND [ARGS]...

  Dataset Preparation Helper

Options:
  -h, --help  Show this message and exit.

Commands:
  create-path-file  Writes out the path to images in a folder as a list
  get-image-name    Prints out the names of images in a folder
  resize-images     Resizes Image dimension to a size provided by user

```

#### 

The CLI is still in early stage of development.

##### Use case:

The above output can easily be integrated with data registration steps 
requried to train a Mask-RCNN model using [Detectron2](https://github.com/facebookresearch/detectron2). 
Check out the example [here](./examples/Imprep_and_Detectron2.ipynb). 

##### Other functionalities included in the library:
- Create list of all bounding boxes
- Stack images as numpy array
- Convert Anchors to and from YOLO
- Dump outputs to JSON file
- Resize images within a single or multiple folders 
 
 ...

##### Current and future work
 - Improve the CLI
 - Add workflow for VOC style
 - Clean up (!!!)
 - Test against RCNN families
 - Improve utils for Detectron2
  

