# file : p66_imageEditor.py
# desc : PyQt 이미지 에디터
'''
qrc 파일을 사용하려면 
> pyrcc5 "resources.qrc" -o "resources_rc.py"

imutils
> pip install imutils
'''

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
# 리소스 파일 추가
import resources_rc
# OpenCV 추가, imutils 모듈 추가
import cv2, imutils

class WinApp(QMainWindow): # QWidget이 아님!!
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        # uic.loadUi('./day09/pyNewPaint.ui', self) # VSCode용
        uic.loadUi('F:/Source/java-BigData-2024/day09/pyNewPaint.ui', self) # PyInstaller 용 절대경로를 다 적어줘야함
        # self.setWindowIcon(QIcon('./day09/imgs/editor.png')) # PyInstaller 용
        self.setWindowIcon(QIcon('F:/Source/java-BigData-2024/day09/imgs/editor.png')) # PyInstaller 용 절대경로를 다 적어줘야함
        self.setWindowTitle('이미지에디터 v0.5')
        ## 이미지 추가/ 여러가지 UI에 대한 초기화 
        # pixmap = QPixmap('./day09/coby.jpg').scaledToHeight(501)
        pixmap = QPixmap('./day09/coby.jpg').scaledToHeight(501)
        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.red # 빨간색 기본
        ## UI 초기화 끝
        self.show()
    
    def initSignal(self):
        # 메뉴/툴바 액션에 대한 시그널처리함수 선언...
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.action_PenRed.triggered.connect(self.actionPenRedClicked)
        self.action_PenGreen.triggered.connect(self.actionPenGreenClicked)
        self.action_PenBlue.triggered.connect(self.actionPenBlueClicked)
        self.action_About.triggered.connect(self.actionAboutClicked) 
        # 변환 메뉴 추가
        self.action_Grayscale.triggered.connect(self.actionGrayscaleClicked)

        
    def actionBlurClicked(self):
            # tmpPath = './day09/temp.png'
            tmpPath = './temp.png'
            pixmap = self.lblCanvas.pixmap() # 라벨에 있는 그림을 pixmap 변수에 저장
            pixmap.save(tmpPath)
            image = cv2.imread(tmpPath)
            blur = cv2.blur(image, (10,10))
            blurImg = QImage(blur, blur.shape[1], blur.shape[0], blur.strides[0], QImage.Format_BGR888)
            self.lblCanvas.setPixmap(QPixmap.fromImage(blurImg))


    def actionGrayscaleClicked(self):
        # image = cv2.imread()
        # QMessageBox.about(self,'알림','그레이스케일')
        ## temp.png  와 같은 형태로 임시 이미지 저장
        # openCV로 불러옴
        #그레이스케일로 변경한 다음
        #변경한 이미지를 다시 pixmap으로 변환뒤 lblCanvas에 올림
        # tmpPath = './day09/temp.png'
        tmpPath = './temp.png'
        pixmap = self.lblCanvas.pixmap() # 라벨에 있는 그림을 pixmap 변수에 저장
        pixmap.save(tmpPath)
        image = cv2.imread(tmpPath)
        # gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('result', gray)
        grayImg = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_Grayscale16)
        self.lblCanvas.setPixmap(QPixmap.fromImage(grayImg))

    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(), self.lblCanvas.height())
        # canvas = QPixmap(801, 471)
        canvas.fill(QColor('white'))
        self.lblCanvas.setPixmap(canvas)

    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(self, '이미지열기', '', 'Image file(*.jpg;*.jpeg;*.png)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.lblCanvas.adjustSize()
        

    def actionSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지저장', '', 'Image file(*.png)')
        if filePath == '': return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath)

    def actionExitClicked(self):
        cv2.destroyAllWindows()
        exit(0) # 아주 쉬워요~

    def actionPenRedClicked(self):
        self.brushColor = Qt.red

    def actionPenGreenClicked(self):
        self.brushColor = Qt.green

    def actionPenBlueClicked(self):
        self.brushColor = Qt.blue

    def actionAboutClicked(self):
        QMessageBox.about(self, '알림', '이미지 에디터 v0.5')

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y()-(54))
        brush = QPainter(self.lblCanvas.pixmap()) # lblCanvas에 브러쉬 하나 생성
        brush.setPen(QPen(self.brushColor, 3.5, style=Qt.SolidLine, cap=Qt.RoundCap))
        brush.drawPoint(e.x(), e.y()-(54))
        brush.end()
        self.update() # 화면 업데이트

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            cv2.destroyAllWindows()
            QCloseEvent.accept()
        else: QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())