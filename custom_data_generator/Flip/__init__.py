import cv2

def flipImage(img, rotation=0):
    flipImg = cv2.flip(img, rotation)
    return flipImg