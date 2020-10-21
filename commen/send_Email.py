# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
#
#
# def send_email(report_file):  # 发送自动化测试邮件
#     with open(report_file, 'r', encoding='utf-8') as f:
#         mail_body = f.read()  # 打开测试报告，读取报告内容作为邮件内容
#         sender = '942882483@qq.com'  # 发出邮箱
#         receiver = ['942882483@qq.com']  # 接收邮箱
#         mail_server = 'smtp.qq.com'  # 邮箱服务地址，这里以139邮箱为例
#         subject = '自动化测试报告'  # 邮件标题
#         username = '942882483@qq.com'  # 邮箱登录名
#         passwd = 'ofqhrthfiaegbdge'  # 密码
#         message = MIMEText(mail_body, 'html', 'utf-8')  # 设置邮件格式
#         message['Subject'] = Header(subject, charset='utf-8')
#         # 邮箱登录
#         smtp = smtplib.SMTP()  # 实例化smtplib.SMTP()类对象
#         smtp.connect(mail_server)  # 连接邮件服务器
#         smtp.login(username, passwd)  # 登录
#         # 发送邮件
#     for i in receiver:
#         smtp.sendmail(sender, i, message.as_string())
#     smtp.quit()

#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.utils import formataddr
# from config.confi import report_path2
#
#
# class EmailHandler:
#     def __init__(self):
#         self.my_sender = '942882483@qq.com'  # 发件人邮箱账号
#         self.my_pass = 'ofqhrthfiaegbdge'  # 发件人邮箱密码,此处为授权码
#         self.my_user = '942882483@qq.com'  # 收件人邮箱账号，我这边发送给自己
#
#     def send_email(self):
#         ret = True
#         #str(open('/python/new.txt', 'rb').read())
#         # report_path
#         try:
#             #创建一个带附件的实例
#             message = MIMEMultipart()
#             msg = MIMEText('接口自动化测试报告', 'plain', 'utf-8')  # #邮件正文内容
#             message['From'] = formataddr(["测试员", self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#             message['To'] = formataddr(["收件人", self.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#             message['Subject'] = "接口自动化测试结果"  # 邮件的标题
#             message.attach(msg)  # 邮件正文内容
#             #添加附件
#             att1 = MIMEText(str(open(report_path2, 'rb').read()), 'base64', 'utf-8')
#             att1["Content-Type"] = 'application/octet-stream'
#             # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#             att1.add_header('Content-Disposition', 'attachment', filename='测试报告.html')
#             message.attach(att1)
#             #发送邮件
#             server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
#             server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#             server.sendmail(self.my_sender, [self.my_user, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#             server.quit()  # 关闭连接
#         except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#             ret = False
#         #     logger().info("邮件发送失败")
#         # logger().info("邮件发送成功")
#
#         return ret


#_*_coding:utf-8_*_

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.header import Header
# from email import encoders
# import time
# import yaml,os,base64
# from pos.lib import gl,scripts
#
#
# class EmailClass(object):
#     def __init__(self):
#         self.curDateTime = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #当前日期时间
#         self.config = scripts.getYamlfield(gl.configFile) #配置文件路径
#         self.sender = self.config['EMAIL']['Smtp_Sender'] # 从配置文件获取，发件人
#         self.receivers = self.config['EMAIL']['Receivers']  # 从配置文件获取，接收人
#         self.msg_title = self.config['EMAIL']['Msg_Title'] #从配置文件获取，邮件标题
#         self.sender_server = self.config['EMAIL']['Smtp_Server'] #从配置文件获取，发送服务器
#         self.From = self.config['EMAIL']['From']
#         self.To = self.config['EMAIL']['To']
#
#     '''
#     配置邮件内容
#     '''
#     @property
#     def setMailContent(self):
#         print(self.receivers)
#         msg = MIMEMultipart()
#         msg['From'] = Header(self.From,'utf-8')
#         msg['To'] = self.To
#         msg['Subject'] = Header('%s%s'%(self.msg_title,self.curDateTime),'utf-8')
#
#         #附件路径
#         dirpath = gl.reportPath
#         zipfile = os.path.join(os.path.dirname(dirpath), 'report.zip')
#         reportfile = os.path.join(gl.reportPath, 'Report.html')
#         scripts.zipDir(dirpath,zipfile) #压缩报告
#         #增加邮件内容为html
#         fp = open(reportfile, 'rb')
#         reportHtmlText = str(fp.read())
#         msg.attach(MIMEText(reportHtmlText,'html','utf-8'))
#         fp.close()
#
#         #增加附件
#         html = self.addAttach(zipfile,filename='Report%s.zip'%self.curDateTime) #自动化测试报告附件
#         msg.attach(html)
#
#         return msg
#
#
#     '''
#     增加附件
#     '''
#     def addAttach(self,apath,filename='Report.html'):
#         with open(apath, 'rb') as fp:
#             attach = MIMEBase('application','octet-stream')
#             attach.set_payload(fp.read())
#             attach.add_header('Content-Disposition', 'attachment', filename=filename)
#             encoders.encode_base64(attach)
#             fp.close()
#             return attach
#
#
#     '''
#     发送电子邮件
#     '''
#     def sendEmail(self,message):
#         try:
#             smtpObj = smtplib.SMTP()
#             smtpObj.connect(self.sender_server,25)
#             smtpObj.login(self.sender,self.config['EMAIL']['Password'])
#             smtpObj.sendmail(self.sender,self.receivers , message.as_string())
#             smtpObj.quit()
#             print ("邮件发送成功")
#         except smtplib.SMTPException as ex:
#             print ("Error: 无法发送邮件.%s"%ex)
#
#     #发送调用
#     @property
#     def send(self):
#         self.sendEmail(self.setMailContent)
#
# if __name__=="__main__":
#     EmailClass().send
