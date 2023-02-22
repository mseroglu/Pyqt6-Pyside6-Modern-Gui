import time

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qthread import  Ui_MainWindow


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.donmadanislem)

    def donmadanislem(self):
        text=self.ui.lineEdit.text()

        # gui içerisinde ki lineedit den gelen bilgiyi o class göndermek için text kısmını da belirttik.
        self.threadbaslat=Threadyapanclass(text=text)
        self.threadbaslat.start()


"""
Bu class arka plan da görev yapıcak class,
Anlamanız için aslında mantığını bu class ram de ayrı bir yer de çalışacak ve programımız da donma yaratmiyacak. 
Ana class da donmadan islem diye bir fonskiyon oluşturdum ihtiyacım olduğu zaman Threadyapanclass'ını devreye sokan komut yazdım.(Button'a basıldığı zaman devreye girecek bu thread classı)

Neler yapılabilir örnek olarak ,
Kullanıcdan aldığınız bilgileri bu thread classı ile ekleyebilirisiniz,
Bir uygulama başlatabilirsiniz.
Döngü kurabilirsiniz.
"""
class Threadyapanclass(QThread):
    def __init__(self,text):
        super(Threadyapanclass, self).__init__()
        self.text=text
    def run(self):
        while True:
            print(self.text)
            time.sleep(1)

app=QApplication([])
window=MainPage()
window.show()
app.exec()