from datetime import datetime

import sqlalchemy as sa

from taskmanager import db, app

class TOdo(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    content =db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.now())
    completed = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return '<Task %r>' % self.id

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email_address = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

user_test_db = db.Table(
    "user_book",
    db.Column("test",db.ForeignKey(User.user_id),primary_key=True ),
    db.Column("tes1",db.ForeignKey(User.user_id),primary_key=True )
)


with app.app_context():
    db.create_all()
    db.session.commit()