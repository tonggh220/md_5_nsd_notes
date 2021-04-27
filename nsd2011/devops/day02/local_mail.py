from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件，plain表示纯文本邮件
message = MIMEText('这是一封测试邮件\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')  # 发件人
message['To'] = Header('tom', 'utf8')     # 收件人
message['Subject'] = Header('py test', 'utf8')  # 主题

# 发邮件
smtp = smtplib.SMTP()  # 创建客户端对象
smtp.connect('127.0.0.1')   # 连接邮件服务器
smtp.sendmail('root', ['tom', 'jerry'], message.as_bytes())

# 查看tom用户邮件的命令: mail -u tom
