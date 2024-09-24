# 프로그램 2-3을 0.1 ~ 1.0으로 축소한 영상 10개를 서로 다른 윈도우에 디스플레이하도록 확장하시오
# 나는 0.4 까지만 했지만 1.0까지 반복해도 되고 복붙으로 늘려도 된다.
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR 컬러 영상을 명암  영상으로 변환
gray_small1=cv.resize(gray,dsize=(0,0), fx=0.1, fy=0.1)
gray_small2=cv.resize(gray,dsize=(0,0), fx=0.2, fy=0.2)
gray_small3=cv.resize(gray,dsize=(0,0), fx=0.3, fy=0.3)
gray_small4=cv.resize(gray,dsize=(0,0), fx=0.4, fy=0.4)

cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small1.jpg',gray_small1) #영상을 저장
cv.imwrite('soccer_gray_small2.jpg',gray_small2) #영상을 저장
cv.imwrite('soccer_gray_small3.jpg',gray_small3) #영상을 저장
cv.imwrite('soccer_gray_small4.jpg',gray_small4) #영상을 저장

cv.imshow('Color image', img)
cv.imshow('Gray Color', gray)
cv.imshow('Gray_small1', gray_small1)
cv.imshow('Gray_small2', gray_small2)
cv.imshow('Gray_small3', gray_small3)
cv.imshow('Gray_small4', gray_small4)

cv.waitKey()
cv.destroyAllWindows()
