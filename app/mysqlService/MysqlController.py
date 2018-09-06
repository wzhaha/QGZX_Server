from app import app
from flask import request,json
from app.mysqlService.MysqlService import MysqlService
import datetime

#菜单页
# 获取学生个人信息
@app.route('/getUserInfoById',methods=['POST'])
def getUserInfo():
    data=request.get_data()
    data=str(data,encoding='utf=8')
    data=json.loads(data)
    id=data['id']
    mysql=MysqlService()
    res=mysql.selectUserInfo(id)
    if(res==None):
        return 'none'
    else:
        return json.dumps(res)

#获取值班记录
@app.route('/getTaskHistry',methods=['POST'])
def getTaskHistry():
    data = request.get_data()
    data = str(data, encoding='utf=8')
    data = json.loads(data)
    id = data['id']
    mysql = MysqlService()
    res=mysql.sign_search(id)
    if (res == None):
        return 'none'
    else:
        return json.dumps(res)

# 获取所有值班的联系方式
@app.route('/getContact')
def getContacts():
    mysql = MysqlService()
    res=mysql.queryContacts();
    if(res==None):
        return 'none'
    else:
        print(res)
        return json.dumps(res)


# 提交建议
@app.route('/insertSuggestion',methods=['POST'])
def insertSuggestion():
    data = request.get_data()
    data = str(data, encoding="utf-8")  # binary转string
    data = json.loads(data)
    id = data['id']  # 获取到用户的学号
    content=data['content']
    mysql=MysqlService()
    mysql.insertSuggestion(id,content)
    return '200'

# 获取学生本人本周所有的值班
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

#获取今日值班
@app.route('/getDaySchedule',methods=['POST'])
def getDaySchedule():
    d = datetime.datetime.now()
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    week=d.weekday()
    data = request.get_data()
    data = str(data, encoding="utf-8")  # binary转string
    data = json.loads(data)
    id = data['id']  # 获取到用户的学号
    mysql = MysqlService()
    res = mysql.queryDaySchedule(id,week+1,day)
    print(res)
    if (res == None):
        return 'none'
    else:
        return json.dumps(res)

# 获取当前值班的人的信息
@app.route('/getNowPeople',methods=['GET'])
def getNowPeople():
    d = datetime.datetime.now()
    week = d.weekday()
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    print(day)
    hour = datetime.datetime.now().strftime('%H')
    minute=datetime.datetime.now().strftime('%M')
    section=transferTime(int(hour),int(minute))
    if(section==0):
        return 'none'
    else:
        mysql=MysqlService()
        res=mysql.queryNowSchedule(week+1,section,day)
        return json.dumps(res)


# 签到
@app.route('/sign',methods=['POST'])
def sign():
    data = request.get_data()
    data = str(data, encoding="utf-8")  # binary转string
    data = json.loads(data)
    id = data['id']  # 获取到用户的学号
    section=data['section'] #当前时间段
    status=data['status'] #签到状态
    position=data['position'] #值班位置
    day = datetime.datetime.now().strftime('%Y-%m-%d') # 当前时间
    mysql = MysqlService()
    if(status==1 or status==3):
        mysql.sign(id,day,section,status,position)
    else:
        mysql.sign_out(id, day, section, status)
    return '200'

#根据时间获取当前是第几个时间段
def transferTime(hour,minute):
    total=hour*60+minute
    if(total>=500 and total<=590):
        return 1
    elif (total >= 610 and total <= 700):
        return 2
    elif (total >= 850 and total <= 960):
        return 3
    elif (total >= 970 and total <= 1060):
        return 4
    else:
        return 0
