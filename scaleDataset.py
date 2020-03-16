import numpy as np
import cv2 as cv
import argparse

if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--outDir", "-o", dest="outDir", type=str)
    args.add_argument("--imagePrefix","-ip",dest="imagePrefix",type=str)
    args.add_argument("--imageSuffix","-is", dest="imageSuffix", type=str)
    args.add_argument("--npyPrefix","-np", dest="npyPrefix", type=str)
    args.add_argument("--npySuffix","-ns", dest="npySuffix", type=str)
    args.add_argument("--start","-st", dest="start", type=int)
    args.add_argument("--end", "-en",dest="end", type=int)
    args.add_argument("--outWidth", "-ow", dest="outWidth", type=int)
    args.add_argument("--outHeight", "-oh", dest="outHeight", type=int)
    args.add_argument("--inWidth", "-iw", dest="inWidth", type=int)
    args.add_argument("--inHeight", "-ih", dest="inHeight", type=int)
    args=args.parse_args()

    # if args.imagePrefix==None: args.imagePrefix=""
    # if args.imageSuffix==None: args.imageSuffix=""
    # if args.npyPrefix==None: args.npyPrefix=""
    # if args.npySuffix==None: args.npySuffix=""
    #

    print("W",args.inWidth,"-->",args.outWidth)
    print("H",args.inHeight,"-->",args.outHeight)
    input("?")
    for i in range(args.start,args.end+1):
     try:
         img="{}{}{}".format(args.imagePrefix,i,args.imageSuffix)
         npy="{}{}{}".format(args.npyPrefix,i,args.npySuffix)
         imgg=cv.imread(img)
         npyy=np.load(npy)
         imgg=cv.resize(imgg,(args.outWidth,args.outHeight))
         # print("*",npyy)
         # npyy2=np.array(npyy)
         print("A",npyy.shape,npyy)
         # for j in range(4):
         # print("A")


         npyy[:,1]=(1.0*npyy[:,1]*args.outHeight)/(1.0*args.inHeight) #)).astype(npyy.dtype)
         npyy[:,0]=(1.0*npyy[:,0]*args.outWidth)/(1.0*args.inWidth)#).astype(npyy.dtype)

         print("Z",npyy.shape, npyy)
         # print("end",npyy)
         cv.imwrite("{}/{}".format(args.outDir,img),imgg)
         np.save("{}/{}".format(args.outDir,npy),npyy)
         print("Saved {} to {}".format(i,args.outDir))
     except:
        print("Error in {}".format(i))

    print("END OF PROGRAM")


