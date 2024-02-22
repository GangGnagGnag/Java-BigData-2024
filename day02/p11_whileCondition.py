#file : p11_whileCondition.py
# desc : while 반복문

hit = 0

while hit < 20:     # True 인 동안 계속, False 가 되는 순간 while 문을 빠져나감
    hit += 1
    if hit % 3 == 0:
        # print('sui!!!!!!!!!')
        continue # 반복문의 아래로 내려가지말고 다시 반복문 위로 올라가라
    else:
        print(f'나무를{hit:02d}번 찍었습니다')
    if hit == 10:
        print('나무가 넘어갑니다')
        break # 조건에 상관없이 반복문을 탈출한다.

## 무한루프
# hit = 0
# while True:
#     hit += 1
#     print(f"나무를{hit:02d}번 찍습니다")
import os

while True:
    os.system('cls')
    select = input('메뉴입력 1.입력, 2.수정, 3.검색, 4. 삭제, 5.종료 > ')

    if select == '1':
        print('데이터를 입력합니다')
        input()
    elif select == '2':
        print('데이터 수정')
        input()
    elif select == '3':
        print('데이터 검색')
        input()
    elif select == '4':
        print('데이터 삭제')
        input()
    elif select == '5':
        print('데이터 종료')
        break
    else:
        print('입력오류')
        continue
  
