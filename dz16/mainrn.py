import run
import  random
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> object:
        super().__init__()
        self.ui = run.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click)
        self.vv = QtWidgets.QApplication.desktop()

        self.x = self.vv.availableGeometry().x() + random.randint(0, 1)
        self.y = self.vv.availableGeometry().y() + random.randint(0, 1)


    def click(self):
        self.ui.pushButton.setGeometry(self.x, self.y, 93, 28)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())