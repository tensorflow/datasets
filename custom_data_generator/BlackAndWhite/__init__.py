import cv2

def blackWhiteImage(img):
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImg) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    return blackAndWhiteImg