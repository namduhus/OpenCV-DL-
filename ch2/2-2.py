import cv2 as cv
import sys ##파이썬이 제공하는 시스템 변수를 설정하거나 exit함수로 프로그램을 종료하는데 사용한다.

img1 = cv.imread('soccer.jpg')
img2 = cv.imread('soccer_gray.jpg')

if img1 is None:
    sys.exit("파일을 찾을 수 없습니다.")

if img2 is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv.imshow('img1', img1)
cv.imshow('img2',img2)

cv.waitKey() # 키보드를 누르면 imshow가 닫힌다. default=10초 정도
cv.destroyAllWindows()
