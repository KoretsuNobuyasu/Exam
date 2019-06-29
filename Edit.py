# usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Edit
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication

class QandA():

    def __init__(self,number):
        self.number = int(number)
        self.data = list()
        self.con = sqlite3.connect('QandA.db')
        self.cursor = self.con.cursor()
        #self.c.execute("select * from qanda where *")
        for row in self.cursor.execute("select * from qanda"):
            print(row[0], self.number)
            print(type(row[0]), type(self.number))
            if(row[0] == self.number):
                self.question = row[1]
                self.answer = row[2]
            else:
                pass
    def save(self, question, answer):
        print('==========')
        print(question)
        print('------')
        print(answer)
        print('------')
        self.question = question
        self.answer = answer
        send_q = [self.question, self.number]
        send_a = [self.answer, self.number]
        self.cursor.execute('update qanda set problem=? where id=?',send_q)
        self.cursor.execute('update qanda set answer=? where id=?',send_a)
        self.con.commit()

def edit():
    con = sqlite3.connect('QandA.db')
    c = con.cursor()
    for row in c.execute("select * from qanda"):
        print(row)
    number = input('編集したい番号を入力してください>>>')
    if(number.isdigit()):
        app = QApplication(sys.argv)
        qanda = QandA(number)
        window = QWidget()
        window.resize(1000, 1000)
        save_button = QPushButton()
        edit_button = QPushButton()
        finish_button = QPushButton()
        save_button.setText('save')
        #Create text entry box
        text_edit_widget = QPlainTextEdit()
        answer_edit_widget = QPlainTextEdit()

        #Change font, color of text entry box
        text_edit_widget.setStyleSheet(
        """QPlainTextEdit {background-color:#333;
                color: #00FF00;
                text-decoration: underline;
                font-family: Courier;}""")
        answer_edit_widget.setStyleSheet(
        """QPlainTextEdit {background-color:#333;
                color: #00FF00;
                text-decoration: underline;
                font-family: Courier;}""")

        layout = QVBoxLayout()
        layout.addWidget(text_edit_widget)
        layout.addWidget(answer_edit_widget)
        layout.addWidget(save_button)
        #"Central Widget" expands to fill all available space
        window.setLayout(layout)


        #Print text to concole whenever it changes
        text_edit_widget.textChanged.connect(
            lambda: print(text_edit_widget.document().toPlainText()))

        # Set initial value of text
        text_edit_widget.document().setPlainText(qanda.question)
        answer_edit_widget.document().setPlainText(qanda.answer)

        # Write text to File whenever it changes
        save_button.clicked.connect(
            lambda: qanda.save(text_edit_widget.document().toPlainText(), answer_edit_widget.document().toPlainText()))
        save_button.clicked.connect(
            lambda: QCoreApplication.instance().quit())


        window.show()


        sys.exit(app.exec_())
    else:
        print('数値を入力してください')
        sys.exit()
