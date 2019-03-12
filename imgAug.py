import cv2
import imgaug as ia
from imgaug import augmenters as iaa
import random

# get test data
# you can replace 'image.jpg' to your own data
image = cv2.imread('images/image.jpg')
outputData = ""
x1 = 0
y1 = 0
x2 = image.shape[1]-1
y2 = image.shape[0]-1
height, width = image.shape[:2]

for i in range(0, 100):
    functionRand = random.randrange(0, 10)
    scaleXrand = random.uniform(0.25, 1)
    scaleYrand = random.uniform(0.25, 1)
    transXrand = random.uniform(-0.3, 0.3)
    transYrand = random.uniform(-0.3, 0.3)
    rotateRand = random.randrange(-10, 10)
    shearRand = random.randrange(-5, 5)


    ia.seed(1)

    ia_bounding_boxes = []
    ia_bounding_boxes.append(ia.BoundingBox(x1, y1, x2, y2))
    bbs = ia.BoundingBoxesOnImage(ia_bounding_boxes, shape=image.shape)


    #rotate and size change
    chSeq = iaa.Affine(
        scale=(scaleXrand, scaleYrand),
        translate_percent={"x":(0, transXrand), "y":(0, transYrand)},
        rotate=(rotateRand, 0),
        shear=(shearRand, 0),
        mode="constant",
        cval=255
    )

    chSeq_det = chSeq.to_deterministic()

    image_aug = chSeq_det.augment_images([image])[0]
    bbs_aug = chSeq_det.augment_bounding_boxes([bbs])[0]

    seq = iaa.Affine()
    # not rotate
    if functionRand < 1:
    #     seq = iaa.Superpixels(p_replace=0.5, n_segments=64)
    # elif functionRand < 2:
        seq = iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0))
    elif functionRand < 3:
    #     seq = iaa.ContrastNormalization((0.5, 1.5), per_channel=0.5)
    # elif functionRand < 4:
    #     seq = iaa.AddElementwise((-40, 40))
    # elif functionRand < 5:
        seq = iaa.CoarseDropout(0.1, size_percent=0.01)
    elif functionRand < 6:
        seq = iaa.Multiply((0.5, 1.5))

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


    image_before = bbs_aug.draw_on_image(image, thickness=0)
    image_after = bbs_aug.draw_on_image(image_aug2, thickness=0, color=[0, 0, 255])


    # save augmented data
    cv2.imwrite('imagesAugWeak/afterAug'+str(i)+'.jpg', image_after)
    outputData = outputData + 'imagesAugWeak/afterAug'+str(i)+'.jpg' + " " + str(bbs_aug.bounding_boxes[0].x1) + "," + str(bbs_aug.bounding_boxes[0].y1) + ","+ str(bbs_aug.bounding_boxes[0].x2) + ","+ str(bbs_aug.bounding_boxes[0].y2) + ",39\n"

# write annotation of data to 'train.txt'
f = open("imagesAugWeak/train.txt", 'w')
f.write(outputData)
f.close()
