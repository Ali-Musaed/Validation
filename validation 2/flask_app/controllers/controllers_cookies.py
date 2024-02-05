from flask_app import app
from flask import request, render_template, redirect, session
from flask_app.models.models_cookies import Cookie
# from flask_app.models.models_customers import Customer
# from flask_app.controllers import controllers_customers
@app.route('/')
def index():

    cookies = Cookie.get_all()
    return render_template('index.html', cookies = cookies)

@app.route('/insert_info', methods = ['POST'])
def insert_into():
    data = {
        'first_name' : request.form['first_name'],
        'cookie_type' : request.form['cookie_type'],
        'num_of_boxes' : request.form['num_of_boxes']
    }
    if not Cookie.validate_cookie(request.form):
        session['first_name'] = request.form['first_name']
        session['cookie_type'] = request.form['cookie_type']
        session['num_of_boxes'] = request.form['num_of_boxes']
        print('fail')
        return redirect('/order_up')
    else:
        Cookie.save(data)
        session.clear()
        print('hello')
        return redirect('/')

@app.route("/delete/<int:cookie_id>")
def delete(cookie_id):
    data = {
        'id' : cookie_id
    }
    Cookie.delete(data, cookie_id)
    return redirect('/')

@app.route("/update/<int:cookie_id>")
def switch(cookie_id):
    data = {
        'id' : cookie_id
    }
    cookie = Cookie.get_one(data)
    
    return render_template('edit.html', cookie = cookie)

@app.route("/update/<int:cookie_id>", methods =['POST'])
def update(cookie_id):
    if not Cookie.validate_order(request.form):
        
        print('fail')
        return redirect(f"/update/{request.form['id']}")
    else:
        print('hello')
        Cookie.update(request.form, cookie_id)
        return redirect('/')
@app.route('/home')
def home():
    return redirect('/')

@app.route('/order_up')
def back():
    return render_template('order_up.html')