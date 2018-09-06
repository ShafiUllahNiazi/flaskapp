from datetime import datetime
from flaskapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    # follo = db.relationship('Follow', backref='foll', lazy=True)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def __repr__(self):
        return "User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    post_image = db.Column(db.String(100),nullable=True)
    post_type = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return "Post('{self.title}', '{self.date_posted}')"

# class Follow(db.Model):
#
#
#     # follower = db.Column(db.Integer, primary_key=True,nullable=False)
#     # following = db.Column(db.Integer, primary_key=True,nullable=False)
#
#     # follower = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     following = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     f_id = db.Column(db.Integer, primary_key=True)
#
#     # followerr= db.relationship('User',db.foreign_keys[follower])
#     # followerr = db.relationship('User', db.foreign_keys[follower])
#
#     def __repr__(self):
#         return "Follow('{self.follower}', '{self.following}')"
