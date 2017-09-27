# -*- coding: utf-8 -*-
import MySQLdb
from flask import Flask, g, request

app = Flask(__name__)
app.debug = True

MYSQL_HOST='rm-uf6m8zukp6b06mxwyo.mysql.rds.aliyuncs.com'
MYSQL_PORT=3306
MYSQL_USER='root' 
MYSQL_PASS='Hubang1994'
MYSQL_DB='xinlang'


@app.before_request
def before_request():
    g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,MYSQL_DB, port=int(MYSQL_PORT),charset="utf8")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'): g.db.close()

@app.route('/')
def hello():
    return "Hello, world! - Flask"

@app.route('/demo', methods=['GET', 'POST'])
def greeting():
    html = ''   
    if request.method == 'POST':      
        if request.form['text'] !='':
            c = g.db.cursor()    
            c.execute("insert test(text) values(%s)", (request.form['text']))
            g.db.commit()
    html += """
    <form action="" method="post">
        <div><textarea cols="40" name="text"></textarea></div>
        <div><input type="submit" /></div>
    </form>
    """
    c = g.db.cursor()
    c.execute('select * from test')
    msgs = list(c.fetchall())
    msgs.reverse()
    for row in msgs:
        html +=  '<p>' + row[-1] + '</p>'

    return html