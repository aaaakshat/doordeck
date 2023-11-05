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

for i in range(len(all_names) // 6 + 1):
	names = all_names[6*i:6*i+6]
	template = Image.open("template.png")
	draw = ImageDraw.Draw(template)

	font = ImageFont.truetype("COOPBL.ttf", 95)
	x, y = (410, 350)

	for name in names:
		temp = Image.new('L', (600, 100))
		tempdraw = ImageDraw.Draw(temp)
		tempdraw.text((300, 50), name.upper(), font=font, fill=255, anchor="mm")
		w = temp.rotate(5, expand=1)  # Rotate by 10 degrees

		template.paste(w, (x, y), w)
		y += 680
		if (y > 1800):
			y = 350
			x = 1750

	title = "test/test" + str(i+1) + ".png"
	template.save(title)



