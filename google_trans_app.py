import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans

form_class = uic.loadUiType('ui/googleUi.ui')[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()  # 부모의 초기화자 호출

        self.setupUi(self)  # 제작해 놓은 googleUi.ui를 연결
        self.setWindowTitle('구글 한줄 번역기')  # 앱 윈도우 타이틀
        self.setWindowIcon(QIcon('icons/google.png'))
        self.statusBar().showMessage('Google Trans App V 0.1')

# 번역 버튼 : trans_btn , 초기화 버튼 : reset_btn
# 한국어 입력 : input_kor_text
# 영어 번역 : output_eng_text
# 일어 번역 : output_jap_text
# 중국어 번역 : output_cha_text

        self.trans_btn.clicked.connect(self.trans_operation)
        self.reset_btn.clicked.connect(self.reset_operation)

    def trans_operation(self):

        trans = googletrans.Translator()
        trans_str = self.input_kor_text.text()
        trans_eng = trans.translate(trans_str, dest='en')
        trans_jap = trans.translate(trans_str, dest='ja')
        trans_cna = trans.translate(trans_str, dest='zh-cn')

        self.output_eng_text.append(trans_eng.text)
        self.output_jap_text.append(trans_jap.text)
        self.output_cha_text.append(trans_cna.text)

    def reset_operation(self):

        self.input_kor_text.clear()
        self.output_eng_text.clear()
        self.output_jap_text.clear()
        self.output_cha_text.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
