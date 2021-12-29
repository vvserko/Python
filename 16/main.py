from PyQt5 import QtWidgets, QtGui
from main_design import Ui_MainWindow
from add_design import Ui_Dialog
from task import Task

import sys
# Задача
# - приоритет
# - дедлайн (выводить сколько времени осталось)
# - текстid


class Dialog_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.comboBox.addItems(['height', 'medium', 'low'])


class Main_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tasks = []
        self.pushButton.clicked.connect(self.click)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['text', 'priority', 'date', 'left'])
        # self.tableWidget.resizeColumnsToContents()

    def add_task_to_table(self, task: Task):
        row = len(self.tasks)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(task.text))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(task.priority))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(task.dead_line)))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(task.left)))

    def click(self):
        window = Dialog_Window()
        if window.exec():
            text = window.textEdit.toPlainText()
            dead_line = window.dateTimeEdit.dateTime().toPyDateTime()
            priority = window.comboBox.currentText()
            task = Task(text, dead_line, priority)
            self.tasks.append(task)
            self.add_task_to_table(task)
        else:
            print('no')



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_Window()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
