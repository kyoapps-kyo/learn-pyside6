from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# self.sender() 调用对象
# f相当于字符串模板 f'str{变量}'

# slide常用的方法：setMinimun() setMaximum,同时设置setRange(min, max)
# 调用slide的信号与槽时，会自动将slide自身当前的index传过去，可以用value进行接受
# 设置刻度setTickPosition(QSlider.TickPosition.TicksBelow)
# 设置刻度间隔 setTickInterval(num)

############################################################
#   常用布局控件
#   水平：QHBoxLayout 垂直：QVBoxLayout
#   格子布局：QGridLayout 表单布局：QFormLayout
#   定义布局: QHBoxLayout()
#   添加布局：.addLayout()
#   添加组件：.addWidget()
#   设定布局：self.setLayout(self.mainLayout)

#   FormLayout: .addRow() .addWidget()

#   grid: addWidget(widget, rowIndex, 跨行数?, colIndex, 跨列数?)
############################################################

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton('button', self)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.resize(800, 600)
    window.show()
    app.exec()

# import sys
# import random
# from PySide6 import QtCore, QtWidgets, QtGui

# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)

#         self.button.clicked.connect(self.magic)

#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))
        
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])

#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()

#     sys.exit(app.exec())