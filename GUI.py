import sys
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton
from PyQt5 import QtWidgets
import PyQt5
from os.path import join
from os.path import dirname

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from qtpy import QtCore
import db


# connect to db


def clicked_button():
    print("clicked")


class MainWindow(QDialog):

    def __init__(self):
        labels = [
            "First Name", "Last Name", "Prefix", "Period", "Organization", "Email",
        ]
        check_labels = ["Course Project", "Guest Speaker", "Site Visit", "Job Shadow", "Internship",
                        "Career Panel", "Networking Event"]

        super(MainWindow, self).__init__()
        loadUi("CubeFormData.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setColumnWidth(3, 250)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("cubesProject.sqlite")
        cursor = conn.cursor()
        sql_query = "SELECT * FROM WuFooData"

        self.tableWidget.setRowCount(10)
        table_row = 0

        for row in cursor.execute(sql_query):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[2]))

            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[3]))

            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[4]))

            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[8]))

            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[5]))

            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[6]))

            table_row += 1

         #   print(row)

        print("Ok")


app = QApplication(sys.argv)
main_screen = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_screen)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
b1 = QtWidgets.QPushButton(main_screen)
b1.setText("Create User")
widget.show()

App = QGuiApplication(sys.argv)

url = QUrl(join(dirname(__file__), 'main.qml'))

view = QQuickView()
view.setSource(url)
view.show()
print(view.source())
sys.exit(App.exec_())

try:
    sys.exit(app.exec_())

except:
    print("Exiting")
