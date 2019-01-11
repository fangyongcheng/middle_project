from django.urls import path
from mainapp import views

# app别名
app_name='mainapp'

# 路由
urlpatterns = [
    # 主页面路由
    path('index/',views.index_view,name='index'),
    # 图书详情页路由
    path('bookDetail/',views.book_detail_view,name='bookDetail'),
    # 图书分类路由
    path('booklist/',views.book_list_view,name='booklist'),
]
