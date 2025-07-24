#!/usr/bin/env python3
import sys
from PyQt6 import QtWidgets, uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('ui/main_window.ui', self)
    '''
        Just fill this with code )))
        
        # Здесь сигналы и слоты
        self.pushButton.clicked.connect(self.on_button_click)  # подключения кнопки

    def on_button_click(self):
        # Действие при нажатии кнопки
        self.label.setText("Кнопка нажата!")  # Изменяем текст метки
    '''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
