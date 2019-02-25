import xml.etree.ElementTree as ET
from os import getcwd
from os import listdir
from os.path import isfile, join
import os

classes = ["cosmetics"]

def convert_annotation(filename, list_file):
    in_file = open('Cosmetics_dataset/annotations/%s.xml'%(filename))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


filelist = listdir('Cosmetics_dataset/images')
list_file = open('Cosmetics_dataset/Cosmetics_train_data.txt', 'w')
for file in filelist:
    filename = os.path.splitext(file)
    convert_annotation(filename[0], list_file)


