#!/usr/bin/env python3

import csv
import numpy as np

def getnum(x):
    a = [l for l in x if l.isdigit()]
    return "".join(a)

# Define the CSV file path
csv_file_path = 'hilly.csv'  # Replace with the actual path to your CSV file

# Define the range of room spaces
min_room_space = 450
max_room_space = 489

# Create a list to store the extracted lines
extracted_names = []


# Read and process the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        room_space = row['Room Space']
        room_number = int(getnum(room_space.split('-')[-1]))  # Extract the room number
        if min_room_space <= room_number <= max_room_space:
            extracted_names.append(row)

# Print the extracted lines
for line in extracted_names:
    print(line)


