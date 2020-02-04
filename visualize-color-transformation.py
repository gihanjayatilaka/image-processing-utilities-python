import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
import cv2 as cv

colorStrToInt = {"B":0,"G":1,"R":2}
colorIntToStr = ["B","G","R"]
bit8Range = np.array(range(256))

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("beforeImage", type=str)
    parser.add_argument("afterImage", type=str)
    parser.add_argument("-color","-c", type=str)
    parser.add_argument("-type", "-t", type=str,default="COLOR")
    parser.add_argument("-colspace", "-cs", type=str, default="RGB")

    ar = parser.parse_args()

    img11=cv.imread(ar.beforeImage)
    img22=cv.imread(ar.afterImage)

    if ar.colspace in ["HSV","hsv"]:
        img11 = cv.cvtColor(img11, cv.COLOR_BGR2HSV)
        img22 = cv.cvtColor(img22, cv.COLOR_BGR2HSV)
        colorStrToInt = {"H": 0, "S": 1, "V": 2}
        colorIntToStr = ["H", "S", "V"]

    img1 = np.reshape(img11, (-1, 3))
    img2 = np.reshape(img22, (-1, 3))



    if ar.type in ["COLOR","C","c"]:
        print("Color transform")

        fig, axes = plt.subplots(1, 4)
        fig.suptitle("Colour transform")

        for c in range(3):

            rImg1 = img1[:, c]
            rImg2 = img2[:, c]

            inToOut=[[] for _ in range(256)]

            for i in range(rImg1.shape[0]):
                inToOut[rImg1[i]].append(rImg2[i])


            intOutMean = np.zeros(256,dtype=np.float32)
            intOutStd = np.zeros(256, dtype=np.float32)


            for x in range(256):
                inToOut[x]=np.array(inToOut[x][:])
                intOutMean[x]=np.mean(inToOut[x])
                intOutStd[x]=np.std(inToOut[x])

                if np.isnan(intOutMean[x]):
                    intOutMean[x]=0
                if np.isnan(intOutStd[x]):
                    intOutStd[x]=0

            # print(inToOut)
            # print(intOutMean)
            # print(intOutStd)


            for i in range(256):
                if intOutMean[i]==0:intOutMean[i]=np.nan
                if intOutStd[i]==0:intOutStd[i]=np.nan

        
            axes[c].plot(bit8Range,intOutMean,bit8Range,intOutMean+intOutStd,bit8Range,intOutMean-intOutStd,bit8Range,bit8Range)
            axes[c].set_title(colorIntToStr[c])
            axes[c].legend(["Mean","Mean+std","Mean-std","No transform"])
            axes[c].set_xlabel("Before image color")
            if c==0:axes[c].set_ylabel("After image color")

        axes[3].imshow(np.concatenate((img11,img22),axis=0))
        axes[3].set_title("Before and After")

        plt.show()

    elif ar.type in ["DISTRIBUTION","D","d"]:
        rImg1 = img1
        rImg2 = img2
        print("Distribution diff")

        pmf1=np.zeros((3,256),dtype=np.int32)
        pmf2 = np.zeros((3, 256), dtype=np.int32)

        fig, axes = plt.subplots(1, 4)
        fig.suptitle("Colour distributions")

        for c in range(rImg1.shape[1]):
            for x in range(rImg1.shape[0]):
                pmf1[c , rImg1[x, c]]+=1
                pmf2[c , rImg2[x, c]] += 1


            # axes[c].hist(np.reshape(pmf1[0,:],(-1,1)), bins=255, log=True)
            axes[c].plot(bit8Range,pmf1[c, :],bit8Range,pmf2[c, :])
            axes[c].set_title(colorIntToStr[c])
            axes[c].legend(["Before image","After image"])
            axes[c].set_xlabel("color")
            if c == 0:axes[c].set_ylabel("Pixel count")

        axes[3].imshow(np.concatenate((img11,img22),axis=0))
        axes[3].set_title("Before and After")

        plt.show()






