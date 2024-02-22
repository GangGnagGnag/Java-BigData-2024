# file: p06_bool.py
# desc: 불타입, None 타입 학습

# 참 / 거짓   (중요함)

# 파이썬에서는 대문자를 쓰기
a = True    
b = False

print(a)
print(type(a))  # <class 'bool'>
print(type(1))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type('Hi'))  # <class 'str'>
print(type([1,2,3]))  # <class 'list'>
print(type((1,2,3)))  # <class 'tuple'>
# 모든 타입을 알고 싶다면 type사용
# type 은 내장 클래스 이다

print( a == b )         #False
print( a != (not b) )   #False


print(bool(3))  #True
print(bool(0))  #False
# 참 / 거짓을 나누는 것은 빈값( 0, None. False ) 그 외에는 True

##None 타입
None

c = None
a = 1
b = 0
print(c)    # None
print(a + b) # a True(1) False(0)   # 1

c = 3
print(c + a)    # 4

