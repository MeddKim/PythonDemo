import smtplib

from email.mime.text import MIMEText
from email.header import Header
from .smtp_config import *

class Sender(object):

	"""邮件发送者"""
	def __init__(self):
		self.__config = SmtpConfig()

		self.__recievers = []

		self.__title = '测试标题'
		self.__content = '测试内容'

	def setSmtpConfig(self,smtp_config):
		self.__config = smtp_config

	def add_reciever(self,receiver):
		self.__recievers.append(receiver)

	def send_mail(self):

		if 0 == len(self.__recievers):
			raise Exception('收件人不可为空')

		message = MIMEText(self.__content, 'plain', 'utf-8')
		message['From'] = "{}".format(self.__config.MAIL_SENDER)
		message['To'] = ",".join(self.__recievers)
		message['Subject'] = self.__title

		try:
			smtpObj = smtplib.SMTP_SSL(self.__config.MAIL_HOST, 465)  # 启用SSL发信, 端口一般是465
			smtpObj.login(self.__config.MAIL_USER, self.__config.MAIL_PASS)  # 登录验证
			smtpObj.sendmail(self.__config.MAIL_SENDER, self.__recievers, message.as_string())  # 发送
			print("邮件发送成功")
		except smtplib.SMTPException as e:
			print(e)


	def set_title(self,title):
		self.__title = title
	def set_content(self,content):
		self.__content = content

# if __name__ == '__main__':
#     sender = Sender()
#     sender.send_mail()