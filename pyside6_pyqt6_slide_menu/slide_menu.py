# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slide_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)
import menubutton_rc
import backbutton_rc
import select_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1219, 774)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.leftmenuwidget = QWidget(self.centralwidget)
        self.leftmenuwidget.setObjectName(u"leftmenuwidget")
        self.leftmenuwidget.setMinimumSize(QSize(91, 0))
        self.leftmenuwidget.setMaximumSize(QSize(91, 16777215))
        font = QFont()
        font.setPointSize(8)
        self.leftmenuwidget.setFont(font)
        self.leftmenuwidget.setStyleSheet(u"QWidget#leftmenuwidget{\n"
"\n"
"	background-color: rgb(203, 20, 41);\n"
"\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.leftmenuwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menu2 = QPushButton(self.leftmenuwidget)
        self.menu2.setObjectName(u"menu2")
        self.menu2.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.menu2.setFont(font1)
        self.menu2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"")
        icon = QIcon()
        icon.addFile(u":/select/selectbutton.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menu2.setIcon(icon)
        self.menu2.setIconSize(QSize(60, 60))
        self.menu2.setFlat(True)

        self.gridLayout.addWidget(self.menu2, 1, 0, 1, 1)

        self.backbutton = QPushButton(self.leftmenuwidget)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setMinimumSize(QSize(0, 50))
        self.backbutton.setFont(font1)
        self.backbutton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/backbutton/backbutton.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.backbutton.setIcon(icon1)
        self.backbutton.setIconSize(QSize(60, 60))
        self.backbutton.setAutoDefault(False)
        self.backbutton.setFlat(True)

        self.gridLayout.addWidget(self.backbutton, 3, 0, 1, 1)

        self.menu1 = QPushButton(self.leftmenuwidget)
        self.menu1.setObjectName(u"menu1")
        self.menu1.setMinimumSize(QSize(0, 50))
        self.menu1.setFont(font1)
        self.menu1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"")
        self.menu1.setIcon(icon)
        self.menu1.setIconSize(QSize(60, 60))
        self.menu1.setFlat(True)

        self.gridLayout.addWidget(self.menu1, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.leftmenuwidget, 0, 0, 2, 1)

        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setMinimumSize(QSize(0, 71))
        self.gridWidget.setMaximumSize(QSize(16777215, 71))
        self.gridWidget.setStyleSheet(u"QWidget#gridWidget{\n"
"border:3px solid rgb(203, 20, 41);\n"
"border-radius:25px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.gridWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.gridWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(203, 20, 41);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.menubutton = QPushButton(self.gridWidget)
        self.menubutton.setObjectName(u"menubutton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menubutton.sizePolicy().hasHeightForWidth())
        self.menubutton.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        self.menubutton.setFont(font3)
        self.menubutton.setStyleSheet(u"\n"
"#menubutton{\n"
"text-align: left;\n"
"	color: rgb(203, 20, 41);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/menubutton/menubutton.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menubutton.setIcon(icon2)
        self.menubutton.setIconSize(QSize(60, 60))
        self.menubutton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.menubutton)


        self.gridLayout_2.addWidget(self.gridWidget, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.backbutton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Slide Menu", None))
        self.menu2.setText(QCoreApplication.translate("MainWindow", u"Menu 2", None))
        self.backbutton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.menu1.setText(QCoreApplication.translate("MainWindow", u"Menu 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                         Slide Menu", None))
        self.menubutton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

