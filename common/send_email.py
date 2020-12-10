import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from config.setting_path import report_path


class Send_email():
    def __init__(self):
        self.smtpserver = 'smtp.163.com'
    def send_report(self):
        # 发送人的账号密码
        user = 'xxxx@163.com'
        password = 'xxxxxxxx'

        # 发送和接收的邮箱
        sender = 'xxx@163.com'
        receive = '9xxxxx@qq.com'

        # 发送的主题和内容
        subject = "UI自动化测试报告"
        content = "测试报告"

        # HTML邮件正文
        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'xxxxx@163.com'
        msg['To'] = 'xxxxxx@qq.com'

        with open(report_path,'rb')as f:
            mime = MIMEBase('html','html',filename=report_path)
            mime.add_header('Content-Disposition', 'attachment', filename=report_path)
            # 获取附件内容
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            # 作为附件添加到邮件
            msg.attach(mime)

        # SSL协议端口号要使用465
        smtp = smtplib.SMTP_SSL(self.smtpserver, 465)

        # 向用户标识用户身份
        smtp.helo(self.smtpserver)
        # 服务器返回结果确认
        smtp.ehlo(self.smtpserver)
        # 登录邮箱服务器用户名和密码
        smtp.login(user, password)

        print("Start send Email....")
        smtp.sendmail(sender, receive, msg.as_string())
        smtp.quit()
        print("Send Email end!")

if __name__ == "__main__":
    Send_email().send_report()