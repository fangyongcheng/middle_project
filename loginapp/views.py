import time


from django.contrib.auth.hashers import make_password, check_password
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render,redirect
from captcha.image import ImageCaptcha
from tools.random_code import code_four
from mainapp import models
# Create your views here.
from tools import send_email_check

'''
说明：
email，电话唯一
跳转登录注册页面状态status说明：
1：跳转主页
2：跳转购物车,地址填写页面
登录状态判断：
登录注册成功后会保存session：名字：session_user_obj，作用：保存用户对象，通过他判断是否登录

'''
# 登录视图函数
def login_view(request):
    # 获得在哪个页面登录的信息
    user_status = request.session.get("user_session_status")
    # 读取cookie
    email=request.COOKIES.get('cookie_user_email_phone')
    pwd=request.COOKIES.get('cookie_user_password')
    # 如果cookie匹配成功自动登录
    # cookie存在
    if email and pwd:
        # 数据库中查找
        user_obj = models.TUser.objects.filter(user_email=email)
        # 账号密码匹配
        if user_obj:
            user_obj_result = check_password(pwd, user_obj[0].user_password)
            # 保存从哪个页面点击的状态status
            user_obj[0].user_status=user_status
            # 保存登录成功状态
            request.session['session_user_obj']=user_obj[0]
            # 都匹配成功跳转判断跳转到具体哪个页面
            return redirect(to='loginapp:register_login_success_jump')
    # 如果没有为1
    if not user_status:
        user_status=1
    return render(request,'loginapp/login.html',{'status':user_status})

# 注册视图
def register_view(request):
    status=request.session.get("user_session_status")
    return render(request,'loginapp/register.html',
                  {
                      'status':status,
                  })

# 注册成功视图
def register_ok_view(request):
    # 获得登录状态
    userobj = request.session.get('session_user_obj')
    return render(request,'loginapp/register ok.html',{
    #     传递登陆状态
        'user_obj':userobj
    })

# 注册判断函数
def register_decide(request):
    return HttpResponse('成功')

# 生成验证码
def create_img_code(request):
    # 创建验证码对象
    image=ImageCaptcha()
    # 生成随机的4位随机码
    code=code_four()
    # 将随机码存session中，键为code
    request.session['code']=code
    # 把随机码存入图片对象
    data=image.generate(code)
    return HttpResponse(data,'image/png')

# 判断注册是否成功的函数,成功添加数据到数据到，失败回滚
def decide_register_is_success(request):
    # 重前端获得数据
    # 昵称
    name=request.POST.get('name')
    # 邮箱/电话
    txt_username=request.POST.get('txt_username')
    # 密码
    txt_password=request.POST.get('txt_password')
    # 状态
    register_status=request.session.get("user_session_status")

    # 如果没有状态，状态默认为1
    if not register_status:
        register_status=1
    # 防止添加数据失败
    try:
        with transaction.atomic():
            # 向数据库添加数据
            # # 生成激活验证码
            # code=code_four()
            # send_email_check.send_to_customer(txt_username,code)
            # 调用Django自带的密码加密
            make_password(txt_password,salt=code_four())
            user_obj=models.TUser.objects.create(user_name=name,user_email=txt_username,user_password=txt_password,user_status=1)
            # 把用户对象添加到session中
            request.session['session_user_obj'] =user_obj
            return redirect(to='loginapp:register_ok_view')
    except BaseException:
        return HttpResponse('注册失败！请检查输入内容')


# ajax判断
# 判断邮箱是否重名
def decide_email_name(request):
    # 前端获取email
    email=request.POST.get('email')
    email_obj=models.TUser.objects.filter(user_email=email)
    if email_obj:
        # 用户名存在
        return HttpResponse('1')
    else:
        # 用户名不存在
        return HttpResponse('0')
# 判断验证码是否正确
def decide_img_code(request):
    # session中获得code
    code=request.session.get('code')
    # 前端获得code
    get_code=request.POST.get('code')
    # 判断验证码是否一致
    if code.upper()==get_code.upper():
        return HttpResponse('1')
    else:
        return HttpResponse('0')

# 注册登录成功跳转
def register_login_success_jump(requst):
    # session中通过email查找对 应的email
    user_obj=requst.session.get('session_user_obj')
    # 在数据库中查找,看是否找到用户，用户验证成功则正常跳转，没有则跳转登录
    find_obj=models.TUser.objects.filter(user_email=user_obj.user_email)
    if find_obj:

        if find_obj[0].blank1=='1':
            # 查找应该跳转的页面：1:主页面；2：订单确定页面
            decide_jump=requst.session.get('user_session_status')
            if decide_jump:
                if int(decide_jump) == 2:
                    # 跳购物车app中的订单确定页面
                    return redirect(to="shopping_car_app:customer_sure_view")
                else:
                    # 状态为1主页
                    return redirect(to='mainapp:index')

            else:
                # 跳主页
                return redirect(to='mainapp:index')
        else:
            # 跳转激活页面·
            return redirect(to='loginapp:set_active_riew')
    else:
        return redirect(to='loginapp:login_view')

# ajax登录判断
def decide_login_is_success(request):
    # 重前端获得email和密码
    user_emial=request.POST.get('email')
    user_pwd=request.POST.get('password')
    user_status=request.session.get("user_session_status")
    check_me=request.POST.get('check_me')
    # 数据库中查找筛选
    user_obj=models.TUser.objects.filter(user_email=user_emial)
    if user_obj:
        # 解码对比
        user_obj_result = check_password(user_pwd,user_obj[0].user_password )
        res=HttpResponse('1')
        if user_obj_result:
            # 判断点击记住我没有，如果点击了，记住账号密码一周
            if check_me:
                res.set_cookie('cookie_user_email_phone',user_emial,max_age=60*60*24*7)
                res.set_cookie('cookie_user_password',user_pwd,max_age=60*60*24*7)
            # 保存从哪跳转的状态
            user_obj[0].user_status=user_status
            # 保存登录状态
            request.session['session_user_obj']=user_obj[0]
            return res
        else:
            return HttpResponse('0')
    else:
        return HttpResponse('0')

#     登出状态
def login_status_exit(request):
    del request.session['session_user_obj']
    return redirect(to='mainapp:index')

# 设置账号的激活
def set_ID_active(requset):
    # 获得验证码和email账号
    code=requset.GET.get('code')
    email_id=requset.GET.get('email')
    # 数据库中查找用户存在否
    user_obj=models.TUser.objects.filter(user_email =email_id)
    if code:
        try:
            if user_obj:
                # 判断如果验证码和数据库相同，激活账号
                if user_obj[0].blank2==code:
                    user_obj[0].blank1='1'
                    user_obj[0].save()
                    return redirect(to="loginapp:register_login_success_jump")
        except:
            pass

    return HttpResponse('激活失败')

#设置激活的页面
def set_active_riew(request):
    return render(request,"loginapp/active.html")

#  发送激活验证
def send_active(request):
    email_id=request.GET.get('email')
    pwd=request.GET.get('pwd')
    # 数据库中查找用户存在否
    user_obj=models.TUser.objects.filter(user_email =email_id,user_password=pwd)
    if user_obj:
        # 生成激活验证码
        code = code_four()
        send_email_check.send_to_customer(email_id, code)
        user_obj[0].blank2=code
        user_obj[0].save()
        return redirect(to='/login/set_ID_active/?'+"code="+code+"&email="+email_id)
    else:
        return HttpResponse("账号密码错误")



