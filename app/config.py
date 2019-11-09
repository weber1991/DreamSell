import sys
import os

# 获取当前路径
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
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://(username):(password)@localhost:3306/(database_name)"


class DevConfig(Config):
    '''
    开发模式，调用本地的数据库
    '''
    debug = True
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'DreamSell.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 设置sqlalchemy结构修改权限（源代码中没有，不写会报警告错误）
    SQLALCHEMY_ECHO = True # 输出显示sql语句
