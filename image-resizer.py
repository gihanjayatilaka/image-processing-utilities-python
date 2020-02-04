import argparse
import os
import cv2
import numpy as np
if __name__=='__main__':
    ar=argparse.ArgumentParser()
    ar.add_argument("operation",type=str)
    ar.add_argument("inputDir",type=str)
    ar.add_argument("outputDir",type=str)
    ar.add_argument("inWidth",type=int)
    ar.add_argument("inHeight", type=int)
    ar.add_argument("outWidth", type=int)
    ar.add_argument("outHeight", type=int)
    ar.add_argument("-maxImages","-m", type=int,default=999999999999999999)


    ar=ar.parse_args()
    imgId=0


    if ar.operation in ["UP","U","u"]:
        print("Small to big")

        WW=int(ar.outWidth/ar.inWidth)
        HH=int(ar.outHeight/ar.inHeight)

        img=np.ndarray((ar.outHeight,ar.outWidth,3),dtype=np.uint8)

        y=0
        x=0
        for r, d, f in os.walk(ar.inputDir):
            for file in sorted(f):
                fileName=os.path.join(r, file)
                img2 = cv2.imread(fileName)
                print(fileName,x,y,WW,HH)
                img[y*ar.inHeight:(y+1)*ar.inHeight, (x * ar.inWidth):((x + 1) * ar.inWidth),:]=img2[:,:,:]

                x+=1

                if x==WW:
                    x=0
                    y+=1
                if y==HH:
                    y=0
                    newFileName="{}{:07d}.png".format(ar.outputDir,imgId)
                    cv2.imwrite(newFileName,img)
                    imgId+=1

                    if imgId>=ar.maxImages:
                        break
            if imgId>=ar.maxImages:
                break









    elif ar.operation in ["DOWN","D","d"]:
        print("Big to small")

        for r, d, f in os.walk(ar.inputDir):
            if imgId >= ar.maxImages: break
            for file in sorted(f):
                if imgId >= ar.maxImages: break
                fileName=os.path.join(r, file)
                img = cv2.imread(fileName)

                for y in range(int(ar.inHeight/ar.outHeight)):

                    for x in range(int(ar.inWidth/ar.outWidth)):
                        newFileName="{}{:07d}.png".format(ar.outputDir,imgId)
                        cv2.imwrite(newFileName,img[y*ar.outHeight:(y+1)*ar.outHeight, \
                                                           x * ar.outWidth:(x + 1) * ar.outWidth])
                        print(fileName,newFileName,"saved")
                        imgId+=1





