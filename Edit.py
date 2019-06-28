# usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import Edit
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication

class QandA():

    def __init__(self):
        lines = list()
        with open('./all.txt', mode="r") as f:
            lines.append(f.read())
        line = lines[0]
        line = line.replace('\n', '\n\n')
        with open('./all.txt', mode='w') as f:
            pass
        self.data = line


    def save(self, text):
        self.data = text
        with open('./all.txt', mode='w') as f:
            f.write(self.data)


def edit():
    app = QApplication(sys.argv)
    qanda = QandA()
    window = QWidget()
    window.resize(1000, 1000)
    save_button = QPushButton()
    edit_button = QPushButton()
    finish_button = QPushButton()
    save_button.setText('save')
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
    layout.addWidget(save_button)
    #"Central Widget" expands to fill all available space
    window.setLayout(layout)


    #Print text to concole whenever it changes
    text_edit_widget.textChanged.connect(
        lambda: print(text_edit_widget.document().toPlainText()))

    # Set initial value of text
    text_edit_widget.document().setPlainText(qanda.data)

    # Write text to File whenever it changes
    save_button.clicked.connect(
        lambda: qanda.save(text_edit_widget.document().toPlainText()))
    save_button.clicked.connect(
        lambda: QCoreApplication.instance().quit())


    window.show()


    sys.exit(app.exec_())
