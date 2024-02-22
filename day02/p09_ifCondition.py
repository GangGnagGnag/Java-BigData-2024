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

a, b, c, d = 10, 5, 7, 9

print(a >= b)
print(c > d)

print(a >= b and c > d) #False 1 and ==1 / 1 and 0 ==0 / 0 and 1 == 0 / 0 and 0 == 0
print(a >= b or c > d) #True 1 or 1 == 1 / 1 or 0 == 1 / 0 or 1 == 0 / 0 or 0 == 0
## and 80%, or 20% 정도 사용

print(not(a >= b))   #False

##print() end 옵션(상당히 많이 사용), sep옵션

print(1 in [1,3,5,7,9], end =',') #True # 프린트를 연결해서 쓰고 싶으면 end 사용
print(6 in [1,3,5,7,9]) #False

print('13579','246810', sep ='.') #13579.246810  # sep ='.' 을 붙이면 두 수가 붙어서 나옴


# 삼항 if 문
# 파이썬에선 조건 연산자를 잘 안씀
score = 60
print('succese' if score >= 60 else 'falure')





