from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 1. 准备邮件
# plain表示纯文本
msg = MIMEText('This is a email test\n', 'plain', 'utf8')  # 邮件正文
msg['subject'] = Header('py test', 'utf8')  # 主题
msg['from'] = Header('root', 'utf8')  # 发件人
msg['to'] = Header('tom', 'utf8')  # 收件人

# 2. 发送邮件
smtp = smtplib.SMTP('localhost')
smtp.sendmail('root', ['tom', 'jerry'], msg.as_bytes())
