import cv2
import numpy as np
def customEdgeDetection(ksize,img):

    if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
        raise ValueError("Rows and Columns must be odd",ksize)
        return
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kernel = np.full(ksize,-1)
        kernel[int(ksize[0])//2,int(ksize[0])//2] = (int(ksize[0])**2) - 1
        print(kernel)
        cv2.filter2D(img,-1,kernel,img)
        return img

def customSharpen(ksize,img):

    if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
        raise ValueError("Rows and Columns must be odd",ksize)
        return
    else:
        kernel = np.full(ksize,-1)
        kernel[int(ksize[0])//2,int(ksize[0])//2] = (int(ksize[0])**2)
        print(kernel)
        cv2.filter2D(img,-1,kernel,img)
        return img

def customBlur(ksize,img):

    if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
        raise ValueError("Rows and Columns must be odd",ksize)
        return
    else:
        kernel = np.full(ksize,1.0/int(ksize[0])**2)
        print(kernel)
        cv2.filter2D(img,-1,kernel,img)
        return img


def customAsymethric(ksize,img):
        if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
            raise ValueError("Rows and Columns must be odd",ksize)
            return
        else:
            kernel = np.zeros(ksize)
            count = 1
            for i in range(int(ksize[0])):
                temp = -int(ksize[0]) + count
                for j in range(int(ksize[0])):
                    kernel[i,j] = temp
                    temp+=1
                count+=1
            cv2.filter2D(img,-1,kernel,img)
            return img

def laplacian(img,kersize,blurKernel = (3,3)):
    img = cv2.GaussianBlur(img,blurKernel,0,0)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.Laplacian(img,cv2.CV_16S,ksize = kersize[0])
    return img

def canny(img):
    return cv2.Canny(img,150,300)


def ApplyFilter(filterType,frame,ksize = (3,3)):
    
    if filterType == 'Edge Detection':
        return customEdgeDetection(ksize,frame)
    elif filterType == 'Custom Blur':
        return customBlur(ksize,frame)
    elif filterType == 'Custom Sharpen':
        return customSharpen(ksize,frame)
    elif filterType == 'Custom Asymethric':
        return customAsymethric(ksize,frame)
    elif filterType == 'Custom Laplacian':
        return laplacian(frame,ksize)
    elif filterType == 'Canny':
        return canny(frame)
    else:
        raise ValueError('There is no filter with this name',filterType)