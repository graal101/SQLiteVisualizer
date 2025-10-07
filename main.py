#!/usr/bin/env python3
"""Приложение для просмотра sqlite3 таблиц."""
import sys

from Dialogs.dialogs import message, FileDialog

from tools.PQtModel import PQtSQliteCURD as Pqt
from PyQt6 import QtSql
from PyQt6 import QtWidgets, uic
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel


class Confdb():
    """Параметры БД
       :table_db_name: Имя таблицы.
       :db_name: Путь до БД.
    """
    table_db_name = ''
    db_name = ''
    table_template = "SELECT name FROM sqlite_master WHERE type='table';"
    add_template = "INSERT INTO table_name (name, age) VALUES ('Noname', 00);"
    del_template = "DELETE FROM table_name WHERE id = ?"
    

class MyApp(QtWidgets.QMainWindow):
    """Класс приложения."""

    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('ui/main_window.ui', self)

        # Здесь сигналы и слоты
        self.mn_open.triggered.connect(self.mn_open_file)  # Открыть файл БД
        self.mn_quit.triggered.connect(self.mn_exit)  # Выход
        self.mn_font.triggered.connect(self.mn_font_choose)  # Выбор шрифта, размера шрифта
        self.mn_alltables.triggered.connect(self.mn_allTables_set)  # Обзор всех таблиц в базе.
        self.mn_addrecord.triggered.connect(self.mn_addrecord_set)  # 
        self.mn_deleterecord.triggered.connect(self.mn_deleterecord_set)
        self.btn_search.clicked.connect(self.fetch_data)  # Запрос к БД из строки
        
    def mn_addrecord_set(self):
        if not Confdb.db_name:
            message('', 'Ошибка', 'Не загружена БД!', ico=2)
            return
        try:
            self.lineEdit.setText(f'{Confdb.add_template}')
        except:
            message('', 'Ошибка', 'Запись в БД!', ico=2)
            
    def mn_deleterecord_set(self):
        if not Confdb.db_name:
            message('', 'Ошибка', 'Не загружена БД!', ico=2)
            return
        try:
            self.lineEdit.setText(f'{Confdb.del_template}')
        except:
            message('', 'Ошибка', 'Запись в БД!', ico=2)
        
    def mn_allTables_set(self):
        """Обзор всех таблиц в базе."""
        if not Confdb.db_name:
            message('', 'Ошибка', 'Не загружена БД!', ico=2)
            return
        qq = Pqt(Confdb.db_name)
        self.tableView.setModel(qq.db_read(Confdb.table_template))

    def mn_open_file(self):
        """Открытие базы данных с заполнением таблицы."""
        flopen = FileDialog()
        result = ''
        file_name = flopen.open_file_dialog()
        Confdb.db_name = file_name
        if file_name == None:
            return
        db_connect = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db_connect.setDatabaseName(file_name)
        db_connect.open()
        query = QSqlQuery()
        if query.exec("SELECT name FROM sqlite_master WHERE type='table';"):
            if query.next():
                Confdb.table_db_name = query.value(0)
        else:
            return

        query.exec(f'SELECT * FROM {Confdb.table_db_name}')
        query.last()
        model = QtSql.QSqlQueryModel()
        model.setQuery(query)
        self.tableView.setModel(model)
        db_connect.close()
        self.lineEdit.setText(f'SELECT * FROM {Confdb.table_db_name}') 
        self.statusbar.showMessage('Загружен: ' + file_name)
        
    def fetch_data(self):
        """Запрос в БД из lineEdit."""
        if not Confdb.db_name:
            message('', 'Ошибка', 'Не загружена БД!', ico=2)
            return
        str_query = self.lineEdit.text()
        if str_query == '':
            message('', 'Ошибка', 'Пустая строка запроса к БД!', ico=2)
            return
        qq = Pqt(Confdb.db_name)
        self.tableView.setModel(qq.db_read(str_query))

    def mn_font_choose(self):
        font_open = FileDialog()
        fsize = font_open.font_dialog()
        if fsize:
            self.tableView.setFont(fsize)

    def mn_exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
