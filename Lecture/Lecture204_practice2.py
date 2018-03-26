import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('testimage.jpg')
R_img = img.copy()

black = np.array([0,0,0])
blue = np.array([0,0,255])
green = np.array([0,255,0])
red = np.array([255,0,0])
pink = np.array([255,0,255])
yellow = np.array([255,255,0])
white = np.array([255,255,255])
cyan = np.array([0,255,255])
colors = [black, blue, green, red, pink, yellow, white, cyan]
    
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pick_min = 1000
        color = white
        for pattern in colors:
            pick = img[i,j] - pattern
            pick_norm = np.linalg.norm(pick)
            if pick_norm < pick_min :
                pick_min = pick_norm
                color = pattern
        R_img[i,j,0] = color[0]
        R_img[i,j,1] = color[1]
        R_img[i,j,2] = color[2]

plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.imshow(R_img)
plt.show()
