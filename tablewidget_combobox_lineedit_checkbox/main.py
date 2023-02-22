from PySide6.QtWidgets import *
from PySide6.QtCore import *
from tablewidget_combobox_lineedit_checkbox import Ui_MainWindow
from PySide6 import QtCore
import pandas as pd
from PySide6 import QtWidgets


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ModernTableWidget()



        delegate = AlignDelegate(self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegate(delegate)

    def ModernTableWidget(self):


        data=pd.read_excel(r"pazarfiyatlari.xlsx")
        df=pd.DataFrame(data).reset_index(drop=True)

        self.ui.tableWidget.setColumnCount(df.shape[1]+3)
        self.ui.tableWidget.setRowCount(df.shape[0])
        self.ui.tableWidget.setHorizontalHeaderLabels(df.columns.astype(str))


        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        list_values = df.values
        row_index = 0
        for value_tuple in list_values:
            col_index = 0
            for value in value_tuple:
                arztalepcombobox=["Alış","Satış"]

                self.ui.tableWidget.setItem(row_index, col_index,QTableWidgetItem(str(value)))
                self.comboBox = QtWidgets.QComboBox()
                self.comboBox.addItems(arztalepcombobox)
                header=QTableWidgetItem("Arz Talep")

                self.ui.tableWidget.setHorizontalHeaderItem(2,header)
                self.ui.tableWidget.setCellWidget(row_index, 2, self.comboBox)

                self.lineedit = QtWidgets.QLineEdit()
                header2 = QTableWidgetItem("Durum Özeti")
                self.lineedit.setPlaceholderText("Açıklama: ")


                self.ui.tableWidget.setHorizontalHeaderItem(3,header2)
                self.ui.tableWidget.setCellWidget(row_index,3, self.lineedit)

                self.checkbox = QtWidgets.QCheckBox("İşlem")
                self.checkbox.setStyleSheet("padding-left:50px;")


                checkbox_item = QtWidgets.QTableWidgetItem()
                checkbox_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                checkbox_item.setCheckState(QtCore.Qt.Unchecked)

                header3 = QTableWidgetItem('İşlem')

                self.ui.tableWidget.setHorizontalHeaderItem(4,header3)
                self.ui.tableWidget.setCellWidget(row_index,4, self.checkbox)

                col_index += 1
            row_index += 1



# Bu Class table da bulunan itemların ortalanmasını sağlamaktadır.

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter





app=QApplication([])
window=MainPage()
window.show()
app.exec()