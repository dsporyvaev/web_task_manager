from taskmanager import app
from taskmanager.models import db
from flask import render_template, request,redirect
from taskmanager.models import TOdo

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
        return render_template('home.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task_to_delete = TOdo.query.get_or_404(task_id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/home')
    except:
        return 'There was an unexpected error'

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = TOdo.query.get_or_404(task_id)
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