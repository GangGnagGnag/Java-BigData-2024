# file : p25_reivew.py
# p185


# -----------Q1-------------
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

# # -----------Q2-------------
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

# # -----------Q3-------------
input1 = int(input(" 첫 번째 숫자를 입력하세요: "))
input2 = int(input(" 두 번째 숫자를 입력하세요: "))


total = input1 + input2
print("두 수의 합은 %s 입니다" %total)

# -----------Q4-------------
# 3
print("you""need""python")                  #youneedpython
print("you"+"need"+"python")                #youneedpython
print("you","need","python")                #you need python
print("".join(["you","need","python"]))     #youneedpython

# -----------Q5-------------
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# -----------Q6-------------
user_input = input("저장할 내용을 입력하세요: ")
f = open('test4.txt','a')
f.write(user_input)
f.write('\n')
f.close()


