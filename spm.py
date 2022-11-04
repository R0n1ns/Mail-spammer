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


#выполнение
def send_msg(logn,pus,to,msg):
    srv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    #srv.set_debuglevel(1)
    srv.login(logn,pus)
    srv.sendmail(logn,to,msg)
    srv.quit()

def spam(acs,ms,to,vlm):
    srv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    for i in range(vlm):
        srv.login(acs[0][0], acs[0][1])
        srv.sendmail(acs[0][0], to, ms)
    srv.quit()

#######
#send_msg(acc[0][0],acc[0][1],to,msg)
spam(acc,msg,t,volum)