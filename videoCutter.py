'''
    gihanjayatilaka@eng.pdn.ac.lk 2020-02-03
'''
import argparse
import cv2 as cv
import numpy as np
import sys

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--inVideoFile","--in","-i",dest="inVideoFile",type=str)
    args.add_argument("--outVideoFile","--out","-o",dest="outVideoFile",type=str)
    args.add_argument("--startFrame", "-s", dest="startFrameNo", type=int,default=0)
    args.add_argument("--noFrames", "-n", dest="noFrames", type=int,default=1000)
    args=args.parse_args()

    fileIn=cv.VideoCapture(args.inVideoFile)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    fileOut = cv.VideoWriter(args.outVideoFile, fourcc,\
                             int(fileIn.get(cv.CAP_PROP_FPS)),\
                             (int(fileIn.get(cv.CAP_PROP_FRAME_WIDTH)), int(fileIn.get(cv.CAP_PROP_FRAME_HEIGHT))))


    fIdx=0

    # while fileIn.isOpened():
    for fIdx in range(args.startFrameNo):
        ret,fr=fileIn.read()

        print("Skipping {}".format(fIdx))
        sys.stdout.write("\033[F")

    for fIdx in range(args.noFrames):
        ret,fr=fileIn.read()
        if ret:
            fileOut.write(fr)
        print("Writing {}".format(fIdx))
        sys.stdout.write("\033[F")


    fileIn.release()
    fileOut.release()

    print("Finished writing {} frames from {}[{}:] to {}".format(\
        args.noFrames,args.inVideoFile,args.startFrameNo,args.outVideoFile))
    print("End of program")
