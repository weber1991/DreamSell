# _*_ codding:utf-8 _*_
import os
from app import create_app, db
from flask_script import Shell, Manager, Server
from flask_migrate import Migrate, MigrateCommand


env = os.environ.get("InWorld_ENV", "Dev") # 调用系统的环境变量的值，如果没有则使用dev
app = create_app("app.config.%sConfig" % env.capitalize())

# 调用flask_script扩展
manager = Manager(app)

# 调用flask_migrate扩展
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)

# 添加shell命令，同时初始化shell的变量
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("server", Server())

# 再添加db命令，将flask_script和flask_migrate关联起来
manager.add_command("db", MigrateCommand)


@app.errorhandler(404)
def page_not_found(error):
    """
    404
    """
    # return render_template("home/404.html"), 404
    return "404"

if __name__ == '__main__':
    '''
    使用flak_script模块来对flask项目调试
    1、先需要利用create_app来创建flask项目
    2、再把flask_script模块和flask项目进行关联，添加相关的参数以实现不同的功能
    3、运行该文件，并根据需要输入不同的参数
    '''
    manager.run()