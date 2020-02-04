import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt

print("python traverse-mp4-framebyframe.py video.mp4    0.5")
print("python traverse-mp4-framebyframe.py argv[1]      [2]")

VIDEO_FILE=sys.argv[1]
RATIO=float(sys.argv[2])
vidIn=cv2.VideoCapture(VIDEO_FILE)

frIdx=0
while vidIn.isOpened():
    ret,fr=vidIn.read()
    if not ret: break


    fr=cv2.resize(fr,dsize=(int(fr.shape[1]*RATIO),int(fr.shape[0]*RATIO)))
    print("Frame {}".format(frIdx))
    # cv2.imshow("Frame",fr)
    cv2.imwrite("fr{}.png".format(frIdx),fr)
    # plt.show()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    frIdx+=1

    if frIdx==100:
    	break
