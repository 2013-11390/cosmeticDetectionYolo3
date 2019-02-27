# CosmeticDetectionYolo3

## Introduction

A Cosmetic detector using YOLOv3 (Tensorflow backend) for cosmetic detection (ref: [qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3))


## Test data

Test data is under 'test/'

![Cosmetic](pictures/image.jpg)

## How to use:

### 1) Get the model

Step 1: Download the project:
```
git clone https://github.com/2013-11390/cosmeticDetectionYolo3.git
```

Step 2: Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/) or [yolov3.weights](https://drive.google.com/uc?id=1owAyOwfpwxpbs0BLWPkwT0srRUTpFHIn&export=download).

Step 3: Convert the Darknet YOLO model to a Keras model 
```
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5	# to get yolo.h5(model)
```

**OR** download the model [yolo.h5](https://drive.google.com/uc?export=download&confirm=8R0l&id=1Dd-uUhhXvosXiIIZM8tiXoZyENJxIY4u) to *model_data/* directory directly.

### 2) Test the model on coco dataset(original yolo model is trained on coco dataset)
Run YOLO detecion.
```
python yolo_video.py --model_path model_data/yolo.h5 --classes_path model_data/coco_classes.txt --image
```

![Raccoon](pictures/coco_1.png)

### 3) Train the model for cosmetic detection:
Step 1: Augment test data
```
python imgAug.py
```
Step 2: Parse annotation:
```
python raccoon_annotation.py
```
Step 3: Download YOLOv3 weights from [yolo_weights](https://drive.google.com/uc?export=download&confirm=-b_7&id=1HlydiovCtnUJabQvZIbx77v6sE4OXrac) to *model_data/* directory

Step 4: Train the model(use yolo.h5 as the pretrained model) 
```
python train.py -a Raccoon_dataset/raccoon_train_data.txt -c Raccoon_dataset/raccoon_classes.txt -o model_data/raccoon_derived_model.h5
```

**OR** download the trained model [raccoon_derived_model.h5](https://drive.google.com/uc?export=download&confirm=6pCi&id=1mdSiioui7H8pskBCMrE08jo-0saIf-y-) to *model_data/* directory directly.

Step 5: Run the model
```
python yolo_video.py --image
```

## Cosmetic detection result

![Cosmetic](pictures/result1.jpg)

![Cosmetic](pictures/result2.jpg)
