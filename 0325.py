#애플리케이션에 필요한 라이브러리 추가
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)
#애플리케이션 핸들러와 빈 GUI위젯
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    #QWidget 클래스를 상속받아서 클래스를 정의

    def __init__(self):
        super().__init__()
        #부모클래스 QWidget을 초기화
        self.initUI()
        #나머지 초기화는 initUI함수에 정의

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message', self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage)
        #버튼 클릭시 핸들러 함수 연결

        self.btn2 =QPushButton('Clear',self)
        self.btn2.clicked.connect(self.clearMessage)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)

        vbox.addLayout(hbox)
        # 빈 공간 - 버튼 - 빈 공간간 순으로 수직 배치된 레이아웃
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        #Windows에 표시되는 타이틀
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
        #Windows화면 표시
    def activateMessage(self):
        #버튼을 클릭할 떄 동작하는 함수 : 메세지 박스 출력
        #QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        self.te1.clear()
if __name__ == '__main__':
    #pyqt는 애플리케이션 당 1개의 QApplication이 필요함
    app = QApplication(sys.argv)
    #QApplication 인스턴스 생성
    view = Calculator()
    # Calculator windows 인스턴스 생성
    sys.exit(app.exec_())
    #Application이 event 처리를 하도록 루프 생성성