from PyQt5 import QtWidgets
from design import Ui_MainWindow
import sys
from decimal import Decimal

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._operand_1 = '0'
        self._operand_2 = '0'
        self.operation = '+'
        self.ui.pushButton_1.clicked.connect(self.add_number)
        self.ui.pushButton_2.clicked.connect(self.add_number)
        self.ui.pushButton_3.clicked.connect(self.add_number)
        self.ui.pushButton_4.clicked.connect(self.add_number)
        self.ui.pushButton_5.clicked.connect(self.add_number)
        self.ui.pushButton_6.clicked.connect(self.add_number)
        self.ui.pushButton_7.clicked.connect(self.add_number)
        self.ui.pushButton_8.clicked.connect(self.add_number)
        self.ui.pushButton_9.clicked.connect(self.add_number)
        self.ui.pushButton_0.clicked.connect(self.add_number)
        self.ui.pushButton_dot.clicked.connect(self.add_number)
        self.ui.pushButton_plus.clicked.connect(self.apply_operation)
        self.ui.pushButton_minus.clicked.connect(self.apply_operation)
        self.ui.pushButton_multiply.clicked.connect(self.apply_operation)
        self.ui.pushButton_division.clicked.connect(self.apply_operation)
        self.ui.pushButton_equals.clicked.connect(self.equals)

    @property
    def operand_1(self):
        return self._operand_1

    @operand_1.setter
    def operand_1(self, value):
        if value.startswith('0') and not value.startswith('0.') and len(value) > 1:
            value = value[1:]
        if value.endswith('.0'):
            value = value[:-2]
        if len(value) > 10:
            value = value[:10]
        self._operand_1 = value
        self.ui.lcdNumber.display(value)

    def add_number(self):
        sender = self.sender()
        self.operand_1 = self.operand_1 + sender.text()

    def apply_operation(self):
        sender = self.sender()
        self._operand_2 = self.operand_1
        self.operand_1 = '0'
        self.operation = sender.text()

    def equals(self):
        if self.operation == '+':
            self.operand_1 = str(Decimal(self._operand_1) + Decimal(self._operand_2))
        if self.operation == '*':
            self.operand_1 = str(Decimal(self._operand_1) * Decimal(self._operand_2))
        if self.operation == '/':
            self.operand_1 = str(Decimal(self._operand_1) / Decimal(self._operand_2))



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())