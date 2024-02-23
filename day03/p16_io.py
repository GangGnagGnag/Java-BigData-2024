# file : p16_io.py
# desc : 입출력 학습

#  input() 함수 기본
res = input('인사말을 적으세요 > ')   # >를 사용해서 입력하는 곳을 알려준다.
print(res)

num = input('곱할 수를 적으세요 > ')
print(type(num))
# input( )으로 받는 값은 모두 문자열 이다
num = int(num)  
print(num * 2)
# # 숫자를 입력 받아서 계산등 할때에는 형 변환이 필요하다.

num = int(input('2를 곱할 숫자 입력 > '))
print(num * 2)
# # 위에 있는 8-11행을 한줄에 줄여서 사용

## 여러값 입력
int(40.2) # 40
int('50') # 50
# int((10,20,30)) # 튜플은 바로 int로 변경할 수 있는 방법이 없기때문에 실행되지 않음

# 튜플의 괄호 중에서 할당을 받는 쪽의 괄호()는 생략 가능하다.
# (a1, a2, a3) = int(input('합산 3개의 값을 입력(구분자 space) > ').split(' '))
(a1, a2, a3) = map(int, input('합산 3개의 값을 입력(구분자 space) > ').split(' '))
a1, a2, a3 = map(int, input('합산 3개의 값을 입력(구분자 space) > ').split(' '))    # 튜플의 괄호는 생략 가능하다
print(a1,a2,a3)
# print(a1)
# print(a2)     이렇게 따로따로 써도 사용가능
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
sum = a1 + a2 + a3
print(f'합계는{sum}')   # f 는 포멧의 약자로 {} 안에 값을 넣어서 바로 출력 가능하세 해준다.


