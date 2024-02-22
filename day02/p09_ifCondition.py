#file: p09_ifCondition.py
#desc: if 제어문

haveMoney = True

if haveMoney == True:
    #indentation(들여쓰기) 기본적으로 tab (스페이스4개)
    print('미스터 택시택시택시 지금 즉시즉시즉시')
    print('빈 살만')
else:
    print('걸 어 가~~')
    print('개 백 수')
# 파이썬에서는 탭을 잘 맞춰 줘야 사용 가능하다.

money = 1000

if money >= 5000:
    #indentation(들여쓰기) 기본적으로 tab (스페이스4개)
    print('미스터 택시택시택시 지금 즉시즉시즉시')
    print('집 도착~')
elif money < 5000 and money >= 2500: # elseif 
    print('기사님..홈플까지만..')
    print('중 거지')
else:
    print('걸어 가도록')
    print('이상')
# 파이썬에서는 탭을 잘 맞춰 줘야 사용 가능하다.
