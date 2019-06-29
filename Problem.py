import sqlite3
import sys
import random
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
        self.count = 0
        for row in self.cursor.execute("select * from qanda"):
            self.count = self.count + 1

    def get_problem(self, number):
        self.number = number
        for row in self.cursor.execute("select * from qanda"):
            print(row[0], self.number)
            print(type(row[0]), type(self.number))
            if(row[0] == self.number):
                self.question = row[1]
                print(self.question,'この問題を出力します')
            else:
                pass
    def get_answer(self, number):
        self.number = number
        for row in self.cursor.execute("select * from qanda"):
            print(row[0], self.number)
            print(type(row[0]), type(self.number))
            if(row[0] == self.number):
                self.answer = row[2]
                print(self.answer, 'この答えを出力します')
            else:
                pass

    def finish(self):
        self.con.close()


def start():
    app = QApplication(sys.argv)
    qanda = QandA()
    window = QWidget()
    window.resize(1000, 1000)
    next_button = QPushButton()
    answer_button = QPushButton()
    finish_button = QPushButton()
    answer_button.setText('ans')
    next_button.setText('next')
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
    layout.addWidget(answer_button)
    layout.addWidget(next_button)
    layout.addWidget(finish_button)
    #"Central Widget" expands to fill all available space
    window.setLayout(layout)

    # Set initial value of text
    text_edit_widget.document().setPlainText("nextを押してください")
    # next押されたら、問題の変更と回答を消す必要ありつまりpass??
    next_button.clicked.connect(
        lambda: output_question(qanda, text_edit_widget, answer_edit_widget, answer_button)
    )
    next_button.clicked.connect(
        lambda: answer_edit_widget.document().setPlainText('ansで答えが表示されます'))



    window.show()
    finish_button.clicked.connect(
        lambda: qanda.finish())
    finish_button.clicked.connect(
        lambda: QCoreApplication.instance().quit())

    sys.exit(app.exec_())
def choose(qanda):
    number = random.randint(1, qanda.count)
    return number

def output_question(qanda, text_edit_widget, answer_edit_widget, answer_button):
    print("押されたー",qanda.count)
    number = choose(qanda)
    print(number,"番めの問題が出力されます")
    qanda.get_problem(number)
    text_edit_widget.document().setPlainText(qanda.question)
    answer_button.clicked.connect(
        lambda: output_answer(qanda, number, answer_edit_widget, answer_button))

def output_answer(qanda, number, answer_edit_widget, answer_button):
    print("答えを出力します")
    qanda.get_answer(number)
    answer_edit_widget.document().setPlainText(qanda.answer)
