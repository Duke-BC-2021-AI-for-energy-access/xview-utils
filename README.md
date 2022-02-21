## Some scripts for interfacing with the xview dataset

Based on the official dataset utilities, (https://github.com/DIUx-xView/data_utilities).

Installation:

1. Clone this repo
2. Download the xview dataset from (xviewdataset.org). Make sure to use the `.tar.gz` rather than the `.zip` format and run the checksum with MD5.
3. Extract the files and put the contents in this folder. Here is a current `ls -l` output:
```
drwxr-xr-x 4 yl708 ldapusers      4096 Feb  9 11:18 data_utilities
-rw-r--r-- 1 yl708 ldapusers      1019 Feb 14 13:04 labelct.csv
-rw-r--r-- 1 yl708 ldapusers      1362 Feb 20 14:04 make_object_distribution_csv.py
drwxr-xr-x 2 yl708 ldapusers      4096 Feb 20 14:02 object_distribution_csvs
-rw-r--r-- 1 yl708 ldapusers 892331734 Feb 20 13:28 pretty_xView_train.geojson
drwxr-xr-x 2 yl708 ldapusers      4096 Feb 20 13:36 __pycache__
-rw-r--r-- 1 yl708 ldapusers       330 Feb 21 10:05 README.md
-rw-r--r-- 1 yl708 ldapusers      5662 Feb 20 14:09 sample-object.ipynb
-rw-r--r-- 1 yl708 ldapusers      1849 Feb  9 12:42 scratch.ipynb
-rw-r--r-- 1 yl708 ldapusers     66730 Feb 14 13:00 structurecount.txt
-rw-r--r-- 1 yl708 ldapusers      3822 Feb 14 13:04 test.ipynb
drwxrwxrwx 2 yl708 ldapusers     20480 Feb 19  2018 train_images
-rw-r--r-- 1 yl708 ldapusers      3165 Feb 20 13:36 training_data_loader.py
drwxrwxrwx 2 yl708 ldapusers     12288 Feb 19  2018 val_images
-rwxrwxrwx 1 yl708 ldapusers 372241031 Feb 13  2018 xView_train.geojson
```
Usage:

`training_data_loader.py` provides an interface to the useful utilities in `data_utilities`

More to come ...
