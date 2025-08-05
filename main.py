#!/usr/bin/env python3
"""Приложение для просмотра sqlite3 таблиц."""
import sys

from Dialogs.dialogs import message, FileDialog

from PyQt6 import QtWidgets, uic

from tools.table_kit import SQLiteCRUD as sql3

class MyApp(QtWidgets.QMainWindow):
    """Класс приложения."""

    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('ui/main_window.ui', self)

        # Здесь сигналы и слоты
        self.mn_open.triggered.connect(self.mn_open_file)  # Открыть файл БД
        self.mn_quit.triggered.connect(self.mn_exit)  # Выход
        self.mn_font.triggered.connect(self.mn_font_choose)  # Выбор шрифта, размера шрифта
        
    def mn_open_file(self):
        d = FileDialog()
        sdb = sql3(d.open_file_dialog())
        # print(sdb.read())
        
    def mn_font_choose(self):
        d = FileDialog()
        fsize = d.font_dialog()
        if fsize:
            self.menubar.setFont(fsize)  # for test

    def mn_exit(self):
        # Действие при нажатии кнопки
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
