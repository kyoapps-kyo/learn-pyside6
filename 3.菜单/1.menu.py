from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QStyle
from PySide6.QtGui import QAction
from Ui_untitled import Ui_Menu

class MyMainWindow(QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        # 1 通过ui工具创建
        # self.setupUi(self)

        # 2 手动创建
        self.menu = self.menuBar()

        self.openFile = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon), '打开窗口')
        self.closeFile = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirClosedIcon), '关闭窗口')

        self.fileMenu = QMenu('File')
        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.closeFile)

        self.menu.addMenu(self.fileMenu)

        # QMainWindow的signals and slot
        # self.actionOpen_1.triggered.connect( lambda: print('open'))
        # self.actionExit_1.triggered.connect( lambda: self.close())

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec() 