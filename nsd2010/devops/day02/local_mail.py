from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件, plain表示纯文本
message = MIMEText('python email test.\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')  # 发件人
message['To'] = Header('tom', 'utf8')     # 收件人
message['Subject'] = Header('py test', 'utf8')  # 主题

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('127.0.0.1')
smtp.sendmail('root', ['tom', 'jerry'], message.as_bytes())

# mail -u tom   # 查看tom用户的邮件
