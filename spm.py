#импорты
import smtplib
from imp_acc import acc
##классы
# class frm_mail():
#     def __init__ (self,logn,pus):
#         self.logn=logn
#         self.pus=pus
#     def ret_log(self):
#         return self.logn
#     def ret_pus(self):
#         return self.pus

t="korobovvad@mail.ru"
msg="test"
volum=2

class sender:
    """Отправщик сообщения\n
            Методы:\n
    (__init__;send_1_msg_frm_1_acc;)

    """
    #подключение к серверу
    srv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    #инициализация обьекта отправщика
    def __init__ (self,ac,to,msg):
        """Необходимо указать :
        ac : один или несколько аккаунтов,каждый в списке и все они в еще одном списке; получается двумерный спиисок \n
        to : почта куда: пока одна \n
        msg : текст сообщения
        """
        self.srv=smtplib.SMTP_SSL('smtp.mail.ru', 465)
        self.to = to
        self.msg = msg
        self.acc = acc=ac[0] if len(ac)==1 else ac
    #отправка одного сообщения с одного аккаунта
    def send_1_msg_frm_1_acc(self):
        """Метод для отправки 1 сообщения с одного аккаунта на 1 аккаунт\n
        Принимает:\n
        двумерный массив и берет первый массив в списке массивов \n
        куда отправлять сообщение \n
        какое сообщение"""
        log=self.acc[0]
        puss=self.acc[1]
        self.srv.login(log, puss)
        self.srv.sendmail(log, self.to, self.msg)
        self.srv.quit()

snd = sender(acc,t,msg)
snd.send_1_msg_frm_1_acc()
#выполнение
#отправка 1 сообщения с одной почты
def send_msg(logn,pus,to,msg):
    srv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    #srv.set_debuglevel(1)
    srv.login(logn,pus)
    srv.sendmail(logn,to,msg)
    srv.quit()
#множественный спам с одной почты
def spam(ac,ms,to,vlm):
    srv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    for i in range(vlm):
        srv.login(ac, ac)
        srv.sendmail(ac, to, ms)
    srv.quit()

#######
#тесты
#send_msg(acc[0][0],acc[0][1],to,msg)
# spam(acc,msg,t,volum)