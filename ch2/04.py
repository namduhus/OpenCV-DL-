# 프로그램 2-4를 사용자가 중간에 g를 입력하면 명암 영상을 디스플레이하고 c를 입력하면 컬러 영상을 디스플레이하도록 확장하시오
# 설정
import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW) 
# 카메라와 연결 시도 0은 카메라 장치의 인덱스를 의미한다. + 카메라가 하나인경우

color_mode = 'color'


if not cap.isOpened():
    sys.exit("카메라와 연결 실패")
    
while True:
    ret,frame=cap.read() #비디오를 구성하는 프레임 획득
    
    if not ret:
        print("프레임 획득에 실패하여 루프를 나감")
        break
        
    key=cv.waitKey(1) #1밀리초 동안 키보드 입력 기다림
    
    if key==ord('q'): #'q'키가 들어오면 루프빠져나감
        break
    elif key == ord('g'):
        color_mode = 'gray'
    elif key == ord('c'):
        color_mode = 'color'

    if color_mode == 'gray':
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('gray display', frame_gray)
    else:
        cv.imshow('display',frame)
      
cap.release()
cv.destroyAllWindows()
