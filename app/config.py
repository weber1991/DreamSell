import sys
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 判断系统类型，然后设置sqlite的兼容性
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class Config:
    # CSRF的密钥，设置才可以防止跨站点
    SECRET_KEY = 'woshizuiqiang'

class ProdConfig(Config):
    '''生产模式'''
    # "mysql+pymysql://user:password@ip:port/db_name"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:weber@localhost:3306/learn_flask"


class DevConfig(Config):
    '''
    开发模式，调用本地的数据库
    '''
    debug = True
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'DreamSell.db')
    SQLALCHEMY_ECHO = True # 输出显示sql语句
