
from PySide6.QtWidgets import *
from slide_menu import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtCore import *


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.menubutton.clicked.connect(self.slide_menu)

    def slide_menu(self):
        width = self.ui.leftmenuwidget.width()
        # 91 olarak seçme sebebimiz desinger dan maks büyüklük ve küçüklüğü 91 yapmış olmamız.
        if width == 91:
            # left_menu de büyütmek istediğiniz boyu bu alandan belirleyebilirisiniz.
            newWidth = 180

        else:
            newWidth = 91

        self.animation = QPropertyAnimation(self.ui.leftmenuwidget, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


app=QApplication([])
window=MainPage()
window.showMaximized()
app.exec()