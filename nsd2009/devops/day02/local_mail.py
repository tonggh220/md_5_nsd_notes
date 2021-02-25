from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 1. 准备邮件, plain表示纯文本
message = MIMEText('python email test\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('tom', 'utf8')
message['Subject'] = Header('py test', 'utf8')

# 2. 发送邮件
smtp = smtplib.SMTP()
smtp.connect('127.0.0.1')
smtp.sendmail('root', ['tom', 'jerry'], message.as_bytes())

# mail -u tom  # 查看tom的邮件
