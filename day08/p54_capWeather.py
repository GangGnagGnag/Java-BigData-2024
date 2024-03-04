# file : p54_capWeather.py
# desc : 네이버 날씨 화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울','강원','대전','대구','부산']
 # auto.mouseInfo() # 389,213
for region in regions:
    auto.moveTo(389,213,duration=0.5)
    auto.leftClick()
    for _ in range(5):
        auto.press('backspace')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl','v') #붙여넣기
    time.sleep(0.2)

    auto.press('\n') # enter랑 같은의미
    time.sleep(1.0)

    #33.273
    #695.904

    startX, startY = 33, 273
    endX, endY = 695, 904
    
    # auto.screenshot() 만 사용하면 macos에서 동작안함

    im = auto.screenshot(region=(startX, startY, endX-startX, endY-startY) )
    im.save(f'./day08/{region}.png')
    

print('저장완료')
