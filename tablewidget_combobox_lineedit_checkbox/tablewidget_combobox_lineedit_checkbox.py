# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tablewidget_combobox_lineedit_checkbox.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QMainWindow, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setBold(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget::item {\n"
"    color: \"black\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QHeaderView::section{Background-color: rgb(2, 65, 102);;\n"
"color:\"white\";\n"
"}\n"
"\n"
"text-align: center; \n"
"")
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

