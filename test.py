import tensorflow_datasets as tfds
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
from PIL import Image
import imageio

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


#img1 = plt.imread('./tensorflow_datasets/testing/test_data/fake_examples/spine_web/test_images/test_1.jpg')
#
# img2 = plt.imread('./tensorflow_datasets/testing/test_data/fake_examples/spine_web/training_images/train_1.jpg')
#
# print(img1.shape)
# print(img2.shape)
#
# gray1 = rgb2gray(img1)
# plt.imshow(gray1)
# print(gray1.shape)
# plt.show()

#im1 = Image.fromarray(gray1)
#im1.save('./tensorflow_datasets/testing/test_data/fake_examples/spine_web/test_images/test1.jpg')

#plt.imsave('./tensorflow_datasets/testing/test_data/fake_examples/spine_web/test_images/test1.jpg', gray1)

# gray2 = rgb2gray(img2)
# plt.imshow(gray2)
# print(gray2.shape)
# plt.show()

#im2 = Image.fromarray(gray2)
#im2.save('./tensorflow_datasets/testing/test_data/fake_examples/spine_web/training_images/train1.jpg')

#plt.imsave('./tensorflow_datasets/testing/test_data/fake_examples/spine_web/training_images/train1.jpg', gray2)

# img = imageio.imread('./tensorflow_datasets/testing/test_data/fake_examples/spine_web/training_images/train1.jpg', as_gray=True, pilmode='L')
img = imageio.imread('./../../test/ZIP.test2.zip/test1 A A A.jpg', as_gray=True, pilmode='L')

img = img.astype(np.uint8)
img = img[..., None]
print(img.shape)
print(img)


# dataset = tfds.load('spine_web', split=tfds.Split.TRAIN)
#
# for x in dataset: break
# img = x['image']
# print(img.shape)
