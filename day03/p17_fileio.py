# file : p17_fileio.py
# desc : 파일 입출력 학습

#  컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open() , close() / 파이썬에서만 안닫아도 크게 지장은 없음
# 2. 네트워크 open() , close() 
# 3. DB open(or connect) , close()

# 언어체계 추가 ASCII(한들 cp949), 유니코드(utf-8)
f = open('./sample.txt', mode='w', encoding='utf-8')
# 파일쓰기 진행
f.write('안녕하세요. 파이썬')
f.write('오늘만 하면 내일 쉰다!!!!')


f.close() # 파이썬에서는 없어도 됨.다른언어에선 무조건 close()






