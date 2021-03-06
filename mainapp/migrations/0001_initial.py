# Generated by Django 2.0.6 on 2018-12-29 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('detail_address', models.CharField(max_length=30)),
                ('detail_address1', models.CharField(max_length=30)),
                ('detail_address2', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField()),
                ('telphone', models.BigIntegerField(blank=True, null=True)),
                ('addr_mobile', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_adress',
            },
        ),
        migrations.CreateModel(
            name='TBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('book_publish', models.CharField(max_length=50)),
                ('publish_time', models.DateField(blank=True, null=True)),
                ('revision', models.IntegerField(blank=True, null=True)),
                ('book_isbn', models.CharField(blank=True, max_length=50, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('page_count', models.IntegerField(blank=True, null=True)),
                ('open_type', models.CharField(blank=True, max_length=50, null=True)),
                ('book_paper', models.CharField(blank=True, max_length=50, null=True)),
                ('book_wrapper', models.CharField(blank=True, max_length=50, null=True)),
                ('book_price', models.FloatField(blank=True, null=True)),
                ('book_dprice', models.FloatField(blank=True, null=True)),
                ('product_image_path', models.CharField(blank=True, max_length=100, null=True)),
                ('series_name', models.CharField(blank=True, max_length=100, null=True)),
                ('printing_time', models.DateField(blank=True, null=True)),
                ('impression', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('shelves_date', models.DateField(blank=True, null=True)),
                ('customer_socre', models.FloatField(blank=True, null=True)),
                ('book_status', models.IntegerField(blank=True, null=True)),
                ('sales', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_books',
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.BigIntegerField(blank=True, null=True)),
                ('create_date', models.TimeField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('status', models.SmallIntegerField(blank=True, null=True)),
                ('adress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TAdress')),
            ],
            options={
                'db_table': 't_order',
            },
        ),
        migrations.CreateModel(
            name='TOrderiterm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_num', models.IntegerField()),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TBooks')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TOrder')),
            ],
            options={
                'db_table': 't_orderiterm',
            },
        ),
        migrations.CreateModel(
            name='TTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=30, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_types',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=30)),
                ('user_password', models.CharField(max_length=80)),
                ('user_name', models.CharField(max_length=30)),
                ('user_status', models.SmallIntegerField()),
                ('blank1', models.CharField(blank=True, max_length=70, null=True)),
                ('blank2', models.CharField(blank=True, max_length=70, null=True)),
                ('blank3', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
        migrations.AddField(
            model_name='torder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tbooks',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TTypes'),
        ),
        migrations.AddField(
            model_name='tadress',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
    ]
