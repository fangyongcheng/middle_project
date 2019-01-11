import os,django
import uuid

from django.test import TestCase

# Create your tests here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "middle_project.settings")
django.setup()
from mainapp import models
import random,string

#
# models.TBooks.objects.create(book_name = '《遮天》',
#     book_author = '辰东',
#     book_publish = '浙江文艺出版社',
#     publish_time = '2018-11-10',
#     revision = 10,
#     book_isbn = 9787533946340,
#     word_count = 80000000,
#     page_count = 1800,
#     open_type = '16k',
#     book_paper = '轻型纸',
#     book_wrapper = '平装-胶订',
#     book_price = 588,
#     book_dprice = 500,
#     product_image_path = 'images/1yuan240-120.jpg',
#     series_name = '网络玄幻小说系列从书',
#     printing_time = '2018-10-10',
#     impression = 10,
#     stock = 10,
#     shelves_date ='2018-12-10',
#     customer_socre = 10,
#     book_status = True,
#     sales = 11000,
#     type=models.TTypes.objects.get(id=47)
# )
#
# 添加书的脚本
def add_message(n):
    num=0
    for i in range(n):
        num+=1
        book_val=ran_num(3)
        book_dval=book_val-50
        models.TBooks.objects.create(book_name =ran_book_name(),
            book_author = add__book_author(),
            book_publish = '浙江文艺出版社',
            publish_time = pubish(),
            revision = 10,
            book_isbn = 9787533946340,
            word_count = 80000000,
            page_count = 1800,
            open_type = '16k',
            book_paper = '轻型纸',
            book_wrapper = '平装-胶订',
            book_price = book_val,
            book_dprice = book_dval,
            product_image_path = 'images/'+str(num)+'.jpg',
            series_name = '军事系列从书',
            printing_time = pubish(),
            impression = 10,
            stock = 10,
            shelves_date =pubish(),
            customer_socre = random.randint(1,10),
            book_status = True,
            sales = 0,
            type=models.TTypes.objects.get(id=random.randint(16,25))
        )
#
# 书名
def ran_book_name():
    strs=' 道可道非常道名可名非常名无名天地之始有名万物之母故常无欲以观其妙常有欲以观其徼此两者同出而异名同谓之玄玄之又玄众妙之门。 '
    str1=''.join(random.sample(strs,5))
    name='《'+str1+"》"
    return name
# 作者
def add__book_author():
    strs=' 道可道非常道名可名非常名无名天地之始有名万物之母故常无欲以观其妙常有欲以观其徼此两者同出而异名同谓之玄玄之又玄众妙之门。 '
    str1 = ''.join(random.sample(strs, 3))
    return str1
# 出版时间
def pubish():
    str1 = '20'+str(ran_num(1))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28))
    return str1
def ran_num(n):
    return random.randint(10**n,10**n*9)

# add_message(24)
# user_obj = models.TUser.objects.create(user_name="ww", user_email="txt", user_password="wqeqw",
#                                        user_status=1, blank2=uuid.uuid4())

