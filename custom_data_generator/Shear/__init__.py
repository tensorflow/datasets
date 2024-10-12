from skimage import transform as tf
import random

randShearVal = random.uniform(0.25, 0.8)

def shearImage(img, val=0.5):
    afineImg = tf.AffineTransform(shear=val)
    shearImg = tf.warp(img, inverse_map=afineImg)
    return shearImg
