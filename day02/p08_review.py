#file: p08_review.py

# Q2
a = 13
print('a는', end ='' )
if a % 2 == 0 :
    print('짝수')
else:
    print('홀수')

# a는홀수

#Q3
pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
# 881120
# 1068234

pin = '881120-1068234'
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)
# 881120
# 1068234

# Q5
a = "a:b:c:d"
b = a.replace(':','#')
print(b)    
#a#b#c#d

# Q6
a = [1,3,5,4,2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]


# Q10
a = {'A':90, 'B':80, "C":70}
result = a.pop('B')
print(a)
print(result)
# {'A': 90, 'C': 70}
# 80