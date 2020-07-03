from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_email(message, sender, receivers, subject, server, passwd):
    # 准备邮件，plain表示纯文本
    msg = MIMEText(message, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(receivers[0], 'utf8')
    msg['Subject'] = Header(subject)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(server)
    # smtp.starttls()  # 如果服务器要求安全连接，打开此注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, msg.as_bytes())

if __name__ == '__main__':
    message = 'Python发送互联网邮件测试\n'
    sender = 'zhangzhigang79@qq.com'
    receivers = ['zhangzhigang79@qq.com', 'zhangzhigang79@126.com']
    subject = 'py email test'
    server = 'smtp.qq.com'
    # 注意，此处的密码不是登陆密码，而是授权码
    passwd = getpass.getpass()
    send_email(message, sender, receivers, subject, server, passwd)
