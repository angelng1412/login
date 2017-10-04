from flask import Flask, render_template, request, session
import os 

app = Flask(__name__)
app.secret_key = os.urandom(32)

username = 'username'
password = 'password'

@app.route('/')
def root():
    if session.has_key('name'):
        return render_template('welcome.html', user = session['name'])
    else: 
        return render_template('form.html')

@app.route('/route', methods = ['POST'])
def route():
    if request.form['user'] == username:
        session['name'] = request.form['user']
        return render_template('welcome.html', user = request.form['user'])
    else:
        return render_template('error.html')


#return render_template('response.html', user = request.form['data'], method = request.method)

if __name__ == '__main__':
    app.debug = True
    app.run()
