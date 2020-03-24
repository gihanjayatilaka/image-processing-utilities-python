import cv2 as cv
import numpy as np
import sys
import argparse


if __name__=="__main__":
	args=argparse.ArgumentParser()
	args.add_argument("--rows","-R",dest="rows",type=int)
	args.add_argument("--cols","-C",dest="cols",type=int)
	args.add_argument("--height","-H",dest="H",type=int,default=256)
	args.add_argument("--width","-W",dest="W",type=int,default=256)
	args.add_argument("--verticalOffset","-VO",dest="VO",type=int,default=20)
	args.add_argument("--horizontalOffset","-HO",dest="HO",type=int,default=20)
	args.add_argument('--images','-i', nargs='+',dest="images", required=True)
	args.add_argument('--output','-o',dest="output", required=True)

	args=args.parse_args()


	ans=np.full((args.rows*args.H + (args.rows-1)*args.VO,args.cols*args.W + (args.cols-1)*args.HO,3),255,dtype=np.uint8)

	for i in range(args.rows):
		for j in range(args.cols):
			k=i*args.cols + j
			a=i*args.H + max(0,(i)*args.VO)
			b=j*args.W + max(0,(j)*args.HO)
			img=cv.imread(args.images[k])
			ans[a:a+args.H,b:b+args.W,:]=cv.resize(img,(args.W,args.H))

	cv.imwrite(args.output,ans)
	print("END OF PROGRAM")



