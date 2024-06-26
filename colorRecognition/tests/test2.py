import cv2
import numpy as np
from PIL import Image

def detectPositionsOfColors(path):
    """This function takes path to image as input and returns the dictionary with all the info and the image with the outlines and markers and dimensions of the image.
    This function makes rectangular outlines around the objects of each color and draws a marker in the center of each object,
    additionaly it returns a dictionary of detected colors and their info (position of the marker; is it on the left, right or center; marker's offset from center of the image).
    detectedInfo = {"color": (centerX, centerY, positionX, positionY, XoffsetCenter, YoffsetCenter)}
    Disclaimer: this function only works for the colors red, green, blue and yellow. And its not perfect for those colors either. To add more colors you need to add their HSV color ranges to the hsvCodes dictionary."""

    hsvCodes = { # HSV color ranges for the R, G, B, Y colors
        "red": [(0, 70, 10), (19, 255, 255), (0, 0, 255)],
        "green": [(52, 90, 0), (155, 255, 255), (0, 255, 0)],
        "blue": [(160, 90, 10), (260, 255, 255), (255, 0, 0)],
        "yellow": [(26, 90, 10), (45, 255, 255), (0, 255, 255)],
    }
    detectedInfo = {} # Dictionary of detected colors and their info

    #--- Read the image, convert it to HSV, read dimensions of the image---
    detectedRect = cv2.imread(path)
    imageHeight, imageWidth, imageChannels = detectedRect.shape
    hsv_image = cv2.cvtColor(detectedRect, cv2.COLOR_BGR2HSV)

    #--- Loop through the colors ---
    for color, (lower, upper, marker_color) in hsvCodes.items():
        #--- reset variables ---
        position = ""
        XoffsetCenter = 0
        YoffsetCenter = 0

        #--- Create a mask for the color ---
        lower = np.array(lower, dtype=np.uint8) #convert lowerLimit to numpy array
        upper = np.array(upper, dtype=np.uint8) #convert upperLimit to numpy array
        mask = cv2.inRange(hsv_image, lower, upper) #create mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find contours

        #--- Loop through the contours ---
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour) #get the coordinates of the contour

            #--- Calculate the center of the contour ---
            centerX = x + w//2
            centerY = y + h//2

            #--- Calculate the offset from center of image -> X---
            if centerX < (imageWidth//2):
                positionX = "left"
                XoffsetCenter = centerX - (imageWidth//2)
            elif centerX > (imageWidth//2):
                positionX = "right"
                XoffsetCenter = centerX - (imageWidth//2)
            else:
                positionX = "center"
                XoffsetCenter = 0
            
            #--- Calculate the offset from center of image -> Y---
            if centerY < (imageHeight//2):
                positionY = "top"
                YoffsetCenter = centerY - (imageHeight//2)
            elif centerY > (imageHeight//2):
                positionY = "bottom"
                YoffsetCenter = centerY - (imageHeight//2)
            else:
                positionY = "center"
                YoffsetCenter = 0

            #--- Draw the rectangle and the marker ---
            if w > 5 and h > 5:
                cv2.rectangle(detectedRect, (x, y), (x + w, y + h), marker_color, 2) #draw rectangle
                cv2.circle(detectedRect, (centerX, centerY), 5, marker_color, -1) #draw marker
                cv2.circle(detectedRect, (centerX, centerY), 6, (0, 0, 0), 1) #draw marker outline

            #--- Add the info to the dictionary ---
            detectedInfo[color] = (centerX, centerY, positionX, positionY, XoffsetCenter, YoffsetCenter) 

    #--- Convert the final image to PIL image ---
    color_coverted = cv2.cvtColor(detectedRect, cv2.COLOR_BGR2RGB) #convert to RGB
    finalRect = Image.fromarray(color_coverted) 
        
    return detectedInfo, finalRect, (imageHeight, imageWidth)

path = r'F:\skillscomp\z3colors\YGR3.png'
info, image, dim = detectPositionsOfColors(path)
print(info, dim)
image.show()