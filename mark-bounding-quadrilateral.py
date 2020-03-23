import numpy as np
import cv2 as cv
def markImg(imgIn,corners,col=[255,255,255],thick=2):
    img = None
    if len(imgIn.shape)==2:
        imgIn=np.reshape(imgIn,(imgIn.shape[0],imgIn.shape[1],1))
    if imgIn.shape[2]==1:
        # print("AAA")
        imgIn=np.concatenate((imgIn,imgIn,imgIn),axis=2)


    img=np.array(imgIn,dtype=np.uint8)
    print(img.shape)
    # input("Okau?")
    for i in range(4):
        cv.circle(img,center=(corners[i][0],corners[i][1]),color=col,radius=2,thickness=thick)
        cv.line(img, (corners[i][0],corners[i][1]),(corners[(i+1)%4][0],corners[(i+1)%4][1]), color=col, thickness=thick)
    return img