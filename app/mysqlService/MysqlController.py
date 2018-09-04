from app import app
from flask import request,json
from app.mysqlService.MysqlService import MysqlService


@app.route('/getSecheduleById',methods=['POST','GET'])
def getSecheduleById():
    if(request.method=='POST'):
        data=request.get_data()
        data=str(data, encoding = "utf-8") #binary转string
        data = json.loads(data)
        id=data['id']  # 获取到用户的学号
        mysql = MysqlService()
        res=mysql.querySchedule(id)
        print(res)
        if(res==None):
           return 'none'
        else:
           return json.dumps(res)
    elif(request.method=='GET'):
        return 'ahahhahahh'

@app.route('/getContact')
def getContacts():
    mysql = MysqlService()
    res=mysql.queryContacts();
    if(res==None):
        return 'none'
    else:
        print(res)
        return json.dumps(res)
