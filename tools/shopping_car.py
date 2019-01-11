# 导入书籍类
from mainapp.models import TBooks
# 创建购物车类和书籍类

# 创建书籍类,有两属性，书籍id和书籍数量，书籍数量默认为1
# 删除数量为0
# 传入书籍id
class Book():
    # 初始化
    def __init__(self,book,count=1):
        # 书籍id
        self.book=book
        self.bookCount=int(count)
        self.book_del_count=0
#     删除书籍
    def del_books(self):
        self.book_del_count=self.bookCount
        # print(self.book_del_count)
        self.bookCount=0
#     恢复书籍
    def recover_book_count(self):
        self.bookCount=self.book_del_count
        # print(self.bookCount)
        self.book_del_count=0


# 创建car购物车类，有当当总价，和节省的价格
class Car():
#     初始化，初始化书籍列表，当当总价，和节省的价格均为0
    def __init__(self):
        # 初始化书籍列表
        self.book_list=[]
        # ，当当总价，
        self.total_price=0
        # 节省的价格
        self.save_price=0
#     计算总价
    def count_sum_price(self):
        # 初始化当当总价和节省价格
        self.total_price=0
        self.save_price = 0
        # 遍历列表，统计价格
        for i in self.book_list:
            self.total_price=(i.book.book_dprice)*(i.bookCount)+self.total_price
            self.save_price=(i.book.book_price-i.book.book_dprice)*(i.bookCount)+self.save_price

#     向购物车添加商品
#     添加书籍到购物车,传入书籍id和书籍数量,默认为1
    def add_book(self,bookId,intoBookCount=1):
        # 如果列表中对象存在，则数量加一
        bookId=int(bookId)

        intoBookCount=int(intoBookCount)
        for i in self.book_list:
            if i.book.id==bookId:
                i.bookCount+=intoBookCount
                self.count_sum_price()
                return None
        # 如果不存在则向列表添加一本书
        book=TBooks.objects.get(id=bookId)
        self.book_list.append(Book(book,intoBookCount))
        self.count_sum_price()
#   数量改变
    def book_change(self,bookId,intoBookCount=1):
        # 如果列表中对象存在，则数量改变
        bookId = int(bookId)
        intoBookCount = int(intoBookCount)
        for i in self.book_list:
            if i.book.id == bookId:
                i.bookCount = intoBookCount
                self.count_sum_price()
                return None


#删除购物车商品
    def delete_book(self,bookId):
        bookId=int(bookId)
        for i in self.book_list:
            if i.book.id==bookId:
                i.del_books()
                self.count_sum_price()
                return None

# 恢复购物车商品
    def recover_car_book(self,bookId):
        bookId=int(bookId)
        for i in self.book_list:
            if i.book.id==bookId:
                i.recover_book_count()
                self.count_sum_price()
                return None
