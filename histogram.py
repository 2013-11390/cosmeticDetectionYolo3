# import the necessary packages
from PIL import Image
import math
import numpy as np
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_conversions import convert_color

def dot(vector1, vector2, crop_param):
    for i in range(0, crop_param):
        for j in range(0, crop_param):
            vector_sum = vector1[i][j][0] * vector2[i][j][0] + vector1[i][j][1] * vector2[i][j][1] + vector2[i][j][2] * vector2[i][j][2]
    return vector_sum

def cosine_compare(vector1, vector2, crop_param): #changed
    similarity_param = 0.8
    dot_product = dot(vector1, vector2, crop_param)
    vector1_scale = math.sqrt(dot(vector1, vector1, crop_param))
    vector2_scale = math.sqrt(dot(vector2, vector2, crop_param))
    similarity = dot_product / (vector1_scale * vector2_scale)
    #print("cosin_similarity : ", similarity)

    if similarity > similarity_param:
        return True
    else :
        return False


def image_parse(crop_param, img):
    #image = Image.open(src)
    resized_image = img.resize((200,200))
    #resized_image.save(dst)
    # crop_param = 2
    vector = np.zeros((crop_param, crop_param, 3))
    crop_len = 200/crop_param
    for i in range(0, crop_param):
        for j in range(0, crop_param):
            crop_image = resized_image.crop((crop_len * i, crop_len * j, crop_len * (i+1), crop_len * (j+1)))
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
	#print("delta_e: ", delta_e)

	if delta_e < 80:
		return True
	else:
		return False

# get the dominant color and show it
def get_color(image, convert = False):

	# get top-1 color
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

if __name__ == '__main__':
	img1 = Image.open('cosmetic.jpg')
	img2 = Image.open('cosmetic_lower_half.jpg')
	compare_color(img1,img2)