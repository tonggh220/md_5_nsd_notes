from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件。plain表示纯文本邮件
msg = MIMEText('python send email test.\n', 'plain', 'utf8')  # 正文
msg['From'] = Header('root', 'utf8')  # 发件人
msg['To'] = Header('tom', 'utf8')     # 收件人
msg['Subject'] = Header('py test', 'utf8')  # 主题

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('localhost')
smtp.sendmail('root', ['tom', 'jerry'], msg.as_bytes())
