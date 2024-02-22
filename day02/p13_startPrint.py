# file : p13_startPrint.py
# desc : 별찍기
print('예제그림')
for i in range(1, 6): 
    print('*' * i)

# 2중 for 문으로 만들기
print('\n')


print('-----별 찍기 -----')

for i in range(1, 6):       # 건들 필요없음
    for j in range(i, 6):   # range() 안쪽만 손대면 끝
        print(' ', end='')

    for j in range(6-i, 6):
        print('*', end='')
    print()
    