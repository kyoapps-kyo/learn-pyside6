########################################################
# exe \ txt \ mp4 \ db ... 通过QRC规定，传换成二进制存入py文件中
# designer 中，右下角资源浏览器创建qrc文件
# import xxx_rc.py
# self.label.setPixmap(QPixmap(u":/images/Zombatar_1.jpg")) # 在Python中，通过在字符串前面添加 "u" 前缀，可以指示解释器将字符串视为Unicode编码。
# self.label.setScaledContents(True) # 等比例填充
#  self.label.setAlignment(Qt.AlignCenter) #  垂直居中
########################################################

from PySide6.QtWidgets import QApplication, QWidget
from Ui_untitled import Ui_Form

class MyMainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec() 