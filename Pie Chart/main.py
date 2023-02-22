from PySide6.QtWidgets import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from qchart import Ui_MainWindow
from PySide6 import QtCharts
from PySide6.QtGui import QPainter, QFont

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        #Tittle fontunu bu alandan ayarlarını sağladık.
        font = QFont()
        font.setPixelSize(50)
        font.setPointSize(50)
        titleFont = QFont('Times', 20)

        """
        Bu alanda series yapısı olarak QpieSeries olarak belirledik yani grafik türünü
        Animasyon ayarlarını bu alandan yaptık.
        self.series2.setHoleSize(0.3) bunu kaldırırsanız ortasında delik olmayan bir piechart elde edersiniz.
        """
        self.series2 = QPieSeries()
        self.series2.setHoleSize(0.3)
        self.chart2 = QChart()
        self.chart2.addSeries(self.series2)
        self.chart2.createDefaultAxes()
        self.chart2.setAnimationOptions(QChart.SeriesAnimations)
        self.chart2.legend().hide()
        self.chart2.setFont(titleFont)
        self.chart2.setTitleFont(titleFont)
        self.chart2.legend().setVisible(True)
        self.chart2.legend().setAlignment(Qt.AlignTop)
        self.chart2.zValue()
        self.chart2.setVisible(True)
        self.chart2.setTitle("Kış Ayı Meyve Pazar Büyüklüğü Analizi")
        self.chartview2 = QChartView(self.chart2)
        self.chartview2.setRenderHint(QPainter.Antialiasing)

        self.grafik()


    def grafik(self):
        self.series2.clear()
        # clear deme sebebimiz yenileme sağlarsanız kod üzerinde diğer bir önceki grafik silinir ve yeni güncel olan gelir

        #grafiğe eleman ekleme işlemi.

        portakal=self.series2.append(f"Portakal:50",int(50))
        portakal.setLabelFont(QFont("Times", 7))

        mandalina=self.series2.append(f"Mandalina:30",int(30))
        mandalina.setLabelFont(QFont("Times", 7))

        nar=self.series2.append(f"Nar:15",int(15))
        nar.setLabelFont(QFont("Times", 7))

        elma=self.series2.append(f"Elma:15",int(15))
        elma.setLabelFont(QFont("Times", 7))


        deneme = self.ui.gridLayout.addWidget(self.chartview2)





app=QApplication([])
window=MainPage()
window.show()
app.exec()