import cv2

def blurImage(img):
    blurImg = cv2.blur(img, (8, 8))
    return blurImg