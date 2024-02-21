# file: p02_number.py
#desc: 숫자형 자료타입 및 연산

# 일반 수자형
age = 40        #int 형 숫자 40을 담는 변수
taxRate = 8.8   # float 형을 담는 변수
highFloat = 4.2E10  # 지수승 (float)

# 파이썬은 무조건 문자열
print('나이는: ', age)          # 문자열이 "",'' 둘다 사용가능
print('세율은: ', taxRate)      
print('지수값: ', highFloat)

# 특수 숫자형
binVal = 0b11111111     #225
octVal = 0o11           #1~7   10(8)
hexVal = 0xFF           # = 255  0~9ABCDEF          모든 이유는 컴퓨터 때문임.ㅠ
print('이진수', binVal, '8진수', octVal, '16진수', hexVal)
# 숫자를 아무리 적어도 10진수로 값이 나온다.

#  결론: 타입을 적을 필요가없이 그냥 사용하면 된다.

# 사칙연산
a, b, c = 3, 4, 9
print(a + b)
print(a - c)
print(a * c)
print(b / c)

# 단, 나누기는 3가지로 분류됨
print(c / b)    #정확하게 실수로 나누기 
print(c // b)   #정수로 나누기 몫
print(c % b)    #정수로 나눈 나머지 값

# 제곱연산
print(2 ** 10)  # = 1024 import math; math.pow() 할때 사용
# * 하나만 하면 곱하기 두개 하면 제곱

print(a + b) * c  # 연산자 우선순위는 ()괄호만 잘 쓰면 된다.

