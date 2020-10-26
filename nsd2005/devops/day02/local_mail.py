from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
# plain表示纯文本
message = MIMEText('py email test\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('tom', 'utf8')
message['Subject'] = Header('py test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('localhost')
smtp.sendmail('root', ['tom', 'jerry'], message.as_bytes())

