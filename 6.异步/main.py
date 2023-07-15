################################################################
# QtCore QTimer
# self.timer = QTimer
# self.timer.timeout.connect()
# self.timer.start(100)
# QTimer.singleShot(1000, lambda: print('一秒钟到了'))
# QTimer.start() 开始定时器
# QTimer.stop() 停止计时器
# QTimer.setSingleShot() 设置定时器是否为单次触发
# QTimer.setInterval(int) 设置定时器的间隔如果没有设置则默认为1000ms)
#
# QApplication.processEvent()
#
# QtCore -> QThread, Signal
################################################################

import time
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

## 异步 多线程的子类化
class WorkThread(QThread):
    # 1. 自定义信号
    signal = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        print('run')
    
    def run(self):
        for i in range(10):
            # 2. 信号的手动触发
            self.signal.emit(str(i))
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.lb = QLabel(f'当前值为：{self.value}')

        # 3. 主线程创建线程实例
        self.workThread = WorkThread()
        # 4. 主线程对子线程的信号进行绑定，signal是自定义的，对应的是子线程中的signal
        self.workThread.signal.connect(lambda x: self.lb.setText(f'当前值为{x}'))
        # x 的值是由工作线程发出的信号传递给槽函数时传入的。具体来说，工作线程在某个地方使用 emit(signal) 的方式发出信号，并将一个值作为参数传递给信号。然后，这个值会被传递到与该信号连接的槽函数中，即 lambda 表达式中的 self.lb.setText(f'当前值为{x}')，从而更新标签的文本内容。
        self.workThread.started.connect(lambda: print('start'))
        self.workThread.finished.connect(self.threadFinish)
        # 5. 开始子线程
        self.workThread.start()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.setLayout(self.mainLayout)

    def threadFinish(self):
        self.lb.setText('线程执行完成')
        # 删除
        self.workThread.deleteLater()
        # 阻塞 self.workThread.wait()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()    