from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def inet_mail(body, subject, sender, receivers, host, port, password):
    # 准备邮件, plain表示纯文本
    message = MIMEText(body, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')  # 发件人
    message['To'] = Header(receivers[0], 'utf8')     # 收件人
    message['Subject'] = Header(subject, 'utf8')  # 主题

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(host, port=port)
    # smtp.starttls()  # 如果服务器要求安全连接，则打开此注释
    smtp.login(sender, password)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    body = 'python互联网邮件测试\n'
    sender = 'zhangzhigang79@qq.com'
    receivers = ['zhangzhigang79@qq.com', 'zhangzhigang79@126.com']
    subject = 'py test'
    host = 'smtp.qq.com'
    # 密码不是登陆密码，而是授权码
    passwd = getpass.getpass()
    inet_mail(body, sender, receivers, subject, host, passwd)
