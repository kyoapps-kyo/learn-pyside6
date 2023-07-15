
import time
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

## 异步 多线程的子类化
class WorkThread(QObject):
    # 1. 自定义信号
    signal = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        print('run')
    
    def fn(self):
        for i in range(10):
            # 2. 信号的手动触发
            self.signal.emit(str(i))
            print(i)
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.lb = QLabel(f'当前值为：{self.value}')

        self.workThread = WorkThread()
        self.threadList = QThread()
        self.workThread.moveToThread(self.threadList)
        self.threadList.started.connect(self.workThread.fn)
        self.threadList.start()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)

    def threadFinish(self):
        self.lb.setText('线程执行完成')
        self.workThread.deleteLater()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()    