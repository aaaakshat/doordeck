#!/usr/bin/env python3

from PIL import ImageFont, Image, ImageDraw
import csv

all_names = []
with open("test.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in reader:
        if line == 0:
            line += 1
            pass
        else:
            all_names.append(row[0])

for i in range(len(all_names) // 8 + 1):
    names = all_names[8*i:8*i+8]
    template = Image.open("template.png")
    draw = ImageDraw.Draw(template)


    font = ImageFont.truetype("Arial.ttf", 35)
    x,y = (100, 540)

    for name in names:
        draw.text((x,y), name.upper(), font=font, fill=(0,0,0))
        y += 685
        if (y > 2595):
            y = 540
            x = 1150

    x,y = (530, 490)
    font2 = ImageFont.truetype("Breakable.ttf", 85)
    for name in names:
        txt = Image.new("L", (280, 140), 255)
        d = ImageDraw.Draw(txt)
        d.text((0,0), name.title(),font=font2, fill=0)
        w = txt.rotate(2.1, expand=1, fillcolor=255)
        template.paste(w, (x,y))
        y += 685
        if (y > 2595):
            y = 490
            x = 1570

    title = "test/test" + str(i+1) + ".png"
    template.save(title)

