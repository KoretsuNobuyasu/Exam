# usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget


class QandA():

    def __init__(self):
        self.question = ''
        self.answer = ''

    def send_question(self, question_text):
        self.question = question_text
        with open('./new.txt', mode='w') as f:
            f.write(self.question)

    def send_answer(self, answer_text):
        self.answer = answer_text


def main():
    app = QApplication(sys.argv)
    qanda = QandA()
    window = QWidget()
    window.resize(1000, 1000)
    save_button = QPushButton()
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

    # Write text to File whenever it changes
    save_button.clicked.connect(
        lambda: qanda.send_question(text_edit_widget.document().toPlainText()))
    save_button.clicked.connect(
        lambda: text_edit_widget.document().setPlainText("次の問題を入力してください"))

    # Set initial value of text
    text_edit_widget.document().setPlainText("問題と解答を入力してください。splitは¥マークです。")

    window.show()

    # Start event loop
    sys.exit(app.exec_())


def write_file(object):
    with open('./new.txt', mode='w') as f:
        f.write(object)

if __name__ == '__main__':
    main()
