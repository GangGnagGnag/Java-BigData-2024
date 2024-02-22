# file: p05_dict.py
# desc: 딕셔너리 자료형

## 딕셔너리 구성
spiderMan = { 'name':'Peter Parker', 'age':18, 'weapon':'Web shooter', 'friend':['ironMan','Thor','CaptainAmerica'] }

## 출력
print(spiderMan)
print(spiderMan['name'])

## 값 추가
spiderMan['job'] = 'CameraMan'
print(spiderMan)
# {'name': 'Peter Parker', 'age': 18, 'weapon': 'Web shooter', 'friend': ['ironMan', 'Thor', 'CaptainAmerica'], 'job': 'CameraMan'} 

## 값 삭제
del spiderMan['friend']
print(spiderMan)
# {'name': 'Peter Parker', 'age': 18, 'weapon': 'Web shooter', 'job': 'CameraMan'}

## 딕셔너리 함수
#파이썬은 메소드를 무조건 함수라고 칭함
 # keys는 함수이기때문에 괄호 사용
print(spiderMan.keys()) # 딕셔너리에 현재 존재하는 키 목록
print(list(spiderMan.keys()))   # 키목록을 리스트 형태로 형 변환 # ['name', 'age', 'weapon', 'job']
print(spiderMan.items())    # 딕셔너리 모든 아이템 출력
print(spiderMan.get('job'))     # 딕셔너리에 값 가져오기    #CameraMan

print('friends' in spiderMan) # 딕셔너리안에 키가 있는 지 확인
print(spiderMan.values())

res = spiderMan.pop('job')# 마지막 값을빼냄
print(res)
print(spiderMan)   
#{'name': 'Peter Parker', 'age': 18, 'weapon': 'Web shooter'}
print(spiderMan.pop('age'))
print(spiderMan)

## 데이터 삭제          
spiderMan.clear()
print(spiderMan)    #{}

# 완전 삭제
del spiderMan
print(spiderMan)
#   print(spiderMan)
#           ^^^^^^^^^       아예 값이 없다고 나옴.
# clear 는 데이터만 삭제하지만 del 은 값을 아예 없애버림

## 집합 : 중복을 허용하지 않는다, 순서가 없다
# set([1,2,3,4,3,4,2,1]) = {1,2,3,4}   순서가 계속 바뀜 



