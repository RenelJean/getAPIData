import sys

import CubeApi
import apiData
import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QListWidget,
    QApplication,
    QListWidgetItem,
    QHBoxLayout,
    QVBoxLayout,
    QLayout,
    QGridLayout,
    QPlainTextEdit,
    QLabel,
    QLineEdit,
    QCheckBox,
)

from config import subdomain, formatted, identifier

data_url = "https://" + subdomain + ".wufoo.com/api/v3/forms/" + identifier + "/entries." + formatted


class WuFooEntriesWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.data = CubeApi.get_cubes_data_from_db()
        self.list_control: QListWidget = None
        self.data_window = None
        self.prefix_box: QLineEdit = None
        self.fname_box: QLineEdit = None
        self.lname_box: QLineEdit = None
        self.title_box: QLineEdit = None
        self.org_box: QLineEdit = None
        self.email_box: QLineEdit = None
        self.website_box: QLineEdit = None
        self.project_check: QCheckBox = None
        self.speaker_check: QCheckBox = None
        self.visit_check: QCheckBox = None
        self.shadow_check: QCheckBox = None
        self.internship_check: QCheckBox = None
        self.panel_check: QCheckBox = None
        self.network_even_check: QCheckBox = None
        self.subject: QLineEdit = None
        self.description_box: QPlainTextEdit = None
        self.funding: QLineEdit = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("GUI Demo for Capstone")
        main_layout = QHBoxLayout()
        self.list_control = QListWidget()
        left_pane = QVBoxLayout()
        main_layout.addLayout(left_pane)
        left_pane.addWidget(self.list_control)
        right_pane = self.build_right_pane()
        self.list_control.resize(400, 400)
        self.list_control.currentItemChanged.connect(self.wufoo_entry_selected)
        self.put_data_in_list(self.data)
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.instance().quit)
        left_pane.addWidget(quit_button)
        main_layout.addLayout(right_pane)
        self.setLayout(main_layout)
        self.show()

    def build_right_pane(self) -> QLayout:
        right_pane = QVBoxLayout()
        one_liners_pane = QGridLayout()
        right_pane.addLayout(one_liners_pane)
        one_liners_pane.addWidget(QLabel("Prefix:"), 0, 0)
        self.prefix_box = QLineEdit()
        self.prefix_box.setReadOnly(True)
        one_liners_pane.addWidget(self.prefix_box, 0, 1)
        one_liners_pane.addWidget(QLabel("Name:"), 0, 2)
        self.fname_box = QLineEdit()
        self.fname_box.setReadOnly(True)
        one_liners_pane.addWidget(self.fname_box, 0, 3)
        self.lname_box = QLineEdit()
        self.lname_box.setReadOnly(True)
        one_liners_pane.addWidget(self.lname_box, 0, 4)
        one_liners_pane.addWidget(QLabel("Title:"), 0, 5)
        self.title_box = QLineEdit()
        self.title_box.setReadOnly(True)
        one_liners_pane.addWidget(self.title_box, 0, 6)
        one_liners_pane.addWidget(QLabel("Organization:"), 1, 0)
        self.org_box = QLineEdit()
        self.org_box.setReadOnly(True)
        one_liners_pane.addWidget(self.org_box, 1, 1)
        one_liners_pane.addWidget(QLabel("email and Website:"), 1, 2)
        self.email_box = QLineEdit()
        self.email_box.setReadOnly(True)
        self.website_box = QLineEdit()
        self.website_box.setReadOnly(True)
        one_liners_pane.addWidget(self.email_box, 1, 3)
        one_liners_pane.addWidget(self.website_box, 1, 4)
        self.project_check = QCheckBox("Course Project")
        self.project_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        self.project_check.setFocusPolicy(Qt.NoFocus)  # or keyboard focus
        one_liners_pane.addWidget(self.project_check, 2, 0)
        self.speaker_check = QCheckBox("Guest Speaker")
        self.speaker_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.speaker_check, 2, 1)
        self.visit_check = QCheckBox("Site Visit")
        self.visit_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.visit_check, 2, 5)
        self.shadow_check = QCheckBox("Job Shadow")
        self.shadow_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.shadow_check, 2, 3)
        self.internship_check = QCheckBox("Internship")
        self.internship_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.internship_check, 2, 4)
        self.panel_check = QCheckBox("Career Panel")
        self.panel_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.panel_check, 2, 2)
        self.network_even_check = QCheckBox("Networking Event")
        self.network_even_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.network_even_check, 2, 6)
        one_liners_pane.addWidget(QLabel("Funding:"), 3, 0)
        self.funding = QLineEdit()
        self.funding.setReadOnly(True)
        one_liners_pane.addWidget(self.funding, 3, 1)
        one_liners_pane.addWidget(QLabel("Subject Area:"), 3, 2)
        self.subject = QLineEdit()
        self.subject.setReadOnly(True)
        one_liners_pane.addWidget(self.subject, 3, 3)
        bottom_pane = QHBoxLayout()
        self.description_box = QPlainTextEdit()
        self.description_box.setReadOnly(True)
        self.description_box.resize(200, 400)
        bottom_pane.addWidget(QLabel("Course Project Description:"))
        bottom_pane.addWidget(self.description_box)
        right_pane.addLayout(bottom_pane)
        return right_pane

    def put_data_in_list(self, data_to_add):
        for item in data_to_add:
            display_text = f"{item['first_name']}  {item['last_name']} : {item['org']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
            list_item.setData(1, item)  # lets put the dictionary for later use

    def wufoo_entry_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(1)  # we put the full record in data role 1
        self.prefix_box.setText(selected_data["prefix"])
        self.fname_box.setText(selected_data["first_name"])
        self.lname_box.setText(selected_data["last_name"])
        self.title_box.setText(selected_data["title"])
        self.org_box.setText(selected_data["org"])
        self.email_box.setText(selected_data["email"])
        self.website_box.setText(selected_data["website"])
        self.project_check.setChecked(selected_data["course_project"])
        self.speaker_check.setChecked(selected_data["guest_speaker"])
        self.visit_check.setChecked(selected_data["site_visit"])
        self.shadow_check.setChecked(selected_data["job_shadow"])
        self.internship_check.setChecked(selected_data["internship"])
        self.panel_check.setChecked(selected_data["career_panel"])
        self.network_even_check.setChecked(selected_data["networking_event"])
        self.subject.setText(selected_data["subject_area"])
        self.description_box.setPlainText(selected_data["description"])
        self.funding.setText(selected_data["funding"])


app = QApplication(sys.argv)
main_screen = WuFooEntriesWindow()
main_screen.setup_window()
main_screen.put_data_in_list(CubeApi.get_cubes_data_from_db())
sys.exit(app.exec_())

# import sqlite3
# import sys
# import apiData
#
# from PyQt5.QtWidgets import QListWidget, QApplication, QVBoxLayout, QDialog, QLabel
# from PySide6.examples.widgets.dialogs.findfiles.findfiles import Window
#
# conn = sqlite3.connect("cubesProject.sqlite")
# cursor = conn.cursor()
# sql_query = "SELECT * FROM WuFooData"
# table_data = cursor.execute(sql_query)
#
#
# def load_table(data):
#     user_list = []
#     for users in data:
#         print(users[3])
#         user_list.append(users[3])
#     # print(user_list)
#     return user_list
#
#
# def load_accounts(data):
#     for account in data:
#         print(account[19])
#
#
# load_accounts(table_data)
#
# account_list = load_table(table_data)
# res = apiData.get_api_info()
# print(res)
#
#
# class GUI(QDialog):
#
#     def __init__(self):
#         super().__init__()
#         self.label = None
#         self.user_list = QListWidget()
#         self.title = "GUI"
#         self.left = 500
#         self.top = 200
#         self.width = 1000
#         self.height = 750
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         for users in account_list:
#             self.user_list.insertItem(0, users)
#
#         vbox = QVBoxLayout()
#         # self.user_list.insertItem(0, account_list[0])
#         # self.user_list.insertItem(1, account_list[1])
#         # self.user_list.insertItem(2, account_list[2])
#         # self.user_list.insertItem(3, account_list[3])
#
#         self.user_list.clicked.connect(self.list_clicked)
#
#         self.label = QLabel()
#         vbox.addWidget(self.label)
#
#         vbox.addWidget(self.user_list)
#         self.setLayout(vbox)
#
#         self.show()
#
#     def list_clicked(self):
#         item = self.user_list.currentItem()
#         self.label.setText(str(item.text()))
#
#
# load_table(table_data)
#
# app = QApplication(sys.argv)
# window = GUI()
# sys.exit(app.exec())
