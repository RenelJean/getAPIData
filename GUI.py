import sys
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtWidgets
import PyQt5
from qtpy import QtCore
import db


# connect to db





class MainWindow(QDialog):

    def __init__(self):
        labels = [
            "First Name", "Prefix", "Position", "Last Name", "Organization", "Email",
        ]
        super(MainWindow, self).__init__()
        loadUi("CubeFormData.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("cubesProject.sqlite")
        cursor = conn.cursor()
        sql_query = "SELECT * FROM WuFooData"

        self.tableWidget.setRowCount(11)
        table_row = 0

        for row in cursor.execute(sql_query):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[2]))

            table_row += 1
            print(row)
        print("Ok")

app = QApplication(sys.argv)
main_screen = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_screen)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()

try:
    sys.exit(app.exec_())

except:
    print("Exiting")
