# usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Edit
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication

class QandA():

    def __init__(self):
        self.question = ''
        self.answer = ''
        self.con = sqlite3.connect('QandA.db')
        self.cursor = self.con.cursor()
        sql = 'create table if not exists qanda (id integer primary key, problem char(255) not null, answer char(255) not null)'
        self.cursor.execute(sql)
        self.con.commit()

    def send(self, question, answer):
        print('==========')
        print(question)
        print('------')
        print(answer)
        print('------')
        self.question = question
        self.answer = answer
        send_qanda = [self.question, self.answer]
        self.cursor.execute('insert into qanda values(null,?,?)',send_qanda)
        self.con.commit()

        with open('./new.txt', mode='a') as f:
            f.write(self.question)
    def finish(self):
        lines = list()
        with open('./new.txt', mode='r') as f:
            lines.append(f.read())
        with open('./new.txt', mode='w') as f:
            pass
        with open('./all.txt', mode='a') as f:
            for line in lines:
                f.write(line)
        self.con.close()

def new():
    app = QApplication(sys.argv)
    qanda = QandA()
    window = QWidget()
    window.resize(1000, 1000)
    save_button = QPushButton()
    finish_button = QPushButton()
    save_button.setText('next')
    finish_button.setText('Finish')
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
    layout.addWidget(finish_button)
    #"Central Widget" expands to fill all available space
    window.setLayout(layout)


    #Print text to concole whenever it changes
    text_edit_widget.textChanged.connect(
        lambda: print(text_edit_widget.document().toPlainText()))
    answer_edit_widget.textChanged.connect(
        lambda: print(answer_edit_widget.document().toPlainText()))

    # Write text to File whenever it changes
    save_button.clicked.connect(
        lambda: qanda.send(text_edit_widget.document().toPlainText(), answer_edit_widget.document().toPlainText()))

    # Set value of text when push save
    save_button.clicked.connect(
        lambda: text_edit_widget.document().setPlainText("次の問題を入力してください"))
    save_button.clicked.connect(
        lambda: answer_edit_widget.document().setPlainText("回答を入力してください"))
    # Set initial value of text
    text_edit_widget.document().setPlainText("問題を入力してください。")
    answer_edit_widget.document().setPlainText("回答を入力してください")

    window.show()

    finish_button.clicked.connect(
        lambda: qanda.finish())
    finish_button.clicked.connect(
        lambda: QCoreApplication.instance().quit())

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
