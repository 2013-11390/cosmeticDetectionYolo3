import json

mascara = json.load(open("via_region_data_mascara.json"))
mascara = list(mascara.values())
brush = json.load(open("via_region_data_brush.json"))
brush = list(brush.values())

f=open("train.txt","w")
for i, a in enumerate(mascara):
    f.write('images/' + a['filename'])
    f.write(" ")
    b = list(a['regions'].values())
    for j, c in enumerate(b):
        d= c['shape_attributes']
        f.write(str(d['x']))
        f.write(",")
        f.write(str(d['y']))
        f.write(",")
        f.write(str(d['x']+d['width']))
        f.write(",")
        f.write(str(d['y']+d['height']))
        f.write(",")
        f.write("0")
        if j < len(b) - 1:
            f.write(" ")
    if brush[i]['regions']:
        brush_list = list(brush[i]['regions'].values())
        for j, c in enumerate(brush_list):
            d = c['shape_attributes']
            f.write(" ")
            f.write(str(d['x']))
            f.write(",")
            f.write(str(d['y']))
            f.write(",")
            f.write(str(d['x']+d['width']))
            f.write(",")
            f.write(str(d['y']+d['height']))
            f.write(",")
            f.write("1")
            if j < len(b) - 1:
                f.write(" ")
    if i < len(mascara) - 1:
        f.write("\n")
f.close()