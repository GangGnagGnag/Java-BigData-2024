# file : p50_mouseAuto.py
# desc : PyAutoGui로 마우스 조작하기

'''
파이썬 모듈 설치시는 명령 프로프트보다 VSCode내 터미널에서 설치를 추천
PyAutoGui 모듈 설치
> pip install pyautogui
'''

import pyautogui as auto

print(auto.size()) #현재 모니터 해상도 정보 Size(width=1920, height=1080)
print(auto.position()) # 현재 마우스의 위치

# pyautogui 마우스 설정창
# pillow 모듈이 같이 설치 되어야 색상 표시가 됨 678,51
# auto.mouseInfo()

## 마우스 이동(절대 좌표)
auto.moveTo(100,51) # (0,0) 이후 이동이 안됨
auto.moveTo(678,51,duration = 1.0) # x 축 678, y 축 51fh 1.0초 동안 이동하라
auto.moveTo(1210, 568, duration = 0.1)

## 마우스 이동(상대 좌표)
# auto.move(505, 505, duration=0.5) # 현재위치에서 x 축 500, y 축 500으로 1.5초 동안 이동하라

## 마우스 클릭
# auto.leftClick(x = 678, y = 51) # auto.moveTo가 필요 없어짐 / 해당위치로 가서 바로 마우스 왼쪽버튼 클릭
# auto.rightClick(x = 790, y = 300)
# auto.click(clicks=4, interval = 0.1, button = 'left') # 왼쪽버튼을 소스코드 에디터에서 네번 선택하면 모든 글을 전체 선택

## 마우스 드래그
auto.leftClick(s = 1422, y = 168, duration = 1.0) # 1422, 168에서 왼쪽마우스 클릭후 1초 대기했다가
auto.dragTo(x = 983, y = 550, duration = 2.0, button = 'left') 
# auto.dragRel(500, 400, duration = 1.0, button = 'left'ㄴㅇ) # 현재위치에서 500, 400으로 1초동안 그래그 하라

## 마우스 휠
auto.scroll(500) # 양수는 위로
auto.scroll(-300) # 음수는 아래로 스크롤


