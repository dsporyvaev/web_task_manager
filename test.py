from email.policy import default

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import delete
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
db = SQLAlchemy(app)

class TOdo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content =db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.now())
    completed = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return '<Task %r>' % self.id


with app.app_context():
    db.create_all()
    db.session.commit()


@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = TOdo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/home')
        except:
            return 'An issue occured'
    else:
        tasks = TOdo.query.order_by(TOdo.date_created).all()
        return render_template('home.html', item_name='Phone', tasks=tasks)

@app.route('/delete/<int:id>')
def delete_task(id):
    task_to_delete = TOdo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/home')
    except:
        return 'There was an unexpected error'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = TOdo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/home')
        except:
            return 'ERrror'
    else:
        return render_template('update.html', task=task)




@app.route('/register')
def register_page():
    return render_template('reg_page.html')

@app.route('/login')
def login_page():
    return render_template('login_page.html')


if __name__ == "__main__":
    app.run(debug=True)
