from urllib.request import urlretrieve
import os
import numpy as np
import tensorflow as tf
import skimage.io
import skimage.transform
import matplotlib.pyplot as plt
t = np.load('./vgg16.npy',encoding='latin1')
doc = open('1.txt','a')
print(t,file=doc)
