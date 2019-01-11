from django.urls import path
from loginapp import views

# app别名：
app_name='loginapp'

# 路由系统
urlpatterns = [
    # 登录视图函数路径
    path('login_view/',views.login_view,name='login_view'),
#     注册视图路径
    path('register_view/',views.register_view,name='register_view'),
#     注册成功视图路径
    path('register_ok_view/',views.register_ok_view,name='register_ok_view'),
#     验证码路由
    path('create_img_code/',views.create_img_code,name='create_img_code'),
#     ajax判断email路由
    path('decide_email_name/',views.decide_email_name,name='decide_email_name'),
#     ajax判断验证码路由
    path('decide_img_code/',views.decide_img_code,name='decide_img_code'),
#     判断注册是否成功路由
    path('decide_register_is_success/',views.decide_register_is_success,name='decide_register_is_success'),
#     登录注册成功跳转判断
    path('register_login_success_jump/',views.register_login_success_jump,name='register_login_success_jump'),
#     登录判断路由
    path('decide_login_is_success/',views.decide_login_is_success,name='decide_login_is_success'),
#     登出状态路由
    path('login_status_exit/',views.login_status_exit,name='login_status_exit'),
#     设置账号激活码路由
    path("set_ID_active/",views.set_ID_active,name="set_ID_active"),
#     发送激活验证
    path('send_active/',views.send_active,name="send_active"),
    # 激活页面
    path("set_active_riew/",views.set_active_riew,name="set_active_riew"),
]
