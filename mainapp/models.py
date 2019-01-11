# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAdress(models.Model):
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=30)
    detail_address = models.CharField(max_length=30)
    detail_address1 = models.CharField(max_length=30)
    detail_address2 = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    telphone = models.BigIntegerField(blank=True, null=True)
    addr_mobile = models.BigIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_adress'


class TBooks(models.Model):
    type = models.ForeignKey('TTypes', models.DO_NOTHING, blank=True, null=True)
    book_name = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_publish = models.CharField(max_length=50)
    publish_time = models.DateField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    book_isbn = models.CharField(max_length=50, blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    open_type = models.CharField(max_length=50, blank=True, null=True)
    book_paper = models.CharField(max_length=50, blank=True, null=True)
    book_wrapper = models.CharField(max_length=50, blank=True, null=True)
    book_price = models.FloatField(blank=True, null=True)
    book_dprice = models.FloatField(blank=True, null=True)
    product_image_path = models.CharField(max_length=100, blank=True, null=True)
    series_name = models.CharField(max_length=100, blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    impression = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    shelves_date = models.DateField(blank=True, null=True)
    customer_socre = models.FloatField(blank=True, null=True)
    book_status = models.IntegerField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_books'


class TOrder(models.Model):
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    adress = models.ForeignKey(TAdress, models.DO_NOTHING, blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)
    create_date = models.TimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_order'


class TOrderiterm(models.Model):
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBooks, models.DO_NOTHING, blank=True, null=True)
    shop_num = models.IntegerField()
    total_price = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_orderiterm'


class TTypes(models.Model):
    class_name = models.CharField(max_length=30, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_types'


class TUser(models.Model):
    user_email = models.CharField(max_length=30)
    user_password = models.CharField(max_length=80)
    user_name = models.CharField(max_length=30)
    user_status = models.SmallIntegerField()
    blank1 = models.CharField(max_length=70, blank=True, null=True)
    blank2 = models.CharField(max_length=70, blank=True, null=True)
    blank3 = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_user'
