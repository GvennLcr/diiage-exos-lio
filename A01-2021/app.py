from flask import Flask, render_template, flash, request
from database import *
import sqlite3
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DIIIIIIIIIIIIIIIIIIIIIIIAGE'

@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/api/v1/login', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        msg      = ''

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT username, isadmin FROM users WHERE username = '{0}' AND password = '{1}'".format(username, hashlib.md5(password.encode('utf8')).hexdigest()))
            response = cur.fetchone()

        if response is None:
            msg = 'Incorrect Username/Password'
            flash(msg)

            return render_template('login.html', msg=msg)
        else:
            flag=''

            if response[1] == 1:
                flag="ok"
                return render_template('inbox.html', username=username, flag=flag)
            else:
                flag="There is no mail here, but you did get the correct password !"
                return render_template('flag.html', username=username, flag=flag)

    return render_template('login.html')

@app.route('/api/v2/login', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        msg      = ''

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT username, isadmin FROM users WHERE username = ? AND password = ?", (username, hashlib.md5(password.encode('utf8')).hexdigest(),))
            response = cur.fetchone()

        if response is None:
            msg = 'Incorrect Username/Password'
            flash(msg)

            return render_template('login.html', msg=msg)
        else:
            flag=''

            if response[1] == 1:
                flag="ok"
                return render_template('inbox.html', username=username, flag=flag)
            else:
                flag="There is no mail here, but you did get the correct password !"
                return render_template('flag.html', username=username, flag=flag)

    return render_template('login.html')

@app.route('/api/v1/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

@app.route("/api/v1/admin/debug", methods = ['GET', 'POST'])
def debug():
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        response = cur.fetchall()

    return render_template("debug.html", response=response)

if  '__main__' == __name__:
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)