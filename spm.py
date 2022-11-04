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
# log="korobovvad@mail.ru"
# puss="YkRcAHBJ9HewGYThxdCN"# YkRcAHBJ9HewGYThxdCN
to="korobovvad@mail.ru"
msg="test"
###
# obj1=frm_mail(logn=log,pus=puss)

#выполнение
def send_msg(logn,pus,to,msg):
    srv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    #srv.set_debuglevel(1)
    srv.login(logn,pus)
    srv.sendmail(logn,to,msg)
    srv.quit()
#######
send_msg(acc[0][0],acc[0][1],to,msg)