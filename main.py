from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from ui import Ui_Main
from spm import sender
#список данных аккаунтов
data=[]
#список куда отправлять
dt_to=[]
class mn(QtWidgets.QMainWindow):
    def __init__(self):
        super(mn, self).__init__()
        self.ui=Ui_Main()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.mail_send_but.clicked.connect(self.get_dt)
        self.ui.msg_acc.clicked.connect(self.msg)
        self.ui.vlm_acc.clicked.connect(self.check_vlm)
        self.ui.add_us_dt_but.clicked.connect(self.add_dt)
        self.ui.add_to_but.clicked.connect(self.add_to)


    #получение данных
    def get_dt(self):
        # if result():
        log = self.ui.log_us_edit.text()
        pus = self.ui.pus_us_edit.text()
        msg = self.ui.msg_txt_edit.text()
        vlm = self.ui.volum_edit.text()
        to = self.ui.to_edit.text()
        c = sender(ac=[[log,pus]],to=[to],msg=msg)
        c.send_1_msg_frm_1_acc()
        # else:
        #     pass
    #проверка правильности написания сообщения
    def msg(self):
        msg = self.ui.msg_txt_edit.text()
        if msg=="":
            err_msg(txt="Поле сообщения не должно быть пусты.", title="Ошибка текста.")
            self.ui.msg_status.setText("-")
        elif check_kod(str(msg)):
            err_msg(txt="Текст сообщения далжен содержать только англ. язык.",title="Ошибка текста.")
            self.ui.msg_status.setText("-")
        else:
            self.ui.msg_status.setText("+")
    #проверка количества
    def check_vlm(self):
        vlm=self.ui.volum_edit.text()
        try:
            vlm=int(vlm)
            if vlm==0:
                err_msg(txt="Количество не может быть равно нулю.", title="Ошибка.")
                self.ui.vlm_status.setText("-")
                self.ui.volum_edit.clear()
            elif vlm>=200:
                err_msg(txt="Слишком много.", title="Ошибка.")
                self.ui.vlm_status.setText("-")
                self.ui.volum_edit.clear()
            else:
                self.ui.vlm_status.setText("+")
        except:
            err_msg(txt="В поле количества должны быть цифры.", title="Ошибка.")
            self.ui.volum_edit.clear()
            self.ui.vlm_status.setText("-")

    #проверка все ли данные вписаны
    def result(self):
        log = self.ui.dt_us_status.text()=="+"
        pus = self.ui.dt_us_status.text()=="+"
        msg = self.ui.msg_status.text()=="+"
        vlm = self.ui.vlm_status.text()=="+"
        to = self.ui.to_status.text()=="+"
        if log and pus and msg and vlm and to:
            return True
        else:
            return False
    #добавление аккаунто
    def add_dt(self):
        log = self.ui.log_us_edit.text()
        pus = self.ui.pus_us_edit.text()
        md = 0
        row = 0
        data.append([log,pus,md])
        self.ui.dt_us_area_table.setRowCount(len(data))
        for tup in data:
            col = 0
            for item in tup:

                cellinfo = QtWidgets.QTableWidgetItem(item)
                self.ui.dt_us_area_table.setItem(row, col , cellinfo)
                col += 1

            row += 1
    #добавление куда отправлять
    def add_to(self):
        to = self.ui.to_edit.text()
        md = 0
        row = 0
        dt_to.append([to,md])
        self.ui.to_area.setRowCount(len(dt_to))
        for tup in dt_to:
            col = 0
            for item in tup:

                cellinfo = QtWidgets.QTableWidgetItem(item)
                self.ui.to_area.setItem(row, col , cellinfo)
                col += 1

            row += 1



#проверка состоит ли код только из символов кодировки , предотврощает ошибку smtp при вводе русских слов
def check_kod(a):
    try:
        rs=a.encode('ascii')
        return False
    except:
        return True

#Сообщение об ошибке
def err_msg(txt,title):
    msg_err = QMessageBox()
    msg_err.setWindowTitle(title)
    msg_err.setText(txt)
    msg_err.setIcon(QMessageBox.Warning)
    msg_err.exec_()

app=QtWidgets.QApplication([])
application=mn()
application.show()

sys.exit(app.exec())
