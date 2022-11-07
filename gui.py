from PyQt5 import uic ,QtWidgets #выдает ошибку,но не трогать,все работает
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("говно.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())