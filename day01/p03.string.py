# file: p03_string.py
# desc: 문자열 자료형 연산

a = "Hello World"
print(a)

b = 'Hello World'
print(b)

c = "Hello, 'Ashley'"       #문자열로 주고싶을 경우에는 앞과 끝에 " " 넣주기
print(c)
# 탈출문자 \n,\t 외 나머지는 파이썬에서 잘 사용되지 않음.

# 문자열에서 문장을 여러줄 쓰고 싶으면 
# \는 문장을 이어주는 역할을함
d  = 'Hello~ \n'          
'I\'m gyeongho~' \
'Nice'
print(d)
#  여러줄 문장을 쓸때는 ''',  """ 사용하기 줄 맞춘다고 tab을 사용할 경우 tab 까지 같이 출력됨
d = '''Hello~ 
I'am Ashley.
Nice'''
print(d)


## 문자열 연산 +, *
before = 'I wanna go to'
after = 'Boracai'
print(before + after)   # +는 문자열을 합쳐서 하나의 문자열 만듬
# print(before * after)  # 이런건 없음
print(after * 3)   # 하나의 문자를 여러번 출력하고싶으면 * 사용


## 문자열 길이 구하기
print('글자길이 = ',len(before))
print('한글 글자 길이', len('안녕하세요'))  #글자 자체는 5


## 문자열 인덱싱, 슬레이싱
cp = 'Life is too short, You need Python'
print(len(cp))


## 슬라이싱
print(cp[8])
print(cp[17])

# cp[8] = 'd' #문자열은 배열이긴 하지만 값을 변경할 수 없다.
# 문자열 범위 슬라이싱
print(cp[12:16 + 1])        #앞은 시작하는인덱스 뒤는 끝나는 인덱스
# 뒤에 있는 숫자는 항상 +1

print(ascii('안')),ascii('녕'),ascii('하'),ascii('세'),ascii('요')
print(chr(65))

#기존 문자열로 새로운 문자열을 만들때는 슬라이싱, 다른 문자열로 대체 필수 
print(cp[0:7+1], 'long',cp[17:])    # :뒤에 값을 생략하면 끝까지 

# 다른언어에는 -슬라이싱이 없음
print(cp[-6:])
print(cp[-11:-7])       # -로 슬라이싱 할때도: 뒤에도 +1을 해줘야함


## 문자열 포메팅(format String)
## 파이썬 에서는 %d, %s, %c 등 포멧 스트링용 연산자는 사용 빈도가 낮음.
temp = 21
print('현재온도는 %d 도 입니다' % temp)     #현재온도는 21 도 입니다
temp = 17
print('현재온도는 %d 도 입니다' % temp)     #현재온도는 17 도 입니다 
    
# format이라는 함수를 통해서 포매팅(가장 일반적)
print('현재 온도는 {0}도 입니다'.format(temp))


## 날짜를 포맷으로 만들때
month = 2
day = 21
hour = 3
mins = 18
sec = 9 
print('오늘은 {0:02d}월 {1:02d}일 {2:02d}시 {3:02d}분 입니다'.format(month, day, hour, mins))
#  오늘은 02월 21일 03시 18분 입니다
print('오늘은 {0:02d}-{1:02d}, {2:02d}:{3:02d}입니다'.format(month, day, hour, mins))
# 오늘은 02-21, 03:18입니다

# 숫자 자료형 에서 _ 사용 
salary = 6_000_000  # 600만원
income = 6_000_000_000 # 60억 연매출
print('올해 매출액은{0}원'.format(income))  # 올해 매출액은6000000000원 으로 출력됨 적은값과는 다르게 _가 나오지 않음
print('올해 매출액은{0:,d}원'.format(income)) # 올해 매출액은6,000,000,000원  

PI = 3.1415926536  # 소수점 10째 자리까지
print('파이는{0:.2f}'.format(PI))  #소수점 둘째 자리 까지
print('파이는{0:10.2f}'.format(PI)) #파이는      3.14   // 10.2f 소수점 .까지 다 포함해서 10자리, 소수점뒤는 2 자리
# print('{0:d}'.format(PI)) # 실수형은 d(정수형 포멧팅) 불가능


## f  포멧팅 3.6(2016) 이후에 나온 최신방식
name = '한국진'
age = 29

cont = f'나는{name}이고, 나이는 {age}세 입니다.'
print(cont)

name = '박창현'
age = 28
print(f'나는{name:>10}이고, 나이는 {age:03d}세 입니다.')
# 나는       박창현이고, 나이는 028세 입니다.
# :> 앞으로 10칸 밀어라 :< 뒤로 10 칸 밀어라
# 03d 개의 숫자로 나타내라
print(f'나는{name:>10}이고, 나이는 {age:03.1f}세 입니다.')
# 나는       박창현이고, 나이는 28.0세 입니다.
# 정수는 f 포맷 사용가능하지만 실수는 d 포맷이 사용 불가능하다


##문자열 함수
a = 'Life is short, You need Python'

print(a.count('Life'))    # 1      # 이 문장안에 Life가 있다는 뜻
print(a.count('o'))       # 3 

print(a.find('sh'))       # 8       #8번째 문자에서 사용된다는 의미.

print(a.index('t'))       # 12         #첫번째 t의 위치
print(a.count('k'))       # index()는 count()로 갯수가 0이 아닐때만 호출
print(','.join('abcde'))  #a,b,c,d,e 

print(a.upper())        # LIFE IS SHORT, YOU NEED PYTHON
# 소문자는 대문자로 바꿔주는 함수

print(a.lower())        #life is short, you need python
# 대문자를 소문자로 바꿔줌

print(a.capitalize())   #Life is short, you need python
# 문장이 시작되는 첫번째 단어의 첫글자만 대문자로 

origin = '          Hi          '
print(f'++{origin}++')      #++          Hi          ++
print(f'++{origin.lstrip()}++')     #왼쪽공백을 없앤다  # ++Hi          ++
print(f'++{origin.rstrip()}++')     # 오른쪽 공백없앰   #   ++          Hi++
print(f'++{origin.strip()}++')     # 양쪽 공백 없앰     #   ++Hi++
# 문자 사이의 공백만 없앨수 있음.

print(cp.replace('too','').replace(' short','long'))        # Life is long, You need Python


##문자열 자르기   ->    리스트(파이썬은 배열이x 리스트로 모든걸 만듦)
cpWords = cp.split(' ')
print(cpWords)      # ['Life', 'is', 'too', 'short,', 'You', 'need', 'Python']