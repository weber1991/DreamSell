from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True) # 编号
    username = db.Column(db.String(100)) # 用户名
    password = db.Column(db.String(100)) # 密码
    email = db.Column(db.String(100), unique=True) # 邮箱
    phone = db.Column(db.String(11), unique=True) # 手机号码
    consumption = db.Column(db.DECIMAL(10,2), default = 0) # 消费额
    addtime = db.Column(db.Datetime, index = True. default=datetime.now)

    orders = db.relationship('Orders', backref = 'user') # 订单外键关系关联

    def __repr__(self):
        return '<User %r>'% self.username
    
    def check_password(self, password):
        '''
        检测密码是否正确
        :param password:密码
        :return : 返回布尔值
        '''
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)

# 管理员类：单独使用一个类来做后台管理员，而不是使用用户来添加权限
class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key = True)
    manager = db.Column(db.String(100), unique = True) # 管理员账号
    password = db.Column(db.String(100)) 

    def __repr__(self):
        return "<Admin %r>"% self.manager

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)



'''
实现类别的方法：
1、使用多个类：如果碰到多种关系，那就要很多个类
2、使用无限递归的方式来（待优化）
'''

#商品的分类，大分类
class SuperCat(db.Model):
    __tablename__ = "supercat"
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100)) # 大分类名称
    addtime = db.Column(db.Datetime, index = True, default=datetime.now)

    # 关联关系
    subcat = db.relationship("Subcat", backref="supercat") # 和小类进行关联
    goods = db.relationship("Goods", backref="supercat") # 和商品进行关联

    def __repr__(self):
        return "<SuperCat %r>" % self.cat_name

# 商品的分类，小分类
class Subcat(db.Model):
    __tablename__  = "subcat"
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100)) # 分类名称
    addtime = db.Column(db.Datetime, index = True, default=datetime.now)
    
    # 关联关系
    supercat_id = db.relationship(db.Integer, db.ForeignKey('supercat.id') ) # 和大类进行关联
    goods = db.relationship("Goods", backref="subcat") # 和商品进行关联

    def __repr__(self):
        return "<SubCat %r>" % self.cat_name

# 商品类
class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255)) # 商品名称
    original_price = db.Column(db.DECIMAL(10,2)) # 原价
    current_price = db.Column(db.DECIMAL(10,2)) # 现价
    picture = db.Column(db.String(255))  # 用来存放图片的路径
    introduction = db.Column(db.Text) # 介绍
    view_count = db.Column(db.Integer, default = 0) # 浏览次数
    is_sale = db.Column(db.Boolean(), default = 0) # 是否特价
    is_now = db.Column(db.Boolean(), default = 0) # 是否新品
    addtime = db.Column(db.Datetime, default = datetime.now, index=True)

    # 待优化
    # is_sell = db.Column(db.Boolean(), default = 0) # 是否在售
    
    # 关系关系
    supercat_id = db.Column(db.Integer, db.ForeignKey('supercat.id'))
    subcat_id = db.Column(db.Integer, db.ForeignKey('subcat.id'))
    catr = db.relationship("Cart", backref = 'goods') # 和购物车关联
    orders_detail = db.relationship("OrderDetail", backref = "goods") # 和订单关联

    def __repr__(self):
        return "<Goods %r>" % self.name

# 购物车类
class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key = True)
    addtime = db.Column()
    number = db.Column() # 购买数量

    # 关联关系
    good_id = db.Column()
    user_id = db.Column()
