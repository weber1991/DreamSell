from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
def create_app(config_name):
    '''
    作用：创建并初始化一个app，而根据情况调用config文件里面的配置类
    '''

    print("config_name is %s" % config_name)
    # 实例一个flask项目
    app = Flask(__name__)

    # 调入相关配置
    app.config.from_object(config_name)

    # 将数据库注册到app里面
    db.init_app(app)
    
    # 导入和注册蓝图


    return app