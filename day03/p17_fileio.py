# file : p17_fileio.py
# desc : 파일 입출력 학습

#  컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open() , close() / 파이썬에서만 안닫아도 크게 지장은 없음
# 2. 네트워크 open() , close() 
# 3. DB open(or connect) , close()

# 언어체계 추가 ASCII(한들 cp949), 유니코드(utf-8)

# 상대경로, 절대경로(*중요*)
# 절대 경로는 필요한 상황이 아니면 쓰지말기

# w 는 매번 새로 파일 생성, a는 기존 파일에 내용 추가
# 로그 등을 남길땐 a 로 작업해야함
f = open('./sample.txt', mode='a', encoding='utf-8')
# 파일쓰기 진행
f.write('안녕하세요. 파이썬.\n')    # 한줄 띄워쓰기 할때는 \n쓰기
f.write('오늘만 하면 내일 쉰다!!!!\n')


f.close() # 파이썬에서는 없어도 됨.다른언어에선 무조건 close()






