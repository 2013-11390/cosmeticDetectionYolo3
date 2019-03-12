# import the necessary packages
from PIL import Image
import math
import numpy as np
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_conversions import convert_color
import cv2
from skimage.color import rgb2lab

similarity_param = 0.75
delta_e_param = 32
intersection_param = 0.25

def dot(vector1, vector2, crop_param):
    vector_sum = 0
    for i in range(0, crop_param):
        for j in range(0, crop_param):
            vector_sum += vector1[i][j][0] * vector2[i][j][0] + vector1[i][j][1] * vector2[i][j][1] + vector2[i][j][2] * vector2[i][j][2]
    return vector_sum

def cosine_compare(vector1, vector2, crop_param): #changed
    # similarity_param = 0.70
    dot_product = dot(vector1, vector2, crop_param)
    vector1_scale = math.sqrt(dot(vector1, vector1, crop_param))
    vector2_scale = math.sqrt(dot(vector2, vector2, crop_param))
    similarity = dot_product / (vector1_scale * vector2_scale)
    print("cosin_similarity:", similarity)

    if similarity > similarity_param:
        return True
    else :
        return False


def image_parse(crop_param, img):
    #image = Image.open(src)
    #resized_image = img.resize((200,200))
    #resized_image.save(dst)
    # crop_param = 2
    vector = np.zeros((crop_param, crop_param, 3))
    crop_h = img.size[0] / crop_param
    crop_w = img.size[1] / crop_param
    for i in range(0, crop_param):
        for j in range(0, crop_param):
            crop_image = img.crop((crop_h * i, crop_w * j, crop_h * (i+1), crop_w * (j+1)))
            #crop_image.save(str(i)+str(j)+'test.jpg')
            rgb_crop_image = get_color(crop_image)
            vector[i][j][0] = rgb_crop_image[0]
            vector[i][j][1] = rgb_crop_image[1]
            vector[i][j][2] = rgb_crop_image[2]
    return vector

def compare_color(img1, img2):
    a=get_color(img1)
    b=get_color(img2, convert = True)
    a1=sRGBColor(a[0],a[1],a[2])
    b1=sRGBColor(b[0],b[1],b[2])
    color1 = convert_color(a1, LabColor)
    color2 = convert_color(b1, LabColor)
    delta_e = delta_e_cie2000(color1, color2)
    print("delta_e:", delta_e)

    if delta_e < delta_e_param:
        return True
    else:
        return False

# get the average color and show it
def get_color(image, convert = False):

    # get average color
    colors = image.getcolors(image.size[0] * image.size[1])
    i = 0
    c = [0,0,0]
    for (count, color) in colors:
        if True:
            i = i + count
            for a in range(count):
                if convert:
                    c[2] += color[0]
                    c[1] += color[1]
                    c[0] += color[2]
                else:
                    c[0] += color[0]
                    c[1] += color[1]
                    c[2] += color[2]
    if i == 0:
        return (0,0,0)
    else:
        c[0] = c[0] // i
        c[1] = c[1] // i
        c[2] = c[2] // i
    c=tuple(c)

    #print('avg_color: ', c)
    return c

# histogram intersection
def histogram_intersection(img1, img2):
    intersection = [0, 0, 0]
    resized_img1 = img1.resize((256, 256))
    resized_img2 = img2.resize((256, 256))
    lab_img1 = cv2.cvtColor(np.array(resized_img1), cv2.COLOR_RGB2LAB)
    lab_img2 = cv2.cvtColor(np.array(resized_img2), cv2.COLOR_BGR2LAB)

    hist1 = cv2.calcHist([lab_img1], [0], None, [100], [0,100])
    hist2 = cv2.calcHist([lab_img2], [0], None, [100], [0,100])
    for i in range(0, 100):
        intersection[0] += min(hist1[i], hist2[i])

    hist1 = cv2.calcHist([lab_img1], [1], None, [256], [-128, 128])
    hist2 = cv2.calcHist([lab_img2], [1], None, [256], [-128, 128])
    for i in range(0, 256):
        intersection[1] += min(hist1[i], hist2[i])

    hist1 = cv2.calcHist([lab_img1], [2], None, [256], [-128, 128])
    hist2 = cv2.calcHist([lab_img2], [2], None, [256], [-128, 128])
    for i in range(0, 256):
        intersection[2] += min(hist1[i], hist2[i])

    average_intersection = (intersection[0]+intersection[1]+intersection[2])/(3*256*256)
    print("average_intersection:", average_intersection)
    if average_intersection > intersection_param:
        return True
    else:
        return False

if __name__ == '__main__':
    img1 = Image.open('cosmetic.jpg')
    img2 = Image.open('cosmetic_lower_half.jpg')
    compare_color(img1,img2)
