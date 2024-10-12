import numpy as np
from skimage.util import random_noise

def noisyImage(img, val=0.1):
    noise_img = random_noise(img, mode='s&p', amount=val)
    noisyImg = np.array(255 * noise_img, dtype='uint8')
    return noisyImg