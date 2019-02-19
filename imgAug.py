from os import listdir
import cv2
import numpy as np
import imgaug as ia
from imgaug import augmenters as iaa
from files import *
import random

image = cv2.imread('images/original.jpg')
outputData = ""
x1 = 67
y1 = 13
x2 = 219
y2 = 534
height, width = image.shape[:2]

for i in range(0, 30):
    functionRand = random.randrange(0, 10)
    scaleXrand = random.uniform(0.5, 1)
    scaleYrand = random.uniform(0.5, 1)
    rotateRand = random.randrange(-90, 90)
    shearRand = random.randrange(-45, 45)

    ia.seed(1)

    ia_bounding_boxes = []
    ia_bounding_boxes.append(ia.BoundingBox(x1, y1, x2, y2))
    bbs = ia.BoundingBoxesOnImage(ia_bounding_boxes, shape=image.shape)


    #rotate and size change
    chSeq = iaa.Affine(
        scale=(scaleXrand, scaleYrand),
        translate_percent={"x":(-0.2, 0.2), "y":(-0.2, 0.2)},
        rotate=(rotateRand, -1 * rotateRand),
        shear=(shearRand, -1 * shearRand)
    )

    chSeq_det = chSeq.to_deterministic()

    image_aug = chSeq_det.augment_images([image])[0]
    bbs_aug = chSeq_det.augment_bounding_boxes([bbs])[0]

    seq = iaa.Affine()
    # not rotate
    if functionRand < 2:
        seq = iaa.Superpixels(p_replace=0.5, n_segments=64)
    elif functionRand < 4:
        seq = iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0))
    elif functionRand < 6:
        seq = iaa.ContrastNormalization((0.5, 1.5), per_channel=0.5)
    elif functionRand < 8:
        seq = iaa.AddElementwise((-40, 40))

    image_aug2 = seq.augment_images([image_aug])[0]

    for j in range(len(bbs.bounding_boxes)):
        before = bbs.bounding_boxes[j]
        after = bbs_aug.bounding_boxes[j]

    if bbs_aug.bounding_boxes[0].x1 < 0 :
        bbs_aug.bounding_boxes[0].x1 = 0
    else :
        bbs_aug.bounding_boxes[0].x1 = int(bbs_aug.bounding_boxes[0].x1)
    if bbs_aug.bounding_boxes[0].y1 < 0 :
        bbs_aug.bounding_boxes[0].y1 = 0
    else :
        bbs_aug.bounding_boxes[0].y1 = int(bbs_aug.bounding_boxes[0].y1)
    if bbs_aug.bounding_boxes[0].x2 > width - 1 :
        bbs_aug.bounding_boxes[0].x2 = width - 1
    else :
        bbs_aug.bounding_boxes[0].x2 = int(bbs_aug.bounding_boxes[0].x2)
    if bbs_aug.bounding_boxes[0].y2 > height - 1 :
        bbs_aug.bounding_boxes[0].y2 = height - 1
    else :
        bbs_aug.bounding_boxes[0].y2 = int(bbs_aug.bounding_boxes[0].y2)


    image_before = bbs_aug.draw_on_image(image, thickness=20)
    image_after = bbs_aug.draw_on_image(image_aug2, thickness=20, color=[0, 0, 255])



    cv2.imwrite('images/afterAug'+str(i)+'.jpg', image_after)
    outputData = outputData + 'images/afterAug'+str(i)+'.jpg' + " " + str(bbs_aug.bounding_boxes[0].x1) + "," + str(bbs_aug.bounding_boxes[0].y1) + ","+ str(bbs_aug.bounding_boxes[0].x2) + ","+ str(bbs_aug.bounding_boxes[0].y2) + ",0\n"

f = open("train.txt", 'w')
f.write(outputData)
f.close()