# file : p33_unicode.py
# desc : 아스키, 유니코드 설명

a = "Life is short, you need python"
print(a)
print(type(a))

b = a.encode('utf-8') # 유니코드로 변환
print(b)
print(type(b))  # 2진수로 데디터 표현, 네트워크로 데이터 전송/ DB에 저장/ 파일로 저장 등 데이터전송에 최적화

c = a.encode('euc-kr') # or cp949 한글체계 cp949로 변환 / 글씨가 깨질수도 있기 때문에 만약 글자가 깨지면 인코딩을 해줘야함
print(c)
print(type(c))

print(b.decode('utf-8'))    # 유니코드로 문자열 변환   
