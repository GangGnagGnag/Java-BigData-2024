# p 295
# --------------Q1---------------


cal1 = UpgradeCalculator(Cal)

print(cal1.add(10))
print(cal1.minus(7))

print(cal1.value)

# --------------Q2----------------

# MaxLimitCalculator = Calculator
# cal = MaxLimitCalculator(100)

# cal.add(50)
# cal.add(60)

# print(cal.value)

# --------------Q6----------------

def lambo(a):
    return a * 3

print(list(map(lambo, [1,2,3,4])))

#  --------------Q7----------------
print(max([-8,2,7,5,-3,5,0,1])) # 7
print(min([-8,2,7,5,-3,5,0,1])) # -8


#  --------------Q11----------------
import datetime

print(datetime.date(2024, 2, 26))   
curr = datetime.datetime.now()
print(f'{curr.year}/{curr.month}/{curr.day} {curr.hour}:{curr.minute}:{curr.second}')
