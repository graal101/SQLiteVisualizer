import sqlite3

class SQLiteCRUD:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.__table_name = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()[0][0] 

    def create_table(self, table_name, columns):
        columns_with_types = ', '.join([f"{col} {typ}" for col, typ in columns.items()])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})")
        self.connection.commit()

    def insert(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(data))
        self.connection.commit()

    def read(self, conditions=None):
        query = f"SELECT * FROM {self.__table_name}"
        if conditions:
            query += " WHERE " + ' AND '.join([f"{key} = ?" for key in conditions.keys()])
            self.cursor.execute(query, tuple(conditions.values()))
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def update(self, table_name, data, conditions):
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        condition_clause = ' AND '.join([f"{key} = ?" for key in conditions.keys()])
        self.cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {condition_clause}", 
                            tuple(data.values()) + tuple(conditions.values()))
        self.connection.commit()

    def delete(self, table_name, conditions):
        condition_clause = ' AND '.join([f"{key} = ?" for key in conditions.keys()])
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition_clause}", tuple(conditions.values()))
        self.connection.commit()

    def close(self):
        self.connection.close()
