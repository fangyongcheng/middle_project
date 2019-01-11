from random import sample
import string

# 创建随机的4位数字符串为了验证码

def code_four():
    str1=string.digits+string.ascii_letters
    code=sample(str1,4)
    code=''.join(code)
    return code

