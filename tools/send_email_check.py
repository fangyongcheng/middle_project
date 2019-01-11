'''邮箱发送'''


import os


from django.core.mail import send_mail, EmailMultiAlternatives

"""测试代码"""
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "middle_project.settings")

# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# if __name__ == '__main__':
#     print(111)
#     send_mail(
#         '这是邮件的标题',
#         '这是邮件的内容！',
#         'fangyongcheng520@sina.com',
#         ['747061804@qq.com'],)


# 传入邮箱账号,验证码
def send_to_customer(email_ID,check_code):
    subject, from_email, to = '来自的测试邮件', 'fangyongcheng520@sina.com', email_ID
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://127.0.0.1:8000/login/set_ID_active/?email='+email_ID+"&code="+check_code+'" target=blank>www.baizhi.com</a>，欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('发送成功')



# send_to_customer('747061804@qq.com',"123455")