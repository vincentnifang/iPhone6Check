__author__ = 'vincent'


import smtplib
from email.mime.text import MIMEText


# host = 'smtp.163.com'
# port = 465
# sender = 'ad_vincent@163.com'
# pwd = '232323'
# receiver = 'ad_vincent@163.com'
# body = '<h1>Hi</h1><p>test</p>'
#
# msg = MIMEText(body, 'html')
# msg['subject'] = 'Hello world'
# msg['from'] = sender
# msg['to'] = receiver
#
# s = smtplib.SMTP_SSL(host, port)
# s.login(sender, pwd)
# s.sendmail(sender, receiver, msg.as_string())
#
# print 'over'



mailto_list=[""] # mazhaoqin mail
mail_host="smtp.163.com"
mail_user=""
mail_pass=""
mail_postfix="163.com"
ssl_port = 465

def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP_SSL()
        server.connect(mail_host,ssl_port)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"hello","hello world"):
        print "SS"
    else:
        print "Fail"