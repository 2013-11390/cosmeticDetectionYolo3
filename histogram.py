# import the necessary packages
from PIL import Image
import math
import numpy as np

def floor(number):
	return number-number%10

def compare_color(img1, img2):
	color1 = get_color(img1)
	color2 = get_color(img2)

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

	if (((abs(color1[0]-color2[0])<60) and (abs(color1[1]-color2[1])<255))or
		((abs(color1[0]-color2[0])<60) and (abs(color1[2]-color2[2])<255))or
		((abs(color1[1]-color2[1])<60) and (abs(color1[2]-color2[2])<255))):
		return True
	else:
		return False


# get the dominant color and show it
def get_color(image):

	# get top-1 color
	colors = image.getcolors(image.size[0] * image.size[1])
	max = 0
	max_color = (255, 255, 255)
	for (count, color) in colors:
		if count > max:
			if (abs(color[0]-color[1])>20 and
				# abs(color[1]-color[2])>20 and
				abs(color[2]-color[0])>20):
				max = count
				max_color= color

	print(max_color)
	return max_color

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