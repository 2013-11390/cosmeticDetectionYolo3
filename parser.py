import json

annotations = json.load(open("via_region_data.json"))
annotations = list(annotations.values())

f=open("train.txt","w")
for i, a in enumerate(annotations):
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
    if i < len(annotations) - 1:
        f.write("\n")
f.close()