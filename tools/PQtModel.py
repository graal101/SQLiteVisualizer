from PyQt6 import QtSql
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel


class PQtSQliteCURD:
    def __init__(self, db_name):
        self.db_name = db_name

    def db_read(self, db_query):
        pass
        
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
        
    def __del__(self):
        pass
        # self.close()
