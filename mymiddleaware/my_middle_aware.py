from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin



# 创建中间介强制跳转
class MyMiddleAware(MiddlewareMixin):
    # view处理请求前执行
    def process_request(self,request):
        # 如果路由中没有login和main和car强制跳到主页中
        if 'main' not in request.path and 'login' not in request.path and 'car' not in request.path and 'favicon' not in request.path and 'header' not in request.path:
            # return HttpResponse('wqe')
            return redirect(to='mainapp:index')
        elif "indent" in request.path or "customer" in request.path:
            # 获得登录状态
            userobj = request.session.get('session_user_obj')
            # 如果登录状态不存在，跳转登录界面
            if not userobj:
                return redirect(to='loginapp:login_view')




