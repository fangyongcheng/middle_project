from django.urls import path
from shopping_car_app import views

# 购物车app别名：
app_name='shopping_car_app'

# 购物车路由系统
urlpatterns = [
#     购物车视图函数路由
    path('shopping_car_view/',views.shopping_car_view,name="shopping_car_view"),
#     地址页面视图路由
    path("shopping_car_indent_view/",views.shopping_car_indent_view,name="shopping_car_indent_view"),
# 购物车订单完成视图路由
    path("shopping_car_indent_ok_view/",views.shopping_car_indent_ok_view,name="shopping_car_indent_ok_view"),
#     添加书减少数到购物车函数路由
    path("add_book_into_car/",views.add_book_into_car,name="add_book_into_car"),
#     改变书数量到购物车路由
    path('change_book_into_car/',views.change_book_into_car,name='change_book_into_car'),
#     删除书路由
    path('delete_book/',views.delete_book,name='delete_book'),
#     恢复书
    path("find_book/",views.find_book,name="find_book"),
#     顾客确定路由
    path("customer_sure_view/",views.customer_sure_view,name='customer_sure_view'),
#     订单提交提交判断路由
    path("user_indent_dispose/",views.user_indent_dispose,name="user_indent_dispose"),

]
