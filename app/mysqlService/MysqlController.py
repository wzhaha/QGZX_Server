from app.mysqlService.MysqlService import MysqlService
from app import app

@app.route('/addUser')
def addUser():
    MysqlService.addUser('')
