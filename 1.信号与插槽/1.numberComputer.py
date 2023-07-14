from PySide6.QtWidgets import QApplication, QWidget
from Ui_untitled import Ui_computer

##########################################################
#   按键绑定、事件发布以及处理
#   eval 计算字符串中的数学表达式
#   信号 与 槽 signals and slot
#   component.signal.connect(slot)
#   eval 计算字符串中的数学表达式
##########################################################

class NumberComputer(QWidget, Ui_computer):
    def __init__(self):
        super().__init__()
        # 通过setupUi绑定设计好的ui文件
        self.setupUi(self)

        self.result = ''

        self.bind()
        # 使用自定义bind函数对
    
    def bind(self):
        # 对按钮进行绑定
        self.pushButton_0.clicked.connect( lambda: self.addStr('0'))
        self.pushButton_1.clicked.connect( lambda: self.addStr('1'))
        self.pushButton_2.clicked.connect( lambda: self.addStr('2'))
        self.pushButton_3.clicked.connect( lambda: self.addStr('3'))
        self.pushButton_4.clicked.connect( lambda: self.addStr('4'))
        self.pushButton_5.clicked.connect( lambda: self.addStr('5'))
        self.pushButton_6.clicked.connect( lambda: self.addStr('6'))
        self.pushButton_7.clicked.connect( lambda: self.addStr('7'))
        self.pushButton_8.clicked.connect( lambda: self.addStr('8'))
        self.pushButton_9.clicked.connect( lambda: self.addStr('9'))
        self.pushButton_point.clicked.connect( lambda: self.addStr('.'))
        self.pushButton_plus.clicked.connect( lambda: self.addStr('+'))
        self.pushButton_minus.clicked.connect( lambda: self.addStr('-'))
        self.pushButton_multiply.clicked.connect( lambda: self.addStr('*'))
        self.pushButton_division.clicked.connect( lambda: self.addStr('/'))
        self.pushButton_del.clicked.connect( lambda: self.back())
        self.pushButton_clear.clicked.connect( lambda: self.clearStr())
        self.pushButton_enter.clicked.connect( lambda: self.equal())

    def addStr(self, str):
        self.lineEdit.clear()
        self.result += str  
        self.lineEdit.setText(self.result)

    def equal(self):
        self.numberResult = float(eval(self.result))
        self.lcdNumber.display(self.numberResult)

    def clearStr(self):
        self.lineEdit.clear()
        self.result = ''

    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)


if __name__ == '__main__':
    app = QApplication([])
    window = NumberComputer()
    window.show()
    app.exec()