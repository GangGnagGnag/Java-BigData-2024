# file: p07_variable.py
# desc: 변수에 대하여

import copy


a = [1,2,3]
print(id(a))
b = a
print(id(b))

# c = 1
# d = c
# print(id(c))
# print(id(d))
# 주소값을 나타내줌

# del b[2]
# print(a)    
#[1, 2]
# 같은 주소값을 나타내기때문에 b 를지워도 a 에 있는 값이 없어짐

d = copy(a)
print(id(d))
del d [2]
print(a)







