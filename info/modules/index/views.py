from info import redis_store
from info.modules.index import index_blu


# 2.蓝图注册路由
@index_blu.route('/')
def index():
    # 向redis中保存一个值name xuxue
    redis_store.set("name", "it")
    return 'hello'
