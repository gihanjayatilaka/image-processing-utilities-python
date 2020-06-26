'''
    pip install scikit-video
    pip install scikit-image
'''

'''
python image-enhancement-metrics.py -i mercon-results/gt/ -o mercon-results/dark/
python image-enhancement-metrics.py -i mercon-results/gt/ -o mercon-results/gt/
python image-enhancement-metrics.py -i mercon-results/gt/ -o mercon-results/dcgan/
python image-enhancement-metrics.py -i mercon-results/gt/ -o mercon-results/retinex/
python image-enhancement-metrics.py -i mercon-results/gt/ -o mercon-results/our/

'''
import argparse
import numpy as np
import cv2 as cv
from skvideo.measure import *



from os import listdir
from os.path import isfile, join


if __name__ =='__main__':

    args=argparse.ArgumentParser()
    args.add_argument("--inputFolder","-i",required=True,dest="inputFolder",type=str)
    args.add_argument("--outputFolder","-o",required=True,dest="outputFolder",type=str)
    args=args.parse_args()



    inputFiles = [join(args.inputFolder,f) for f in listdir(args.inputFolder) if isfile(join(args.inputFolder,f))]
    
 

    inputImages=[]
    for f in inputFiles:
        img=cv.imread(f)
        inputImages.append(img)
    

    outputFiles = [join(args.outputFolder, f) for f in listdir(args.outputFolder) if isfile(join(args.outputFolder, f))]
    print("Output files:: ",outputFiles)

    outputImages=[]
    for f in outputFiles:
        img=cv.imread(f)
        outputImages.append(img)

    print("Finished loading {} input images and {} output images".format(len(inputImages),len(outputImages)))

    inputImages=np.array(inputImages)
    outputImages=np.array(outputImages)

    inputImages=np.mean(inputImages,axis=-1)
    inputImages=np.resize(inputImages,(inputImages.shape[0],inputImages.shape[1],inputImages.shape[2],1))
    outputImages=np.mean(outputImages,axis=-1)
    outputImages=np.resize(outputImages,(outputImages.shape[0],outputImages.shape[1],outputImages.shape[2],1))

    print("Numpy Shapes {} {} ".format(inputImages.shape,outputImages.shape))


    mseVal=np.mean(mse(inputImages,outputImages))
    psnrVal=np.mean(psnr(inputImages,outputImages))
    # ssimVal=np.mean(ssim(inputImages,outputImages))
    # a=np.mean(niqe(inputImages))
    # b=np.mean(niqe(outputImages))
    # niqeVal=a/b


    print("Results after comparing {} and {}".format(args.inputFolder,args.outputFolder))
    print("MSE\t: {}".format(mseVal))
    print("PSNR\t: {}".format(psnrVal))
    # print("SSIM\t: {}".format(ssimVal))
    # print("NIQE ratio\t: {}".format(mseVal))
    print("End of Programs")










