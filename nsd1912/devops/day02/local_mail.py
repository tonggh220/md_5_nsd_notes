from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件，plain表示纯文本
msg = MIMEText('python发送邮件测试\n', 'plain', 'utf8')
msg['From'] = Header('root', 'utf8')
msg['To'] = Header('tom', 'utf8')
msg['Subject'] = Header('py test')

# 发送邮件
smtp = smtplib.SMTP('localhost')
smtp.sendmail('root', ['tom', 'jerry'], msg.as_bytes())

# 查看邮件的使令: mail -u tom
