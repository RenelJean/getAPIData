import sys

from PyQt5.QtWidgets import QListWidget, QApplication, QVBoxLayout, QDialog, QLabel
from PySide6.examples.widgets.dialogs.findfiles.findfiles import Window


class GUI(QDialog):
    def __init__(self):
        super().__init__()
        self.label = None
        self.user_list = QListWidget()
        self.title = "GUI"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.user_list.insertItem(0,"KYle")
        self.user_list.insertItem(1,"Bobo")
        self.user_list.insertItem(2,"John")
        self.user_list.insertItem(3,"Dad")

        self.user_list.clicked.connect(self.list_clicked)

        self.label = QLabel()
        vbox.addWidget(self.label)

        vbox.addWidget(self.user_list)
        self.setLayout(vbox)

        self.show()

    def list_clicked(self):
        item = self.user_list.currentItem()
        self.label.setText(str(item.text()))


app = QApplication(sys.argv)
window = GUI()
sys.exit(app.exec())

