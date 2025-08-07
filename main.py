#!/usr/bin/env python3
"""Приложение для просмотра sqlite3 таблиц."""
import sys

from Dialogs.dialogs import message, FileDialog

from PyQt6 import QtSql
from PyQt6 import QtWidgets, uic
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel




class MyApp(QtWidgets.QMainWindow):
    """Класс приложения."""

    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('ui/main_window.ui', self)

        # Здесь сигналы и слоты
        self.mn_open.triggered.connect(self.mn_open_file)  # Открыть файл БД
        self.mn_quit.triggered.connect(self.mn_exit)  # Выход
        self.mn_font.triggered.connect(self.mn_font_choose)  # Выбор шрифта, размера шрифта
        self.btn_search.clicked.connect(self.fetch_data)  # Запрос к БД из строки

    def mn_open_file(self):  # FIX table_kit with PyQt6.QtSql!!!
        """Открытие базы данных с заполнением таблицы."""
        flopen = FileDialog()
        result = ''
        file_name = flopen.open_file_dialog()
        db_connect = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db_connect.setDatabaseName(file_name)
        db_connect.open()
        query = QSqlQuery()
        if query.exec("SELECT name FROM sqlite_master WHERE type='table';"):
            if query.next():
                result = query.value(0)
        else:
            return

        query.exec(f'SELECT * FROM {result}')
        query.last()
        model = QtSql.QSqlQueryModel()
        model.setQuery(query)
        self.tableView.setModel(model)
        db_connect.close()
        self.statusbar.showMessage('Загружен: ' + file_name)
        
    def fetch_data(self):
        """Запрос в БД из lineEdit."""
        str_query = self.lineEdit.text()
        
        

    def mn_font_choose(self):
        font_open = FileDialog()
        fsize = font_open.font_dialog()
        if fsize:
            self.tableView.setFont(fsize)

    def mn_exit(self):
        # Действие при нажатии кнопки
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
