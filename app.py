from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import make_response
from flask import session
from flask import redirect
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH']

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/static/')
def static_page():
    return '<p>static<p/>'


@app.route('/int/<int:nums>')
def int_static(nums):
    return f"input num is { nums }"


@app.route('/string/<string:str>')
def string_static(str):
    return f"input str is {str}"


@app.route('/path/<path:cur_path>')
def path_static(cur_path):
    return f"you cur path is {cur_path}"


@app.route('/methods/', methods=['GET', 'POST'])
def f_methods():
    if request.method == "GET":
        return "GET"
    if request.method == "POST":
        return "POST"


@app.route('/name/<string:name>')
def username(name):
    return render_template('index.html', name=name)


@app.route('/student/')
def student():
    return render_template('student.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == "POST":
        result = request.form
        return render_template('result.html', result=result)


@app.route('/set_cookies')
def set_cookies():
    response = make_response('success')
    response.set_cookie('chiudk','luanqibazhaodecookie', max_age=3600)
    return response


@app.route('/get_cookies')
def get_cookies():
    cookie_1 = request.cookies.get('chiudk')
    return cookie_1


@app.route('/del_cookies')
def del_cookies():
    response = make_response('del sucess')
    response.delete_cookie('chiudk')
    return response


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/index')
def index():
    if 'username' in session:
        return '''
        <p>用户 {0} 已登陆成功
        <p><a href='/logout'>点击注销登陆</a>
        '''.format(session["username"])
    return '''
     <p><h1>你未登陆</h1>
     <p><h1><a href="/login">点击这里登陆</a></h1>
    '''


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for('index'))
    return '''
    <form method="POST">
      <p><input type=text name=username>
      <p><input type=submit value=Login>
    </ from>
    '''


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))


@app.route('/hostinfo', methods=["POST", "GET"])
def hostinfo():
    if request.method == "POST":
        host = request.form.get('host')
        return render_template('hostinfo.html', host=host)


@app.route('/insert_host')
def insert_host():
    return render_template('insert_host.html')

@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        file.save(os.path.join('static', file.filename))
    return render_template('upload.html')

@app.route('/dict', methods=["POST","GET"])
def dicts():
    hosts = {'ip': '192.168.31.100', 'hostname': 'master01', 'username': 'root', 'cpu': 'Intel-i9-13900k'}
    return render_template('hosts.html', zhujixinxi=hosts)


@app.route('/staticfile')
def static_file():
    return render_template('staticfile.html')
if __name__ == '__main__':
    app.run()





