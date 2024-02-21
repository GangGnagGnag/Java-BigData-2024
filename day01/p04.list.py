# file : p04_list.py
# desc : 리스트 , 튜플

## 파이썬엔 배열이 없다. 리스트로 대신삼
even = [2,4,6,8,10]
odd = [1,3,5,7,9]

print(even)
print(even[4])  # 10        #길이가 n일때 마지막 인덱스는 -1()

even[4] = 20
print(even) # 20            # 리스트는 인덱스의 값을 변경가능하다.

datas = [123, 45.6, True, 'Hello', 'odd', None]   
#파이썬에는 형 지정이 없기때문에 어떤 자료형 이든 리스트에 할당 가능하다
print(datas)


## 인덱싱, 슬라이싱
print(odd[2])
print(even[0] + odd[0])

cpWords = ['Life', 'is', 'short']
print(cpWords[0] + cpWords[2])  #Lifeshort

print(even[1:4])    # [4, 6, 8]


## 2차원 리스트
# 3행 4열
# [[1,2,3,4]
# [5,6,7,8]
# [9,10,11,12]]

d2Datas = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]

print(d2Datas)  # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for i in d2Datas:
    print(i)    
#     [1, 2, 3, 4]
#     [5, 6, 7, 8]
#     [9, 10, 11, 12]
    
    dm1col1 = [1,2,3,4]
    dm1col2 = [1,2,3,4]
    dm1col3 = [9,10,11,12]

    print([dm1col1, dm1col2, dm1col3])
    # [[1, 2, 3, 4], [1, 2, 3, 4], [9, 10, 11, 12]]
    # 리스트 연산은 문자열 연산과 동일

    print(even + odd)
    print(odd * 2)
#  [2, 4, 6, 8, 20, 1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]

    

## 값 변경
    even[3] = 10
    print(even)

    del even[2]   # 삭제
    print(even)

##리스트 함수
# append 리스트 제일 뒤에 추가
    even.append(30) 
    print(even)

# insert  원하는 위치 값 추가
    even.insert(2, 6)   #인덱스 2에다가 6을 추가
    print(even)

# 정렬
    origin = [45, 23, 9, 17, 1, 5, 11, 3, 29, 30]

    origin.sort()   #오름 차순
    print(origin)   #[1, 3, 5, 9, 11, 17, 23, 29, 30, 45]
    origin.sort(reverse=True)   #내림 차순(Descendin)
    print(origin)   # [45, 30, 29, 23, 17, 11, 9, 5, 3, 1]

# 뒤집기
    aa = ['a', 'f', 'e', 'b'] 
    aa.reverse()

    print(aa)   # ['b', 'e', 'f', 'a']

print(aa.count('a'))    # 1
print(aa.index('e'))    # 1

bb = [1, 3, 5, 6, 8, 3, 1]
bb.remove(3)    # 맨 앞에 있는 3만 지움

print(bb)   # [1, 5, 6, 8, 3, 1]

print(even.pop())   # 30
print(even.pop())   # 30 # 스택의 기능 append() 마지막에 할당, pop() 마지막에서 값 꺼내기 
print(even) 


## 튜플
#리스트랑 동일, 단 삭제, 편집 불가능
tVal = (1, 3, 5, 7, 9)

# 튜플은 한번 만들어지면 끝까지 그대로
# tVal[2] = 11
# del tVal[2]