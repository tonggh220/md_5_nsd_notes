from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件, plain表示纯文本
message = MIMEText("python local email test.\n", 'plain', 'utf8')  # 正文
message['From'] = Header('root', 'utf8')
message['To'] = Header('zhangsan', 'utf8')
message['Subject'] = Header('py test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('localhost')
smtp.sendmail('root', ['root', 'zhangsan'], message.as_bytes())
