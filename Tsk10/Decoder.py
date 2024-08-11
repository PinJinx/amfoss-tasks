import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math


l_coords = []
l_color = []
last_pos = (0,0)
for i in range(1,98):
    path = os.path.realpath(os.curdir)
    path += "/assets/Layer "+str(i)+".png"
    if os.path.exists(path) == True:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(path)
        params = cv2.SimpleBlobDetector_Params()
        params.filterByArea = True
        params.minArea = .5
        params.filterByColor = 205
        params.blobColor = 0
        detector = cv2.SimpleBlobDetector_create(params)
        k = detector.detect(img)
        for cv2.KeyPoint in k:
            x = k[0].pt[0]
            y = k[0].pt[1]
            b,g,r = (img2[math.floor(x),math.floor(y)])
            l_coords.append((math.floor(x),math.floor(y)))
            l_color.append((r,g,b))
            last_pos = (math.floor(x),math.floor(y))
        
        x_coords = []
        y_coords = []
        if len(k) == 0:
            for x in range(512):
                for y in range(512):
                    if img[x,y] != 255:
                        x_coords.append(y)
                        y_coords.append(x)
            if x_coords != []:
                center =  (math.floor((min(x_coords)+max(x_coords))/2),math.floor((min(y_coords)+max(y_coords))/2))
                l_coords.append(center)
                b,g,r = (img2[center[1],center[0]])
                last_pos = center
                l_color.append((r,g,b))
            else:
                l_coords.append((0,0))
                l_color.append(l_color[-1])
print(len(l_color))
image = Image.new("RGB", (512,512)) 
for i in range(0,len(l_coords)-1):
    draw = ImageDraw.Draw(image)
    if(l_coords[i] != (0,0) and l_coords[i+1] != (0,0)):
        coord = [l_coords[i],l_coords[i+1]]
        draw.line(coord,width = 10,fill=l_color[i])
image.save(os.path.realpath(os.curdir)+"/output Image.png")