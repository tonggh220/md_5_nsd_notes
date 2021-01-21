from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备正文，plain表示纯文本内容
message = MIMEText('python email test.\n', 'plain', 'utf8')
# 设置头部消息
message['From'] = Header('root', 'utf8')
message['To'] = Header('tom', 'utf8')
message['Subject'] = Header('py test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP()  # 创建smtp对象
smtp.connect('127.0.0.1')  # 连接服务器
smtp.sendmail('root', ['tom', 'jerry'], message.as_bytes())
