# p27_exceptionHandle.py
# desc : 예외처리2
# 비정상적인 종료를 막기 위한것

while True:
    try:
        select = int(input('메뉴입력 1.저장, 2.검색, 3.종료 > '))
    except:
        print('예외발생 입력을 정확히 하세요')
        continue    

    if select == '1':
        print('입력')
    elif select == '2':
        print('검색')
    elif select == '3':
        break
    else:
        continue

