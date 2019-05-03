# Image and Object Recognition

This repository is made to fulfill all the information about the project.

## Main Idea for the Project

TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications. It is the fastest and the simplest way to do image recognition on your laptop or computer without any GPU because it is just an API and your CPU is good enough for this. We will be adding our dataset into the Tensorflow and applying all the mentioned things below.


# Installation

[Link to Tensorflow](https://www.tensorflow.org/ "")

```python

from PIL import Image
import os
import argparse
 
def rescale_images(directory, size):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(directory+img)
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
    args = parser.parse_args()
    rescale_images(args.directory, args.size)
    
```

# Training Process

![Training process first steps](https://github.com/nijatmursali/MachineLearningProject/blob/master/image/Capture.JPG)
![Training process first steps](https://github.com/nijatmursali/MachineLearningProject/blob/master/image/Capture1.JPG)
![Training process first steps](https://github.com/nijatmursali/MachineLearningProject/blob/master/image/Capture2.JPG)
![Training process first steps](https://github.com/nijatmursali/MachineLearningProject/blob/master/image/Capture4.JPG)

# Outcome 

![Image for project](https://github.com/nijatmursali/MachineLearningProject/blob/master/image/test.jpg)


```python
```



# Motivation

# Methods


# Intended experiments

>

As mentioned above, Tensorflow is one of the important concepts of Machine and Deep Learning because of the job it does. Actually, there are several ways to do image and object recognition, but thanks to Google’s Tensorflow it’s way easier and more beneficial because of using sufficient CPU when it works. 

The experiments we will try to do are the following:

1. Image and object recognition using the Tensorflow API
1. Checking all the imported dataset in Azerbaijani language
1. Adding the voices when the objects are found
1. Implementing the application on mobile phones

The main question is that how we can use the Tensorflow and implement it in the way that we want. 

For the image recognition, we need to add all the required images for our dataset that will be CSV mostly (we will add all the images and their labelled classification into the dataset). Tensorflow will try to find out what the image is and to which class it belongs. For the videos, we will be using OpenCV which is open source and used for real-time object recognition. In our final report we will be explaining OpenCV more. 

As mentioned above, the voice will also be added to the application for saying the exact object in the scene. Mostly, we will be using the mobile phone cameras for our real-time showcase for the project. 
