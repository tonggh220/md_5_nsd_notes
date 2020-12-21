from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def inet_mail(body, sender, receivers, subject, host, passwd):
    # 准备邮件, plain表示纯文本
    message = MIMEText(body, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()  # 如果服务器要求安全连接，则打开此注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())
    smtp.close()

if __name__ == '__main__':
    body = 'python发送互联网邮件测试\n'
    sender = 'zhangzhigang79@qq.com'
    receivers = ['zhangzhigang79@qq.com', 'zhangzhigang79@126.com']
    subject = 'py mail test'
    host = 'smtp.qq.com'
    # 密码是开启smtp服务时给的授权码，不是登陆密码
    passwd = getpass.getpass()
    inet_mail(body, sender, receivers, subject, host, passwd)
