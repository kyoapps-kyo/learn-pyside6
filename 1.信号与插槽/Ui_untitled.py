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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLCDNumber,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_computer(object):
    def setupUi(self, computer):
        if not computer.objectName():
            computer.setObjectName(u"computer")
        computer.resize(592, 558)
        self.gridLayoutWidget = QWidget(computer)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 130, 411, 331))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.horizontalLayoutWidget = QWidget(computer)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 470, 411, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_0 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_0)

        self.pushButton_plus = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        sizePolicy.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_plus)

        self.pushButton_minus = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_minus)

        self.pushButton_multiply = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        sizePolicy.setHeightForWidth(self.pushButton_multiply.sizePolicy().hasHeightForWidth())
        self.pushButton_multiply.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_multiply)

        self.verticalLayoutWidget = QWidget(computer)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(430, 130, 151, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_del = QPushButton(self.verticalLayoutWidget)
        self.pushButton_del.setObjectName(u"pushButton_del")
        sizePolicy.setHeightForWidth(self.pushButton_del.sizePolicy().hasHeightForWidth())
        self.pushButton_del.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_del)

        self.pushButton_clear = QPushButton(self.verticalLayoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_clear)

        self.pushButton_division = QPushButton(self.verticalLayoutWidget)
        self.pushButton_division.setObjectName(u"pushButton_division")
        sizePolicy.setHeightForWidth(self.pushButton_division.sizePolicy().hasHeightForWidth())
        self.pushButton_division.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_division)

        self.pushButton_point = QPushButton(self.verticalLayoutWidget)
        self.pushButton_point.setObjectName(u"pushButton_point")
        sizePolicy.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_point)

        self.pushButton_enter = QPushButton(self.verticalLayoutWidget)
        self.pushButton_enter.setObjectName(u"pushButton_enter")
        sizePolicy.setHeightForWidth(self.pushButton_enter.sizePolicy().hasHeightForWidth())
        self.pushButton_enter.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_enter)

        self.layoutWidget = QWidget(computer)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 571, 111))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lcdNumber = QLCDNumber(self.layoutWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(150, 0))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setProperty("value", 0.000000000000000)

        self.horizontalLayout.addWidget(self.lcdNumber)


        self.retranslateUi(computer)

        QMetaObject.connectSlotsByName(computer)
    # setupUi

    def retranslateUi(self, computer):
        computer.setWindowTitle(QCoreApplication.translate("computer", u"Form", None))
        self.pushButton_9.setText(QCoreApplication.translate("computer", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("computer", u"6", None))
        self.pushButton_8.setText(QCoreApplication.translate("computer", u"8", None))
        self.pushButton_4.setText(QCoreApplication.translate("computer", u"4", None))
        self.pushButton_7.setText(QCoreApplication.translate("computer", u"7", None))
        self.pushButton_5.setText(QCoreApplication.translate("computer", u"5", None))
        self.pushButton_1.setText(QCoreApplication.translate("computer", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("computer", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("computer", u"3", None))
        self.pushButton_0.setText(QCoreApplication.translate("computer", u"0", None))
        self.pushButton_plus.setText(QCoreApplication.translate("computer", u"+", None))
        self.pushButton_minus.setText(QCoreApplication.translate("computer", u"-", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("computer", u"*", None))
        self.pushButton_del.setText(QCoreApplication.translate("computer", u"Del", None))
        self.pushButton_clear.setText(QCoreApplication.translate("computer", u"Clear", None))
        self.pushButton_division.setText(QCoreApplication.translate("computer", u"/", None))
        self.pushButton_point.setText(QCoreApplication.translate("computer", u".", None))
        self.pushButton_enter.setText(QCoreApplication.translate("computer", u"Enter", None))
        self.lineEdit.setText("")
    # retranslateUi

