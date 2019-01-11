import uuid,os
# 传入扩展名，生成唯一id

def pictrue_name(filename):
    id=str(uuid.uuid4())
    extend_name=os.path.splitext(filename)[1]
    return id+extend_name