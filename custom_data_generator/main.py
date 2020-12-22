import os
import cv2
from skimage import io

import Blur as Blur
import Brightness as Brightness
import Flip as Flip
import Hue as Hue
import Noise as Noise
import Shear as Shear
import BlackAndWhite as BlackAndWhite

# The path to the input directory and reading the image
inputPath = "src/input/"
writePath = "src/output/"

for i in os.listdir(inputPath):
    img = cv2.imread(inputPath + f"{i}")

    ###########################
    ############ 1 ############
    # Blurred image manipulation
    blurredImg = Blur.blurImage(img)
    cv2.imwrite(writePath + f"Blurred{i}", blurredImg)

    ###########################
    ############ 2 ############
    # Brightness image manipulation
    brightImg = Brightness.brightImage(img, gamma=2.0)
    cv2.imwrite(writePath + f"Brightened{i}", brightImg)

    ###########################
    ############ 3 ############
    # Flip image manipulation
    # Images are being flipped over X, Y, and the center automatically,
    # and each of them is being saved as a new data/image in the directory
    for j in range(-1, 2):
        flipImg = Flip.flipImage(img, j)
        cv2.imwrite(writePath + f"Flipped{j}{i}", flipImg)

    ###########################
    ############ 4 ############
    #  Hue image manipulation
    hueImg = Hue.hueImage(img, val=250)
    cv2.imwrite(writePath + f"Hue{i}", hueImg)

    ###########################
    ############ 5 ############
    # Noise image manipulation
    noisyImage = Noise.noisyImage(img, val=0.1)
    cv2.imwrite(writePath + f"Noisy{i}", noisyImage)

    ###########################
    ############ 6 ############
    # Black &  White image manipulation
    blackWhiteImage = BlackAndWhite.blackWhiteImage(img)
    cv2.imwrite(writePath + f"BlackAndWhite{i}", blackWhiteImage)

    ###########################
    ############ 7 ############
    # Shear image manipulation
    img = io.imread(inputPath + f"{i}")
    imgShear = Shear.shearImage(img)
    io.imsave(writePath + f"Shear{i}", imgShear)


