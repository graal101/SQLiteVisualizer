from PyQt6 import QtSql
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel


class PQtSQliteCURD:
    def __init__(self, db_name):
        self.db_name = db_name
        self.__table_name = self.__bd_table_name()
        self.__records_list = []

    def db_read(self, db_query):
        '''Чтение из базы данных.'''
        res = None
        try:
            db_connect = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db_connect.setDatabaseName(self.db_name)
            db_connect.open()
            query = QSqlQuery()
            query.exec(db_query)
            query.last()     
            model = QtSql.QSqlQueryModel()
            model.setQuery(query)
            res = model  
        except:
            print(f'\nОшибка при чтении базы данных[{self.db_name}, {db_query}]\n')
        db_connect.commit()
        db_connect.close()
        return res
        
    def db_update(self):
        print('def db_update(self)')
        
    def db_create(self):
        pass
        
    def db_delete(self):
        pass
        
    """
    def close(self):
        self.connection.close()
    """
    
    def __bd_table_name(self):
        '''Распознование имени таблицы.'''
        db_connect = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db_connect.setDatabaseName(self.db_name)
        db_connect.open()
        query = QSqlQuery()
        if query.exec("SELECT name FROM sqlite_master WHERE type='table';"):
            if query.next():
                val = query.value(0)
                db_connect.close()
                return val
        db_connect.close()
        return None
        
    @property
    def table_name(self):
        return self.__table_name
        
    def __del__(self):
        print('class closed..')
        # self.close()
