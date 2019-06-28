# usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from time import sleep
import Edit, New
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QDialog
from PyQt5.QtCore import QCoreApplication


def main(argv):

    option = argv[0]
    if option == '--help':
        help = """
                終了ボタンから終了した場合は正常に終了できません。
                --new     新たなデータを入力できます
                --edit    データを更新できます
        """
        print(help)
    elif option == '--new':
        New.new()
    elif option == '--edit':
        Edit.edit()
    else:
        print('やり直してください')

if __name__ == '__main__':
    print('コマンドラインで操作を入力してください')
    print('--helpでコマンド一覧を見ることができます')
    main(sys.argv[1:])
