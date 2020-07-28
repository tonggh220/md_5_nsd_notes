from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def write_email(text, subject, sender, receiver):
    # 1. 准备邮件
    msg = MIMEText(text, 'plain', 'utf8')  # 邮件正文
    msg['subject'] = Header(subject, 'utf8')  # 主题
    msg['from'] = Header(sender, 'utf8')  # 发件人
    msg['to'] = Header(receiver, 'utf8')  # 收件人
    return msg

def send_email(host, port=25, user=None, passwd=None, receivers=None, msg=None):
    # 2. 发送邮件
    smtp = smtplib.SMTP()  # 创建SMTP实例
    smtp.connect(host, port=port)  # 连接服务器
    # smtp.starttls()      # 如果服务器要求安全连接，则打开此注释
    smtp.login(user, passwd)
    smtp.sendmail(user, receivers, msg.as_bytes())

if __name__ == '__main__':
    message = write_email('python发送邮件测试\n', 'py email', 'zhangzhigang79@qq.com', 'zhangzhigang79@qq.com')
    host = 'smtp.qq.com'
    zzg = 'zhangzhigang79@qq.com'
    # 密码是开启smtp功能后的授权码，不是用户的登陆密码
    passwd = getpass.getpass()
    send_email(host, user=zzg, passwd=passwd, receivers=zzg, msg=message)
