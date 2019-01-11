import os
import django
from django.test import TestCase

# Create your tests here.

# 测试
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "middle_project.settings")
django.setup()
#
# from mainapp.models import TTypes
#
# obj=TTypes.objects.create(class_name ='测试类',parent_id =1)
# print(obj.id)
from mainapp.models import TAdress, TUser
from datetime import datetime

# print(datetime.date())

# userobj_id =TUser.objects.get(id=1)
# address_obj =TAdress.objects.create(user =userobj_id,
#                                            name ="111",
#                                            detail_address ="111",
#                                            zipcode ="111",
#                                            telphone=111,
#                                            addr_mobile=111,)



