# file : p26_exceptionHandle.py
# desc : 예외처리
# 오류(Error) 코드상 빨간색 밑줄이 그어지는 것
# 예외 : 프로그램 실행 중에 생기는 오류(비정상적 종료)

# 파일 읽어서
try:
    f = open('./saㅜple.txt', mode = 'r', encoding ='utf-8')
    # f.close()
    res  = f.readline()
    print(res)
except:
    print('파일오픈 예외발생')
else:   #오류가 없는 경우에만 수행
    f.close()
# finally:
#     try:    # try~except는 다중으로 사용하면 성능에 별로 안좋음
#         f.close()   # f에 파일 객체자체가 없어서 close() 불가
#     except NameError as e:
#         print('파일 오픈 실패')

# 2. 계산결과
try:
    print(5 / 0)
except ZeroDivisionError as e:
    print('파일 오픈 예외 발생',e.args)

# a, b = 5, 3

# if a == b:
#     print(True)   
    
class Chicken:
    def fly(self):
        raise NotImplementedError

koko = Chicken()
try:
    koko.fly()
except Exception as e:
    print('닭은 못나농',e.args) # NotImplementedError는 추가 예외메시지가 없음 ( )

