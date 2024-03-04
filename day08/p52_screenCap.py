# file : p52_screenCap.py
# dsec : pyautogui 로 화면 캡쳐하기
'''
> pip install pillow
'''

import time
import pyautogui as auto

startX, endX = 0, 1919
startY, endY = 0, 1079

auto.screenshot('./day08/screen.png', region = (startX, startY, endX - startX, endY - startY))
time.sleep(2.0) # 파일저장후 너무 빨리 읽으면 문제가 생김 

capImg = auto.locateOnScreen('./day08/screen.png') # 이미지 로드
print(capImg)
auto.click(capImg)

auto.alert('문제해결!')