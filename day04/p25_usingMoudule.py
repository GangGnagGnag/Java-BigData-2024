# file : p25_usingMoudule.py
# desc : 모듈 사용

# import calc as c# calc.py 를 사용함 # as를사용해서 이름을 바꿀수도 있음/같은 이름이 있으면 충돌나기때문에 as 로 이름을 바꿔줌
from calc import mul # mul() 이라는 함수명만 쓰면 됨
# 모듈을 하나만 쓸때는 사용해도 좋지만 여러개의 모듈을 사용할 때에는 같은 함수명이 있으면 충돌남

from Math import Math   # from Math는 모듈(파일이름) import Math는 클래스이름

from day03.p22_carClass import Car # 디렉토리(모듈묶음: 패키지).모듈명

if __name__ == '__main__':      ## 자바의 void main() 이랑 같음
    result = mul(10, 7)
    print(result)

    print(__name__) # 명시적으로 모듈의 시작되는 포인트라는 의미 / __main__ = 메인 엔트리

    myMath = Math()
    print(myMath.solv(10))