from flask import Flask, render_template, flash, redirect, request, session, url_for
import sqlite3
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GvennLcr_A01-2021'

con = sqlite3.connect('database.db')
c = con.cursor()

c.execute('''CREATE TABLE users 
            (id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )''')

con.commit()

@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template('index.html', username = session.get("USERNAME"))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message  = ''

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT username FROM users WHERE username = ? AND password = ?", (username, hashlib.sha256(password.encode('utf8')).hexdigest(),))
            response = cur.fetchone()

        if response is None:
            message = 'Incorrect Username/Password'
            flash(message)

            return render_template('login.html', message = message)
        else:
            session['USERNAME'] = username

            return render_template('index.html', username = session.get("USERNAME"))

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('USERNAME', None)

    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm  = request.form['confirm']
        message  = ''

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT username FROM users WHERE username = ?", (username,))
            response = cur.fetchone()

        if username == "":    
            message = 'Please input something as an username !'
            flash(message)

            return render_template('signup.html', message = message)
        else:
            if response is not None:
                message = 'User already registered !'
                flash(message)

                return render_template('signup.html', message = message)
            else:
                if password != confirm:
                    message = 'Passwords do not match !'
                    flash(message)

                    return render_template('signup.html', message = message)
                else:
                    with sqlite3.connect('database.db') as con:
                        cur = con.cursor()
                        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashlib.sha256(password.encode('utf8')).hexdigest(),))
                        con.commit()

                    session['USERNAME'] = username

                    return render_template('index.html', username = session.get("USERNAME"))

    return render_template('signup.html')

@app.route("/profile/<user>", methods = ['GET', 'POST'])
def userProfile(user):
    flag     = ''

    if session.get("USERNAME") is None:
        return redirect(url_for("login"))
    else:
        if user == 'admin':
            flag = "TARTETATIN{b77ebadba0c90e8fd3b8a8b0d36ef7adb4458ebb}"
        else:
            flag = "There is no flag here, it is located on the admin profile !"

        return render_template("profile.html", username = user, flag = flag)

if  '__main__' == __name__:
    from waitress import serve
    serve(app, host = "0.0.0.0", port = 80)