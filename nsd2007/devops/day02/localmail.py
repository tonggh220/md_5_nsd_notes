from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件, plain表示纯文本
message = MIMEText('python发送email测试\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('tom')
message['Subject'] = Header('py test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('127.0.0.1')
smtp.sendmail('root', ['tom', 'zhangsan'], message.as_bytes())
smtp.close()
