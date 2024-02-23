# p188 Q7


# ----------------------------------------------------------

f = open('./day03/test1.txt','w')   # 파일만들려면 w
f.write('Life is too short\n you need java')
f.close()

f = open('./day03/test.txt', 'r')
f = open('./day03/test1.txt', 'r')
body = f.read() # 문자열이기 때문에 결과를 문자열로 리턴, read 함수는 텍스트가 길면 문장이 잘려서 나온다.
f.close()

body = body.replace('java','python')
f = open('./day03/test.txt', mode = 'w', encoding='utf-8') 
f = open('./day03/test1.txt', mode = 'w', encoding='utf-8') # 파일이 있어서 덮어쓰기느낌?

f.write(body)
f.close()
# 하지만! read는 길이 제한이 있음.
# ----------------------------------------------------------

f = open('./day03/test2.txt','w')   # 파일만들려면 w
f.write('Life is too short\n you need java')
f.close()

f = open('./day03/test.txt', 'r')
body = f.readlines()    # 결과를 리스트로 리턴
f.close()

body = [body[0], body[1].replace('java','python')]
f = open('./day03/test2.txt', mode = 'w', encoding='utf-8') 
f.write(body[0] + body[1])
f.close()