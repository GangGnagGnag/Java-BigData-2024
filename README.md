# 빅데이터 언어2024        
빅데이터 자바 개발자 파이썬 학습 리포지토리

## 1일차
- 파이썬 개발환경
    - [깃허브](https://github.com)가입
    - [깃 설치](https://git-scm.com/downloads) 설치
    - [깃허브 데스트탑](https://desktop.github.com/) 설치
    - [파이썬](https://www.python.org/downloads/) 설치
    - [Visual Studio code](https://vscode.dev/github/hyanyul/python-2024/blob/main/README.md)설치
    - [나눔고딕코딩](https://github.com/naver/nanumfont) 글자체 설치

- 파이썬 학습
    - 파이썬 개요
        - 1990년 네덜란드 개발자 귀도 반 로섬이 개발
        - 쉽고, 간결한 문법, 무료, 빠른 개발속도
    - 파이썬 기초문법
        - 숫자형(정수, 실수, 진수)
        
        ```python
        # 숫자는 변수만 선언, 값만 할당하면 숫자형으로 지정
        # C, C++, 자바, C# 처럼 형 지정이 없음!
        val = 10    # 정수형
        val-2.15    # 실수형


        # 특수 숫자형
        binVal = 0b11111111     #225(2진수)
        octVal = 0o11           #1~7   10(8진수)
        hexVal = 0xFF           # = 255  0~9ABCDEF (16진수)    
        print('이진수', binVal, '8진수', octVal, '16진수', hexVal)
        ```

        - 문자열형(특수형 리스트) (연산, 문자열 포맷, 함수)
        '''python
         # '',"" 모두 사용 가능
        '''
        - 리스트현, 튜플형(연산, 함수)  
            - 리스트는 수정 삭제 가능
            - 퓨플은 수정 삭제 불가 (그 외에는 리스트와 동일함)


## 2일차
- 파이썬 학습
    - 파이썬 기초문법
        - 딕셔너리, 집합
        - 불형
        - None형
        - 제어문(if, while, for)
        - 제어문 연습
        - 함수

## 3일차
- 파이썬학습
    - 파이썬 기초문법
        - 입출력
        - 객체지향

## 4일차
- 파이썬학습
    - 파이썬 기초문법
        - 모듈, 패키지
        - ★ 예외처리,디버깅 ★ : 디버깅 하면서 예외를 찾고, 거기서 예외를 처리해야함.
        - 내장함수
        - 표준 및 외부 라이브러리

## 5일차
- 파이썬 학습
    - 파이썬 응용
        - OS내 디렉토리 검색
        - 아스키 및 유니코드
        - 주소록 앱 만들기

       ```python
       class Contact: # 주소록 클래스
            # 생성자
            def __init__(self, name, phoneNumber, eMail, addr) -> None:
                self.__name = name
                self.__phoneNumber = phoneNumber
                self.__eMail = eMail
                self.__addr = addr

            # 사용자가 원하는 형태로 출력
            def __str__(self) -> str: # 원래출력 <__main__.Contact object at 0x0000024500772150> 
                res = (f'이  름 : {self.__name}\n'
                    f'핸드폰 : {self.__phoneNumber}\n'
                    f'이메일 : {self.__eMail}\n'
                    f'주  소 : {self.__addr}')
                return res
            
            # 연락처 여부확인
            def isNameExist(self, name):
                if self.__name == name: # 찾는 이름 존재
                    return True
                else:
                    return False
                
            def getInfo(self):
                return self.__name, self.__phoneNumber, self.__eMail, self.__addr
        ```

        ![주소록앱](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata01.gif)

        - Windows App만들기(PyQt)

        ![QtApp](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata02.png)

## 6일차(2402.02.28)
- 파이썬 학습
    -PyQt5 학습 이어서
        - Qwidget 자식 클래스 종류 학습


    ![QLabel](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata03.png)

    - Naver 뉴스API 검색 앱

    ![naverApp](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata04.png)

## 7일차
- 파이썬 학습
    - pyQt5 계속
        - Naver 뉴스API 검색 앱 마무리

    - json 학습
    - PyQt5
        - 스레드 개념, 학습

        ![스레드](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata05.png)

- 파이썬 응용
    - TTS
    
    - QR코드 생성기

    ![QR](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata06.png)

    - 구글번역기앱

    ![구글번역](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata07.png)


## 8일차

- 파이썬 학습
    - 파이썬 자동화
        - PyAuyoGui 모듈 ( 마우스, 키보드, 화면캡처)
        - 슬랙 webhook로 모아빌 메시지 전송

            <!--![슬랙](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata08.jpg) -->
            <!--html 태그로 이미지를 삽입하면 문제없음-->
            <img src="https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata08.jpg" width="250">

        - Tesseract 프로그램으로 이미지에서 글자 추출(인식률 높이려면 트레이닝을 해서 트레이닝 데이터를 만들어야함)


        ![OCR](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata09.png)


## 9일차
- 파이썬 응용
    - 이미지 처리 OpenCV [윤대희님 깃헙](http://076923.github.io/posts/Python-opencv-1/) 참조

    ![얼굴인식](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata10.gif)

    - [Flask](https://flask-docs-kr.readthedocs.io/ko/latest/index.html)
    - [Django](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django) 웹서버

    - 그림에디터 만들기(with PyQt5)

    ![editor](https://raw.githubusercontent.com/GangGnagGnag/Java-BigData-2024/main/images/bigdata11.gif)

## 10일차 
- 파이썬 응용
    - 그림에디터 완성(OpenCV 그레이스케일)

        > ?mp4로 동영상 업로드 하려면 github 사이트에서 Readme.md 를 수정 클릭 후. mp4 드래그만 하면 됨
        > 제한사항은 10mb 이하

    - 실행파일 만들기
        - PyIstaller 모듈 설치
        ''' shell
        > pip install pyinstaller
        > pyinstaller -w -F pythionfile.py
        '''
        - -w는 윈도우창만 실행 콘솔창삭제, -F _internal 폴더 생성안되도록, 진짜 oneFile 로 만들기; 
        - 실패, 재 생성시는 build, dist폴더 삭제, pythonfile.spec 삭제 뒤 명렁어 실행
    
    - Jupyter Notebook 사용법(빅데이터 분석, 코딩테스트)
        - Ctrl + Shift + P (명령 팔레트)
        - 노트북 사용 
        - ChatGPT API 사용
            - https://github.com/teddylee777/openai-api-kr

    - 메모장 만들기(참조링크)
        - https://www.youtube.com/watch?v=6jPXGgON6oU&list=PLnIaYcDMsScwsKo1rQ18cLHvBdjou-kb5&index=5 참조해서 만들기
        - https://pagichacha.tistory.com/44 참조해서 만들기 