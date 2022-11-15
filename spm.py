#импорты
import smtplib

class sender:
    """Отправщик сообщения\n
            Методы:\n
    (__init__;send_1_msg_frm_1_acc;)

    """
    #подключение к серверу
    srv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    #инициализация обьекта отправщика
    def __init__ (self,ac:list,to:list,msg:str):
        """Необходимо указать :
        ac : один или несколько аккаунтов,каждый в списке и все они в еще одном списке; получается двумерный спиисок \n
        to : почта куда,одномерный массив в любом случае,если если почта одна \n
        msg : текст сообщения
        """
        self.srv=smtplib.SMTP_SSL('smtp.mail.ru', 465)
        self.to = to[0] if len(to)==1 else to
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
    def send_few_msg_frm_1_acc(self,vlm:int):
        """Метод для отправки нескольких сообщений с одного аккаунта на 1 аккаунт\n
        Принимает:\n
        двумерный массив и берет первый массив в списке массивов \n
        куда отправлять сообщение \n
        какое сообщение"""
        log=self.acc[0]
        puss=self.acc[1]
        for i in range(vlm):
            self.srv.login(log,puss)
            self.srv.sendmail(log,self.to,self.msg)
        self.srv.quit()
    def send_1_msg_frm_1_acc_to_mtpl_acs(self):
        """Метод для отправки 1 сообщения с одного аккаунта на несколько аккаунтов\n
        Принимает:\n
        двумерный массив и берет первый массив в списке массивов из аккаунтов отправки \n
        одномерный массив массивов куда отправить, и отправляет на каждый аккаунт одно сообщение \n\n

        какое сообщение"""
        log=self.acc[0]
        puss=self.acc[1]
        to=self.to
        for i in range(len(to)):
            self.srv.login(log,puss)
            self.srv.sendmail(log,to[i],self.msg)
        self.srv.quit()

#
# t="korobovvad@mail.ru"
# msg="test"
# volum=2
# t= ['korobovvad@mail.ru','korobovvad27@yandex.ru']
# snd = sender(ac=[["korobovvad@mail.ru","YkRcAHBJ9HewGYThxdCN"]],to=["korobovvad@mail.ru"],msg="аыпывпывп")
# snd.send_1_msg_frm_1_acc_to_mtpl_acs()
