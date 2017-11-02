import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '13625206589@163.com'
msg['to'] = '2291481531@qq.com'
msg['subject'] = 'test'
content = '''''
    你好， 
            这是一封自动发送的邮件。 


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

#smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('13625206589@163.com', 'CXYchenxinyu1')
smtp.sendmail('13625206589@163.com', '2291481531@qq.com', str(msg))
smtp.quit()  