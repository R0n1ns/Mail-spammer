from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QIcon
from ui import Ui_Main
from spm import sender

class mn(QtWidgets.QMainWindow):
    def __init__(self):
        super(mn, self).__init__()
        self.ui=Ui_Main()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.mail_send_but.clicked.connect(self.get_dt)

    def get_dt(self):
        log = self.ui.log_us_edit.text()
        pus = self.ui.pus_us_edit.text()
        msg = self.ui.msg_txt_edit.text()
        vlm = self.ui.volum_edit.text()
        to = self.ui.to_edit.text()
        c=sender(ac=[[log,pus]],to=[to],msg=msg)
        c.send_1_msg_frm_1_acc()



app=QtWidgets.QApplication([])
application=mn()
application.show()

sys.exit(app.exec())
