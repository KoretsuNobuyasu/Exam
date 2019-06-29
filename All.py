# usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Edit
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication

class QandA():

    def __init__(self):

        self.data = list()
        self.con = sqlite3.connect('QandA.db')
        self.cursor = self.con.cursor()
        for row in self.cursor.execute("select * from qanda"):
            print(row[0], self.number)
            print(type(row[0]), type(self.number))
            if(row[0] == self.number):
                self.question = row[1]
                self.answer = row[2]
            else:
                pass
    def save(self, question, answer):
        self.question = question
        self.answer = answer
        send_q = [self.question, self.number]
        send_a = [self.answer, self.number]
        self.cursor.execute('update qanda set problem=? where id=?',send_q)
        self.cursor.execute('update qanda set answer=? where id=?',send_a)
        self.con.commit()

def all():
    app = QApplication(sys.argv)
    #qanda = QandA()
    window = QWidget()
    window.resize(1000, 1000)
    edit_button = QPushButton()
    finish_button = QPushButton()
    finish_button.setText('Finish')
    #Create text entry box
    text_edit_widget = QPlainTextEdit()
    #Change font, color of text entry box
    text_edit_widget.setStyleSheet(
    """QPlainTextEdit {background-color:#333;
            color: #00FF00;
            text-decoration: underline;
            font-family: Courier;}""")
    layout = QVBoxLayout()
    layout.addWidget(text_edit_widget)

    layout.addWidget(finish_button)
    #"Central Widget" expands to fill all available space
    window.setLayout(layout)

    # Set initial value of text
    con = sqlite3.connect('QandA.db')
    c = con.cursor()
    question_list = ''
    for row in c.execute("select * from qanda"):
        question_list = question_list + row[1] + '\t' + row[2] + '\n\n'
    text_edit_widget.document().setPlainText(question_list)
    finish_button.clicked.connect(
        lambda: QCoreApplication.instance().quit())
    window.show()
    sys.exit(app.exec_())
