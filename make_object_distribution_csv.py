'''
A script that outputs distribution of a specific object in the xview dataset under object_distribution_csvs/{OBJECT_NAME}.csv

'''

################ USER INPUT ##################
# see https://github.com/DIUx-xView/data_utilities/blob/master/xview_class_labels.txt for label number
LABEL=15
##############################################

import csv
import numpy as np
from training_data_loader import XViewTrainingDataset
import os

#Load the class number -> class string label map
labels = {}
with open('data_utilities/xview_class_labels.txt') as f:
    for row in csv.reader(f):
        labels[int(row[0].split(":")[0])] = row[0].split(":")[1]

print(f'Making coordinate distribution csv for {labels[LABEL]} under object_distribution_csvs')

xv = XViewTrainingDataset()
coordinate_list = []

os.system('mkdir -p object_distribution_csvs')
with open(f'object_distribution_csvs/{labels[LABEL]}.csv', 'w') as f:
    for i in range(len(xv)):
        _i, _c, classes, gps_coordinates = next(xv)
        target_class = np.full_like(classes, LABEL)
        target_coordinates = gps_coordinates[classes==target_class]
        
        coordinate_list.extend(target_coordinates)
    
    # f.write(coordinate_list)
    output_content=""
    for gps_coord in coordinate_list:
        output_content+=f'{gps_coord[0]},{gps_coord[1]}\n'

    f.write(output_content)

