from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from mainapp.models import TBooks,TTypes

"""
说明：
1、user_session_status:保存session用于判断用户在哪个页面
状态码：
1：主页面
2：购物车页面

"""
#
# 主视图函数
def index_view(request):
    # 保存session用于判断用户在哪个页面
    request.session['user_session_status'] = 1
    # 获得登录状态
    userobj=request.session.get('session_user_obj')
    # 获得最新上架书的对象
    books_news_max=TBooks.objects.all().order_by('-shelves_date')
    # 获得最新的3组（每组8本）
    book_new_list=[books_news_max[0:8],books_news_max[8:16],books_news_max[16:24]]
    # 获得10本销量最高书的对象
    books_sales_max=TBooks.objects.all().order_by('-sales')[0:10]
    # 获得评分最高的12本书
    books_socre_max=TBooks.objects.all().order_by('-customer_socre')
    book_socre_list=[books_socre_max[0:4],books_socre_max[4:8],books_socre_max[8:12]]
    # 获得一二级分类对象
    # 获得一级分类对象
    books_type_one=TTypes.objects.filter(parent_id__isnull=True)
    # 获得二级分类对象
    books_type_two = TTypes.objects.filter(parent_id__isnull=False)
    # 传参
    return render(request,'mainapp/index.html',
                  # 最新的3组书对象
                  {'books_new_list':book_new_list,
                   # 销量最高书的对象
                   'books_sales_max':books_sales_max,
                   # 评分最高书对象
                   "book_socre_list":book_socre_list,
                   # 类型1列表
                   'books_type_one':books_type_one,
                   # 类型2列表
                   'books_type_two':books_type_two,
                   # 用户名
                   'userobj':userobj,
                   })

# 图书详情视图
def book_detail_view(request):
    # 保存session用于判断用户在哪个页面
    request.session['user_session_status'] = 1
    # 获得登录状态
    userobj=request.session.get('session_user_obj')
    # 如果id出错默认第一本书
    book_id=request.GET.get('book_id')
    if not book_id:
        book_id=1
    # 通过书籍id获得书籍对象
    book_object=TBooks.objects.get(id=book_id)
    # 获得类别1和类别2名字
    book_type_two=book_object.type.class_name
    book_type_one = TTypes.objects.get(id=book_object.type.parent_id).class_name
    # 小类的id
    books_type=book_object.type_id
    # 大类的id
    books_type_big=TTypes.objects.get(id=books_type).parent_id
    print(books_type,books_type_big)
    return render(request,'mainapp/Book details.html',{'book_object':book_object,#传递书籍对象
                                                       'book_types':[book_type_one,book_type_two],#传递类型1，2名字
                                                       # 用户名
                                                       'userobj': userobj,
                                                       # 小类的id
                                                       "books_type": books_type,
                                                       # 大类的id
                                                       'books_type_big': books_type_big,
                                                       })

# 图书列表视图
def book_list_view(request):
    # 保存session用于判断用户在哪个页面
    request.session['user_session_status'] = 1
    # 获得登录状态
    userobj=request.session.get('session_user_obj')
    # 获得图书小分类id
    books_type=request.GET.get('books_type')
    # 获得图书大分类id
    books_type_big=request.GET.get('books_type_big')
    # 获得排序的参数：类型
    sort_obj=request.GET.get('sort')
    # 获得排序状态：升序或者降序
    asc_or_dsc=request.GET.get('asc_or_dsc')
    # 判断是一级分类还是二级分类
    # 如果没获得分类默认1对应的教育类查询
    if not books_type and not books_type_big:
        books_type_big=1
    if books_type:
        #     获得列对象
        books_type_object_list = TBooks.objects.filter(type_id=books_type)
        # 获得类型2名字
        books_type_two_name = TTypes.objects.get(id=books_type).class_name
        # 获得类型1名字
        books_type_one_name = TTypes.objects.get(id=TTypes.objects.get(id=books_type).parent_id).class_name
        # 获得类型1的id
        books_type_big = TTypes.objects.get(id=books_type).parent_id
        # 获得类型名列表
        book_types_list=[books_type_one_name,books_type_two_name]
    else:
        #     获得列对象
        books_type_object_list = TBooks.objects.filter(type__parent_id=books_type_big)
        # 获得类型1名字
        books_type_one_name = TTypes.objects.get(id=books_type_big).class_name
        # 获得类型名列表
        book_types_list = [books_type_one_name]


    # 分页
    # 获得第几页
    num_page=request.GET.get('num_page')
    # 设置默认num_page
    if not num_page:
        num_page=1
    # 获得一二级分类对象
    # 获得一级分类对象
    books_type_one = TTypes.objects.filter(parent_id__isnull=True)
    # 获得二级分类对象
    books_type_two = TTypes.objects.filter(parent_id__isnull=False)
    # 排序
    if sort_obj:
        if sort_obj=='2':
            str_sort='sales'
        elif sort_obj=='3':
            str_sort='book_dprice'
        elif sort_obj == '4':
            str_sort='publish_time'
        if asc_or_dsc=='dsc':
            str_sort="%s"%('-')+str_sort
        books_type_object_list = books_type_object_list.order_by(str_sort)
        # 获得分页对象,分页数量为6
    pagtor=Paginator(books_type_object_list,per_page=6).page(num_page)
    return render(request,'mainapp/booklist.html',{
        # 分页对象
        'books_type_object_list':pagtor,
        # 类型名列表
        'book_types_list':book_types_list,
        # 一级分类对象
        'books_type_one': books_type_one,
        # 二级2分类对象
        'books_type_two': books_type_two,
        # 小类的id
        "books_type":books_type,
        # 大类的id
        'books_type_big':books_type_big,
        # 用户名
        'userobj': userobj,
    })



