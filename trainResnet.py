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


cnn = ResNet50()

cnn.prepare_train_data(get_image_from='directory', data_path='cosmetic_dataset')

cnn.train(epochs = 300, batch_size = 16)

cnn.save(model_path = 'Image_Classification.h5')
