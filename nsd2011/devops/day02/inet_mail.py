from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def inet_mail(body, sender, receivers, subject, host, passwd):
    # 准备邮件，plain表示纯文本邮件
    message = MIMEText(body, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')      # 发件人
    message['To'] = Header(receivers[0], 'utf8')  # 收件人
    message['Subject'] = Header(subject, 'utf8')  # 主题

    # 发邮件
    smtp = smtplib.SMTP()  # 创建客户端对象
    smtp.connect(host)     # 连接邮件服务器
    # smtp.starttls()      # 如果服务器要求安全连接，则打开此注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    body = 'py互联网邮件测试\n'
    sender = 'zhangzhigang79@qq.com'
    receivers = ['zhangzhigang79@qq.com', 'zhangzhigang79@126.com']
    subject = 'py test'
    host = 'smtp.qq.com'
    # 密码是授权码，不是登陆密码
    passwd = getpass.getpass()
    inet_mail(body, sender, receivers, subject, host, passwd)
