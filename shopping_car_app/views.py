import time
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render,redirect
from tools.shopping_car import Car
# Create your views here.


from mainapp.models import TBooks, TAdress, TOrder, TOrderiterm, TUser

# 购物车视图函数
'''
说明：
1、session中存：shop_car_obj，是购物车对象
2、session中存：session_user_obj，是用户对象
'''
# 购物车视图
def shopping_car_view(request):
    # 保存session用于判断用户在哪个页面
    request.session['user_session_status'] = 2
    # 获得登录状态
    userobj=request.session.get('session_user_obj')
    # 获得商品信息
    shop_car_obj=request.session.get("shop_car_obj")
    return render(request,'shopping_car_app/car.html',{
    #     传登录状态
        'userobj':userobj,
    #     传入购物车书籍列表对象
        'shop_car_obj':shop_car_obj,
    })

# 地址页面视图
def shopping_car_indent_view(request):
    # 获得购物车对象，存在session中
    shop_car_obj = request.session.get('shop_car_obj')
    if shop_car_obj:
        # 获得登录状态
        userobj=request.session.get('session_user_obj')
        # 获得用户地址
        user_address_obj=TAdress.objects.filter(user=userobj.id)
        return render(request,'shopping_car_app/indent.html',{
        #     传登录状态
            'userobj':userobj,
        #     传入购物车信息
            "shop_car_obj":shop_car_obj,
        #     传入用户地址
            "user_address_obj":user_address_obj,
        })
    else:
        return redirect(to="shopping_car_app:shopping_car_view")

# 购物车订单完成视图
def shopping_car_indent_ok_view(request):
    # 保存session用于判断用户在哪个页面
    request.session['user_session_status'] = 2
    # 获得登录状态
    userobj=request.session.get('session_user_obj')
    # 获得订单id
    indent_num=request.GET.get('indent_num')
    # 获得订单id对象
    indent_num_obj=TOrder.objects.filter(id=indent_num)
    if indent_num_obj:
        indent_num_obj=indent_num_obj[0]
    return render(request,'shopping_car_app/indent ok.html',{
    #     传登录状态
        'userobj':userobj,
    #     传订单对象
        "indent_num_obj":indent_num_obj,
    })

# ajax添加购物车,增加减少书籍数量函数
def add_book_into_car(request):
    # 从前端获得数据：书的id和书的数量
    bookId=request.POST.get("bookId")
    bookCount=request.POST.get("bookCount")
    if not bookCount:
        bookCount=1
    # 判断否能重前端获得添加书的数据
    if bookId and bookCount:
        # 判断数据库中是否有这本书
        book_obj=TBooks.objects.filter(id=bookId)
        # 如果有这本书，添加进购物车
        if book_obj:
            # 判断购物车对象是否存在session中
            shop_car_obj=request.session.get('shop_car_obj')
            # 添加事务控制，出错回滚
            with transaction.atomic():
                # 如果购物车存在session中
                if shop_car_obj:
                    # 调Car对象的添加书的方法
                    shop_car_obj.add_book(bookId,bookCount)
                else:
                #     如果不存在，创建对象并调用的添加书的方法
                    shop_car_obj=Car()
                    # 调Car对象的添加书的方法
                    shop_car_obj.add_book(bookId, bookCount)
                #     shop_car_obj保存到session中
                request.session["shop_car_obj"]=shop_car_obj
                return HttpResponse('添加成功')
        else:
            HttpResponse('添加失败')
    else:
        return HttpResponse('添加失败')

# ajax改变书数量
def change_book_into_car(request):
    # 从前端获得数据：书的id和书的数量
    bookId=request.POST.get("bookId")
    bookCount=request.POST.get("bookCount")
    # 获得购物车对象，存在session中
    shop_car_obj = request.session.get('shop_car_obj')
    # 添加事务控制，出错回滚
    with transaction.atomic():
        # 如果购物车存在session中
        if shop_car_obj:
            # 添加事务控制，出错回滚
            shop_car_obj.book_change(bookId, bookCount)
            #     shop_car_obj保存到session中
            request.session["shop_car_obj"] = shop_car_obj
            return HttpResponse('成功')
        else:
            return HttpResponse('失败')

# 删除书
def delete_book(request):
    bookId = request.POST.get("bookId")
    # 获得购物车对象，存在session中
    shop_car_obj = request.session.get('shop_car_obj')
    # 添加事务控制，出错回滚
    with transaction.atomic():
        # 如果购物车存在session中
        if shop_car_obj:
            # 添加事务控制，出错回滚
            shop_car_obj.delete_book(bookId)
            #     shop_car_obj保存到session中
            request.session["shop_car_obj"] = shop_car_obj
            return HttpResponse('成功')
        else:
            return HttpResponse('失败')

# 恢复书
def find_book(request):
    bookId = request.POST.get("bookId")
    # print(type(bookId),bookId)
    # 获得购物车对象，存在session中
    shop_car_obj = request.session.get('shop_car_obj')
    # 添加事务控制，出错回滚
    with transaction.atomic():
        # 如果购物车存在session中
        if shop_car_obj:
            # 添加事务控制，出错回滚
            shop_car_obj.recover_car_book(bookId)
            #     shop_car_obj保存到session中
            request.session["shop_car_obj"] = shop_car_obj
    return redirect(to="shopping_car_app:shopping_car_view")

# 订单确定页面视图函数
def customer_sure_view(request):
    # 获得登录状态
    userobj=request.session.get('session_user_obj')
    # 获得购物车对象，存在session中
    shop_car_obj = request.session.get('shop_car_obj')
    # 判断购物车对象存在不，不存在跳转购物车视图
    if shop_car_obj:
        return render(request,'shopping_car_app/customer_sure.html',{
        #     传入购物车信息
            "shop_car_obj":shop_car_obj,
        #     传登录状态
            'userobj':userobj,
        })
    else:
        return redirect(to="shopping_car_app:shopping_car_view")

# 用户订单提交处理函数
def user_indent_dispose(request):
    # 获得购物车对象
    # 获得购物车对象，存在session中
    shop_car_obj = request.session.get('shop_car_obj')
    # 获得收货人姓名
    consignee_name=request.POST.get('ship_man_name')
    # 获得收件人国家
    consignee_country = request.POST.get('country_id')
    # 获得收货地址
    consignee_address=request.POST.get('province_id')
    # 获得收货人详细地址
    consignee_small_address=request.POST.get('ship_man_address')
    # 获得收货人邮编
    consignee_code=request.POST.get('ship_man_code')
    # 获得收货人手机
    consignee_tel_phone=request.POST.get('ship_man_tel_phone')
    # 获得收货人座机
    consignee_phone_number=request.POST.get('ship_man_phone_number')
    # 是否为新地址
    is_new_address=request.POST.get('address_choose')
    # 获得用户对象
    # 获得登录状态
    userobj=request.session.get('session_user_obj')

    # 检查是否为空,为空返回订单视图
    if consignee_name and consignee_country and consignee_address and consignee_small_address and consignee_code and (consignee_tel_phone or consignee_phone_number):
        # 判断是否在登录状态
        # 在则添加，不在则返回登录
        if userobj:
            # 查出登录用户对应id
            user_id_obj = TUser.objects.get(id=userobj.id)
            # 预防添加出错
            try:
            #     事务控制
                with transaction.atomic():
                    # # 地址拼接
                    # result_address="%s+%s+%s"%(consignee_country,consignee_address,consignee_small_address)
                    # 如果不是新地址添加新地址
                    if is_new_address == 'no_val':
                        address_obj =TAdress.objects.create(user =user_id_obj,
                                               name =consignee_name,
                                               detail_address =consignee_country,
                                               detail_address1 =consignee_address,
                                               detail_address2 =consignee_small_address,
                                               zipcode =consignee_code,
                                               telphone=consignee_tel_phone,
                                               addr_mobile=consignee_phone_number,)
            #
                    else:
                        # 如果存在则根据获得的id查找对应的地址
                        address_obj=TAdress.objects.get(id=is_new_address)
            #         创建订单号:12位的当前时间
                    indent_num=int(time.time()*1000)
            #         创建订单表
                    book_order_obj=TOrder.objects.create(user =user_id_obj,
                                          adress =address_obj,
                                          num =indent_num,
                                          create_date =time.strftime("%H:%M:%S", time.localtime()),
                                          price =shop_car_obj.total_price,
                                          status =1)
            #     创建订单项表
            #
                    for i in shop_car_obj.book_list:
                        # 获得书籍对象
                        book_obj=TBooks.objects.get(id=i.book.id)
                        # 改变书籍销量
                        book_obj.sales+=i.bookCount
                        book_obj.save()
                        TOrderiterm.objects.create(order =book_order_obj,
                                                   book =book_obj,
                                                   shop_num =i.bookCount,
                                                   total_price =i.bookCount*i.book.book_dprice)
            #         删除session中购物车对象
                    del request.session["shop_car_obj"]
            except BaseException as errors:
                print(errors)
            #     错误返回订单视图
                return redirect(to='shopping_car_app:shopping_car_indent_view')
            #     成功返回订单提交成功视图,传订单号
            else:
                return redirect("/car/shopping_car_indent_ok_view/?indent_num="+str(book_order_obj.id))
        else:
            return redirect(to='loginapp:login_view')
    else:
        return redirect(to='shopping_car_app:shopping_car_indent_view')



