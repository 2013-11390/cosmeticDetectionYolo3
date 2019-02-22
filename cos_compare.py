def cosin_similar(img1, img2):
    similarity_param = 0.9
    a=get_color(img1)
	b=get_color(img2, convert = True)
	a1=sRGBColor(a[0],a[1],a[2])
	b1=sRGBColor(b[0],b[1],b[2])
    similarity = ((a1[0]*b1[0]) + (a1[1]*b1[1]) + (a1[2]*b1[2])) / (math.sqrt(a1[0]*a1[0] + a1[1]*a1[1] + a1[2]*a1[2]) * math.sqrt(b1[0]*b1[0] + b1[1]*b1[1] + b1[2]*b1[2]))
    print("cosin_similarity : ", similarity)

    if similarity > similarity_param:
        return True
    else :
        return False
