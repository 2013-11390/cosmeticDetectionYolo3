# import the necessary packages
from PIL import Image
import math
import numpy as np
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_diff import delta_e_cie1976
from colormath.color_conversions import convert_color

def floor(number):
	return number-number%10

def compare_color(img1, img2):
	histo_param = 60
	a=get_color(img1)
	b=get_color(img2, convert = True)
	a1=sRGBColor(a[0],a[1],a[2])
	b1=sRGBColor(b[0],b[1],b[2])
	color1 = convert_color(a1, LabColor)
	color2 = convert_color(b1, LabColor)
	delta_e = delta_e_cie1976(color1, color2)
	print("delta_e: ", delta_e)

	# temp1 = []
	# temp2 = []
	# for i in range(0, 3):
	# 	if (floor(color1[i]) == 0):
	# 		temp1.append(1)
	# 	else:
	# 		temp1.append(floor(color1[i]))
	# 	if (floor(color2[i]) == 0):
	# 		temp2.append(1)
	# 	else:
	# 		temp2.append(floor(color2[i]))
	# print(temp1, temp2)
	#
	# if (temp1[0]/temp2[0] == temp1[1]/temp2[1] and temp1[1]/temp2[1] == temp1[2]/temp2[2]):
	# 	return True
	# else:
	# 	return False

	if delta_e < 3000:
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
		if (abs(color[0]-color[1])>20 and
			# abs(color[1]-color[2])>20 and
			abs(color[2]-color[0])>20):
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
	c[0] = c[0] // i
	c[1] = c[1] // i
	c[2] = c[2] // i
	c=tuple(c)

	print('avg_color: ', c)
	return c

	'''
	# get top-3 colors
	colors = image.getcolors(image.size[0]*image.size[1])
	max1 = 0
	max2 = 0
	max3 = 0
	max_color1 = None
	max_color2 = None
	max_color3 = None
	for (count, color) in colors:
		if count>max1:
			if (abs(color[0]-color[1])>20 and 
				abs(color[1]-color[2])>20 and 
				abs(color[2]-color[0])>20):
				max3 = max2
				max2 = max1
				max1 = count
				max_color3 = max_color2
				max_color2 = max_color1
				max_color1 = color
		elif count>max2:
			if (abs(color[0]-color[1])>20 and 
				abs(color[1]-color[2])>20 and 
				abs(color[2]-color[0])>20):
				max3 = max2
				max2 = count
				max_color3 = max_color2
				max_color2 = color
		elif count > max3:
			if (abs(color[0]-color[1])>20 and 
				abs(color[1]-color[2])>20 and 
				abs(color[2]-color[0])>20):
				max3 = count
				max_color3 = color
	print(max_color1, max_color2, max_color3)
	return max_color1
	'''