from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Hahaha!'


from app.mysqlService.MysqlController import *