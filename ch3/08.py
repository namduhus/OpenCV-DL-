import numpy as np
import time
import cv2 as cv

def myEqualizeHist(image):
    # 이미지를 그레이스케일로 변환
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # 이미지 히스토그램 계산
    hist, bins = np.histogram(gray_image.flatten(), 256, range=(0, 256))
    
    # 누적 분포 함수 계산
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # 원본 이미지에 대한 누적 분포 함수의 역함수 계산
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    
    # 히스토그램 평활화 적용
    equalized_image = cdf[gray_image]
    
    return equalized_image
  
# my function
img = cv.imread('이미지 경로')
if img is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
else:
    start = time.time()
    myEqualized = myEqualizeHist(img)
    print("MyEqual time: ", time.time() - start)

# OpenCV function
img2 = cv.imread('이미지 경로', cv.IMREAD_GRAYSCALE)
if img2 is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
else:
    start = time.time()
    cv.equalizeHist(img2)
    print("OpenCV time:", time.time() - start)


# 결과
# MyEqual time:  0.04454755783081055
# OpenCV time: 0.0009865760803222656
