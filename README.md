# Synthetic computer vision data creator

## Is collecting data for your project a pain? Use this helpful script to make a nice training set from a few simple images!
Using a few background pictures as well as images of the object we can combine those together in random orientations to not only create training images but also annotations! That's right xml generation is part of the process so efficiency+=9999 !

## Why make this project?
Current projects have left me in positions where data collection is a very difficult, time consuming, multi person effort that often takes hours out in the cold. To spare myself and team from bearing more winter than we need this program was born.

## Requirements: 
- PIL
- resizeimage
- fileinput
- random
- glob
- time
- shutil


## How to use:

If your data is not yet a uniform size, I would recommend modifying this code to your desired size and running:
```
python3 image_resize_pad.py
```

Once your data is ready, run:
```
python3 create_train_data.py
```


## What each py file does:
- create_train_data.py 	: Combines our background and object images randomly to create synthetic images for training or testing
- create_xml.py		: Called by our create_train_data.py program to make XML annotations for our new data
- image_resize_pad.py	: Resizes and makes our data uniform, not necessary unless your data is not already prepared

## Build status:
Current milestones:
- [X] Working with multiple background images and varying object sizes
- [X] Working to auto annotate XML for each image it makes ( verified through labelImg )
- [] Working with custom object images ( havent started yet ) 
