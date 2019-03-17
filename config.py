import logging
import redis


class Config(object):
    """工程配置信息"""
    # 默认日志等级
    LOG_LEVEL = logging.DEBUG

    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    DEBUG = True

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/aiqiyi"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session 配置
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 指定session保存的redis
    SESSION_PERMANENT = False #设置需要过期
    PERMANENT_SESSION_LIFETIME = 86400 * 2  # session 的有效期，单位是秒


class DevelopementConfig(Config):
    """开发模式下的配置"""
    pass


class ProductionConfig(Config):
    """生产模式下的配置"""
    pass


# 定义配置字典
config = {
    "development": DevelopementConfig,
    "production": ProductionConfig
}