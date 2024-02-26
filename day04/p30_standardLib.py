# file : p30_standardLib.py
# desc : 표준 라이브러리(빌트인) 학습

import datetime
from pstats import SortKey
import time
import random

print(datetime.date(2024, 2, 26))  # 2024-02-26 # 현재의 os에 맞춰서 날짜형으로 변경

## 많이씀
curr = datetime.datetime.now() # 현재의 년 월 일 시 분 초 를 알려줌
print(curr)         # 2024-02-26 15:07:57.660414

print(curr.weekday())   # 0 // 0은 월요일~ 6은 일요일
print(curr.year)    # 2024
print(curr.month)   # 2
print(curr.day)     # 26
print(curr.hour)     # 15
print(curr.minute)     # 10
print(curr.second)     # 6\

print(f'{curr.year}년 {curr.month:02d}월 {curr.day}일 {curr.hour}시 {curr.minute}분')
# 2024년 02월 26일 15시 12분

curr2 = time.localtime()    # time으로 찾는 localtime() 잘 안쓰임
# time.struct_time(tm_year=2024, tm_mon=2, tm_mday=26, tm_hour=15, tm_min=14, tm_sec=2, tm_wday=0, tm_yday=57, tm_isdst=0)
print(curr2)

## 많이쓰임 ☆
for i in range(5):
    print(f'{i} 출력')
    time.sleep(2)    # 2초씩 잠시 멈춤

## 
print(random.random())  #0~1사이의 소수점 랜덤수
print(random.randint(1,45)) # 1, 45 사이의 랜덤수

## 로또
result = []
total = []

for i in range(5):
    while True:
        val = random.randint(1, 45)
        while val not in result:
            result.append(val)
        
        if len(result) == 6:
            break

        result.sort()
    total.append(result)
    result = []

print(total)

## 내부 라이브러리중 웹사이트
# import urllib
# 요청(request) > 응답(response)
from urllib.request import Request, urlopen

req = Request('https:// naver.com')
res = urlopen(req)

print(res.status)   # 응답코드 200
print(res.text)     # 내용가져오기

