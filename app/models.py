from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  FileStorage
from flask_login import UserMixin,current_user

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Quotes:
    quote_list=[]
    def __init__(self,author,id,quote,permanentlink) :
        self.author=author
        self.id=id
        self.quote=quote
        self.permanentlink=permanentlink

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    blog = db.relationship("Blogs", backref="user", lazy="dynamic")
    comments = db.relationship('Comment', backref = 'user', passive_deletes=True,lazy = 'dynamic')

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    def save_blogs(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(comment_id=id).all()
        return comments
    def __repr__(self):
        return f'User {self.username}'
class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer)
    blog_title = db.Column(db.String)
    the_blog = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    comment = db.relationship('Comments', backref='blog', lazy="dynamic")
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_blogs(cls, id):
        blogs= Blogs.query.filter_by(blog_id=id)
        return blogs
    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(comment_id=id).all()
        return comments
    @classmethod
    def getBlogsId(cls, id):
        blogs = Blogs.query.filter_by(id=id).first()
        return blogs
    @classmethod
    def clear_blogs(cls):
        Blogs.all_blogs.clear()

    def __repr__(self):
        return f'Blogs {self.the_blog}'

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment_id = db.Column(db.Integer)
    blog_comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.order_by(Comments.posted.desc()).filter_by(pitches_id=id).all()
        return comments
    def del_comment(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment: id:{self.id} comment: {self.blog_comment}'
        
class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'
    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))



