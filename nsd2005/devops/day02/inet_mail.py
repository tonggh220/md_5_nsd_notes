from email.mime.text import MIMEText
from email.header import Header
import getpass
import smtplib

def inet_mail(body, sender, receivers, subject, host, passwd):
    # 准备邮件
    # plain表示纯文本
    message = MIMEText(body, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()  # 如果服务器要求加密传输，则打开此注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    body = '互联网邮件服务器发送邮件测试\n'
    sender = 'zhangzhigang79@qq.com'
    receivers = ['zhangzhigang79@qq.com', 'zhangzhigang79@126.com']
    subject = 'python email test'
    host = 'smtp.qq.com'
    passwd = getpass.getpass()  # 填写授权码，而不是用户登陆密码
    inet_mail(body, sender, receivers, subject, host, passwd)
