"""Модуль диалогов инфо-сообщений."""
from PyQt6.QtWidgets import QDialog, QFileDialog, QFontDialog, QMessageBox


def message(self, title: str, board_text: str, ico=1):
        """Информационное окно."""
        msg = QMessageBox()
        if ico == 1:
            msg.setIcon(QMessageBox.Icon.Information)
        if ico == 2:
            msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(board_text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
