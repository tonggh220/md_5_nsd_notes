from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
# plain表示纯文本
message = MIMEText('python email test\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('tom', 'utf8')
message['Subject'] = Header('py test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP('localhost')
smtp.sendmail('root', ['tom', 'jerry'], message.as_bytes())

# useradd tom
# useradd jerry
# mail -u tom  查看tom的邮件
