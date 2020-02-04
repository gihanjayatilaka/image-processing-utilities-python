import sys
import pywt
import os
import numpy as np
import matplotlib.pyplot as p
# print(os.listdir(os.path.dirname(pywt.__file__)))


import cv2 as cv
if __name__ == '__main__':
    print("python dwt-for-images.py read.jpg out.jpg outputPrefix")

    img=cv.imread(sys.argv[1])
    outPref=sys.argv[2].strip()


    cv.imwrite("A.jpg",img)
    p.show()

    dwt=np.ndarray((4,np.ceil(img.shape[0]/2).astype(np.int32),\
                       np.ceil(img.shape[1]/2).astype(np.int32),img.shape[2]))
    for c in range(img.shape[2]):
        coeffs = pywt.dwt2(img[:,:,c], 'haar')
        for cc in range(4):
            if cc==0:
                dwt[cc,:,:,c]=coeffs[cc]
            else:
                dwt[cc, :, :, c] = coeffs[0][cc-1]

         # newImg[:,:,c]=coeffs[0]

    print(dwt.shape)

    newImg=np.ndarray(shape=img.shape,dtype=np.uint8)
    zero=np.zeros(dwt[1,:,:,c].shape)


    cv.imwrite("{}-in.jpg".format(outPref),img)
    try:
        imgTrue=cv.imread(sys.argv[1].replace("low","high"))
        cv.imwrite("{}-ture.jpg".format(outPref), imgTrue)
    except:
        print("Couldnt find true output")

    # .fill(0)
    for c in range(img.shape[2]):
        newImg[:,:,c]=pywt.idwt2((dwt[0,:,:,c],\
                                  (dwt[1,:,:,c],dwt[2,:,:,c],dwt[3,:,:,c])),'haar')
    cv.imwrite("{}-a.jpg".format(outPref),newImg)

    for c in range(img.shape[2]):
        newImg[:,:,c]=pywt.idwt2((dwt[0,:,:,c],\
                                  (None,None,None)),'haar')
    cv.imwrite("{}-b.jpg".format(outPref),newImg)


    for c in range(img.shape[2]):
        newImg[:,:,c]=pywt.idwt2((dwt[0,:,:,c],\
                                  (dwt[0,:,:,c],dwt[0,:,:,c],dwt[0,:,:,c])),'haar')
    cv.imwrite("{}-c.jpg".format(outPref),newImg)


    for c in range(img.shape[2]):
        newImg[:,:,c]=pywt.idwt2((None,\
                                  (dwt[1,:,:,c],None,None)),'haar')
    cv.imwrite("{}-d.jpg".format(outPref),newImg)



    for c in range(img.shape[2]):
        newImg[:,:,c]=pywt.idwt2((None,\
                                  (None,dwt[2,:,:,c],None)),'haar')
    cv.imwrite("{}-e.jpg".format(outPref),newImg)


    for c in range(img.shape[2]):
        newImg[:,:,c]=pywt.idwt2((None,\
                                  (None,None,dwt[3,:,:,c])),'haar')
    cv.imwrite("{}-f.jpg".format(outPref),newImg)



    # print("Image shape",img.shape)
    # print(len(coeffs))
    # print(coeffs[0].shape)

