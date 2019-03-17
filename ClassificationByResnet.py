"""First, copy and paste this file to the place where you want to save the image data.

Then download Caltech101 dataset from the url below.
https://github.com/mkh48v/CALTECH101

After downloading the zip file, extract it to the current directory.

Finally, you can get a filetree like below.

CALTECH101-master/
    Faces/
    Faces_easy/
    Leopards/
    ...
trainResnet.py

Now go to the place where you put this file and data and simply run the command below.

python trainResnet.py
"""
from omnis.application.image_processing.image_classification.resnet50 import ResNet50

cnn = ResNet50(model_path='Image_Classification.h5')

prediction_result = cnn.predict(data_path = 'testImage.jpg')

print('predict labels')
print(prediction_result)
