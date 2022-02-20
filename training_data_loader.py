'''
 # @ Author: Yuxi Long
 # @ Create Time: 2022-02-09 09:32:15
 # @ Modified by: Yuxi Long
 # @ Modified time: 2022-02-09 09:36:05
 # @ Description: An interface for loading training data from the xview dataset. Currently implementation uses the json library instead of the geojson library so that we don't have to make modifications to the pt191 environment and break dependencies just for this one task.
 '''

'''
Reference data utilities from the official challenge: https://github.com/DIUx-xView/data_utilities
'''

import json
import os

import data_utilities.aug_util as aug
import data_utilities.wv_util as wv
import matplotlib.pyplot as plt
import numpy as np
import csv

class XViewTrainingDataset:
    """A dataset object for the xview training dataset. If the dataset is moved to another directory, change the variables json_filepath and image_path_prefix.
    """
    # the ability to retrieve each file with __next__
    # the ability to retrieve a list of files with ls()
    # the ability to retrieve info about a specific file with a method
    ## __next__
    json_filepath = '/scratch/public/xview-dataset/xView_train.geojson'
    image_path_prefix = '/scratch/public/xview-dataset/train_images/'
    list_images = None
    unique_list_images = None
    iter_count = 0 # for iterator object use only
    coords, classes = None, None

    def __init__(self):
        self.coords, chips, self.classes, self.gps_coordinates = wv.get_labels(self.json_filepath)
        # print('Loaded GeoJSON file')
        # self.list_images = np.array([self.image_path_prefix + image_name for image_name in np.unique(chips)])
        self.list_images = chips
        self.unique_list_images = np.unique(self.list_images)

    def __next__(self):
        """
        Returns:
            tuple of image_name, coords, classes: 
                image_name: image name, not exact path to image
                coords: list containing bbox coordinates
                classes: list containing bbox classes. See https://raw.githubusercontent.com/DIUx-xView/data_utilities/master/xview_class_labels.txt fror label names
        """
        if self.iter_count == len(self.unique_list_images):
            raise StopIteration

        image_name = self.unique_list_images[self.iter_count]
        coords, classes, gps_coordinates = self.get_label(image_name)
        self.iter_count += 1
        return image_name, coords, classes, gps_coordinates

    def __len__(self):
        return len(self.unique_list_images)
    
    def ls(self) -> list:
        """
        Returns list of image names
        """
        return self.unique_list_images

    def get_image(self, name):
        """
        returns ndarray representation of image
        """
        return wv.get_image(self.image_path_prefix + name)

    def get_label(self, name):
        coords = self.coords[self.list_images==name]
        classes = self.classes[self.list_images==name].astype(np.int64)
        gps_coordinates = self.gps_coordinates[self.list_images==name]
        return coords, classes, gps_coordinates


if __name__ == '__main__':
    xv = XViewTrainingDataset()
    print(xv.list_images)
