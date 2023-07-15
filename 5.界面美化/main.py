########################################################
# 常用QSS主题库 qt_material \ Qtmodern \ QDarkStyleSheet \ PyQtDarkTheme
#   qt_material https://github.com/UN-GCPDS/qt-material
#   Qtmodern  https://github.com/gmarull/qtmodern
#   QDarkStyleSheet https://github.com/ColinDuquesnoy/QDarkStyleSheet
#   PyQtDarkTheme https://github.com/5yutan5/PyQtDarkTheme
#
# 隐藏系统标题栏，实现自定义窗体 详细跳转到鼠标事件
#   去除系统标题栏 self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
#   窗体最小化 self.showMinimized
#
# 预设模板 PyDracula https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6
#   常用操作：
#       对界面进行修改
#       新建页面
#       控件信号绑定
#       侧边栏修改
#       更改明暗主题
#   文件
#        main.py主文件
#        main.ui负责修改界面
#        resources.qrc资源文件清单
#        在modules中
#        app_functions.py是后期添加函数的文件
#        resources_rc.py是生成的rc文件
#        ui_main.py是生成的界面文件
########################################################

from PySide6.QtWidgets import QApplication, QWidget
from qt_material import apply_stylesheet
from Ui_untitled import Ui_Form

class MyMainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()

    apply_stylesheet(app, theme='dark_teal.xml')

    window.show()
    app.exec() 