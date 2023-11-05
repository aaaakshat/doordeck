#!/usr/bin/env python3

from PIL import ImageFont, Image, ImageDraw
import csv

def getnum(x):
    a = [l for l in x if l.isdigit()]
    return "".join(a)

# Define the CSV file path
csv_file_path = 'hilly.csv'  # Replace with the actual path to your CSV file

# Define the range of room spaces
min_room_space = 450
max_room_space = 489
all_names = []


# Read and process the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        room_space = row['Room Space']
        room_number = int(getnum(room_space.split('-')[-1]))  # Extract the room number
        if min_room_space <= room_number <= max_room_space:
            name_preferred = row['Name Preferred']
            first_name = row['First Name']
            if name_preferred:
                all_names.append(name_preferred)
            else:
                all_names.append(first_name)

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
"""
    x,y = (530, 490)
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


"""


