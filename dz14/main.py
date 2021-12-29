import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
from rev import Ui_MainWindow  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self):
      super().__init__()
      self.setupUi(self)  # Это нужно для инициализации нашего дизайна
      self.vv = Ui_MainWindow()
      self.pushButton.clicked.connect(self.click_reverse)


   def click_reverse(self):
      mytext= self.textEdit.toPlainText()
      self.textEdit_2.setText(str(float(mytext)*1.2))



app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = ExampleApp()  # Создаём объект класса ExampleApp
window.show()  # Показываем окно
app.exec_()  # и запускаем приложение




