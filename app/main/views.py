from flask import render_template,request,redirect,url_for,abort,flash
from ..models import User,Blogs,Comments,PhotoProfile
from .. import db,photos
import markdown2  
from .forms import BlogForm, UpdateProfile,CommentForm
# from app import auth
from . import main
from flask_login import login_required,current_user
#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
 
    title='Personal blog'
    return render_template('index.html',title=title)
    



@main.route('/blogs/recently/<int:id>', methods=['POST', 'GET'])
def recent_blogs(id):
    blogs=Blogs.query.filter_by(id).all()
    return render_template('recently.html', blogs=blogs)

def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname = user.username))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    # return render_template('profile/update.html',form = form)



@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))

@main.route('/blogs/new/', methods= ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        details= form.details.data
        blog_id =current_user
        title= form.title.data
        # print(current_user._get_current_object().id)
        new_blogs = Blogs(blog_id=current_user._get_current_object().id, details=details, title=title)
        new_blogs.save_blog()

        return redirect(url_for('main.all_blogs'))

    return render_template('blog.html', form=form)


@main.route('/comment/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def del_comment(id):
    comment= Comments.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    flash ('you have succesfully deleted the comment')
    return redirect(url_for('main.all_blogs'))
@main.route('/comment/new/<int:blogs_id>', methods=['GET','POST'])
# @login_required
def add_comment(blogs_id):
    form = CommentForm()
    blog = Blogs.query.get(blogs_id)
    if form.validate_on_submit():
        details= form.details.data
        add_comment= Comments(user_id=current_user._get_current_object().id, blogs_id=blogs_id)
        db.session.add(add_comment)
        db.session.commit()

        return redirect(url_for('.add_comment', blogs_id=blogs_id))
    allComents= Comments.query.filter_by(blogs_id=blogs_id).all()
    return render_template('comment.html',form=form, allComents=allComents,blog =blog)


@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def updateBlog(id):
    blog=Blogs.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    flash('you have succesfully deleted the comment')
    return redirect(url_for('main.all_blogs'))