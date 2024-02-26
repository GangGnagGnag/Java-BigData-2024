# p 295
# --------------Q1---------------

from day04.Calculator import Calculator

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value
    
cal = UpgradeCalculator()

cal.add(10)
cal.minus(7)

print(cal.value)
# --------------Q2----------------

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()

cal.add(50)
cal.add(60)

print(cal.value)

# --------------Q6----------------

def lambo(a):
    return a * 3

print(list(map(lambo, [1,2,3,4])))

#  --------------Q7----------------asdasd
print(max([-8,2,7,5,-3,5,0,1])) # 7
print(min([-8,2,7,5,-3,5,0,1])) # -8


#  --------------Q11----------------
import datetime

print(datetime.date(2024, 2, 26))   
curr = datetime.datetime.now()
print(f'{curr.year}/{curr.month}/{curr.day} {curr.hour}:{curr.minute}:{curr.second}')
