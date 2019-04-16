# 0.导入蓝图
from flask import Blueprint

# 1.初始化蓝图对象
mmonly_blu = Blueprint("mmonly",__name__)

from . import views

