# file : p34_addrBook.py
# desc : 콘솔 주소록 프로그램

class Contact: # 주소록 클래스
    # 생성자
    def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

# 사용자가 원하는 형태로 출력
    def __str__(self) -> str:   # 원래 출력 <__main__.Contact object at 0x000001F60DD92330>
        res = (f'이  름: {self.__name}\n'
               f'핸드폰: {self.__phoneNumber}\n' 
               f'이메일: {self.__eMail}\n'
               f'주  소: {self.__addr}')
        return res

def run(): 
    first = Contact('한국진', '010-6541-5634', 'korean@naver.com','부경')       
    first = Contact(addr='부경', phoneNumber='010-6541-5634', name='한국진', eMail='korean@naver.com')
# 두가지 방법중 첫번째 방법은 순서대로 적어줘야하고 두번째 방법은 순서를 내 마음대로 바꿀수 있음
    print(first)

if __name__ == '__main__': #메인 엔트리
    print('프로그램 시작')
    run() # 메인함수 실행

print('프로그램 종료')
