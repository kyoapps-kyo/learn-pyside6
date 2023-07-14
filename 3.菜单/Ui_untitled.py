# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QWidget)

class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(800, 600)
        self.actionOpen = QAction(Menu)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(Menu)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpen_1 = QAction(Menu)
        self.actionOpen_1.setObjectName(u"actionOpen_1")
        self.actionExit_1 = QAction(Menu)
        self.actionExit_1.setObjectName(u"actionExit_1")
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Menu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        Menu.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_1)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_1)

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("Menu", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("Menu", u"Exit", None))
        self.actionOpen_1.setText(QCoreApplication.translate("Menu", u"Open", None))
        self.actionExit_1.setText(QCoreApplication.translate("Menu", u"Exit", None))
        self.menuFile.setTitle(QCoreApplication.translate("Menu", u"File", None))
    # retranslateUi

